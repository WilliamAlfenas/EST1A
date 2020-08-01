from django.db import models

# Create your models here.

class AutoDesc():
    nome: str
    descricao: str
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome + ' -> ' + self.descricao

class Alergia(models.Model):
    substancia = models.CharField("Substância", max_length=200, unique=True)
    def __str__(self):
        return self.substancia

class Sintoma(AutoDesc, models.Model): 
    nome = models.CharField("Nome", max_length=200, unique=True)
    descricao = models.CharField("Descrição", max_length=400)
    
    def __str__(self):
        return self.nome

class Fase(AutoDesc, models.Model):
    nome = models.CharField("Nome", max_length=200, unique=True)
    descricao = models.CharField("Descrição", max_length=400)

class Forma_Tratamento(models.Model):
    substancia = models.CharField("Substância", max_length=200, unique=True)
    descricao = models.CharField("Descrição", max_length=400)
    posologia = models.CharField("Posologia", max_length=100, null= True)

    class Meta:
        verbose_name = 'Forma de Tratamento'
        verbose_name_plural = 'Formas de Tratamento'

    def __str__(self):
        return self.substancia

class Comorbidade(AutoDesc, models.Model):
    nome = models.CharField("Nome", max_length=200, unique=True)
    descricao = models.CharField("Descrição", max_length=400)

class DiagFinal(AutoDesc, models.Model):
    nome = models.CharField("Nome", max_length=200, unique=True)
    descricao = models.CharField("Descrição", max_length=400)
    class Meta:
        verbose_name_plural = "Diagnosticos Finais"
        verbose_name = "Diagnóstico final"

class Cidade(models.Model):
    nome = models.CharField("Nome", max_length=200, unique=True)
    estado = models.CharField("Estado", max_length=2)
    def __str__(self): 
        return f'{self.nome}/{self.estado}'

class Origem(AutoDesc, models.Model):
    nome = models.CharField("Nome", max_length=200, unique=True)
    descricao = models.CharField("Descrição", max_length= 400)
    class Meta:
        verbose_name_plural = "Indicações"
        verbose_name = "Indicação"

class Paciente(models.Model):
    form_consentimento = models.FileField("Formulário de Consentimento", upload_to='consentimento/%Y/%m/%d/', null=True, blank=True)
    nome = models.CharField("Nome completo", max_length=200, unique=True)
    origem = models.ForeignKey(Origem, on_delete=models.SET_NULL, null = True, blank = True, verbose_name = "Indicação")
    idade = models.IntegerField("Idade")
    sexo = models.CharField("Sexo", max_length=1, 
        choices=[
            ('M', 'Masculino'),
            ('F', 'Feminino')
        ])
    peso = models.FloatField("Peso (kg)")
    altura = models.IntegerField("Altura (cm)")
    tipo_sang = models.CharField("Tipo Sanguíneo", max_length=16, 
        choices=[
            (tp, tp)
            for tp in [
                s + rh
                for s in ['A', 'B', 'AB', 'O']
                for rh in ['+', '-']
            ]
        ], null=True)
    alergias = models.ManyToManyField(Alergia, null = True, blank= True, verbose_name="Alergia a remédio - se sim, qual(is)")
    sintomas = models.ManyToManyField(Sintoma, null = True, blank= True, verbose_name="Teve sintomas - se sim, qual(is)")
    
    fase = models.ForeignKey(Fase, on_delete = models.SET_NULL, null = True)
    tratamentos = models.ManyToManyField(Forma_Tratamento, null = True)
    outros_tratamentos = models.CharField("Outros Tratamentos", max_length=400, blank= True)
    comorbidades = models.ManyToManyField(Comorbidade, null = True, blank= True)
    cidade = models.ForeignKey(Cidade, on_delete = models.SET_NULL, null = True)
    medicacao_diaria = models.CharField("Medicação Diária", max_length=400, blank= True)
    tempo_rec = models.IntegerField("Tempo de Recuperação (dias)")
    exame = models.FileField("Exame", upload_to='exames/%Y/%m/%d/', null=True, blank=True)
    questionario = models.FileField("Questionário", upload_to='questionarios/%Y/%m/%d/', null=True, blank=True)
    #diag_final = models.CharField("Diagnóstico Final", max_length=200, blank=True)
    diagfinal = models.ForeignKey(DiagFinal, verbose_name="Diagnóstico Final", blank=True, null=True, on_delete=models.SET_NULL)

    @property
    def imc(self):
        return self.peso / (self.altura/100) **2

    @property
    def grau_obesidade(self):
        graus = [
            (18.5, 'Magreza', 0),
            (25,   'Normal', 0),
            (30,   'Sobrepeso', 1),
            (40,   'Obesidade', 2),
            (400,  'Obesidade Grave', 3),
        ]
        
        for limite, nome, _ in graus:
            if self.imc < limite:
                return nome

        return graus[-1][1]

    def __str__(self):
        s = self
        return f'{s.nome}, {s.idade} anos, IMC {s.imc:.2f} - {s.grau_obesidade}'

class Dias_Sintoma(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null= False)

    def calc_intervalo(): pass

    @property
    def intervalo(self):
        print(self)
        return 'Dias 1, 2 e 3:'
    sintoma = models.ForeignKey(Sintoma, null = True, blank = True, on_delete = models.CASCADE)
    
    dia1 = models.BooleanField("D1", null = False, blank= True, default=False)
    dia2 = models.BooleanField("D2", null = False, blank= True, default=False)
    dia3 = models.BooleanField("D3", null = False, blank= True, default=False)
    dia4 = models.BooleanField("D4", null = False, blank= True, default=False)
    dia5 = models.BooleanField("D5", null = False, blank= True, default=False)
    dia6 = models.BooleanField("D6", null = False, blank= True, default=False)
    dia7 = models.BooleanField("D7", null = False, blank= True, default=False)
    dia8 = models.BooleanField("D8", null = False, blank= True, default=False)
    dia9 = models.BooleanField("D9", null = False, blank= True, default=False)
    
    class Meta:
        verbose_name_plural = "Sintomas por dias"
        verbose_name = "Sintoma por dias"
    
class Medicoes_dia(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null= False)

    medicao = models.CharField("Tipo de Medição", max_length=32, 
        choices=[
            (t, t)
            for t in [
                'Temperatura',
                'Frequência cardiáca',
                'Frequência respiratória',
                'Pressão Arterial',
                'Saturação de O2'
            ]
        ], default='Temperatura')
    dia1 = models.FloatField("D1")
    dia2 = models.FloatField("D2")
    dia3 = models.FloatField("D3")
    dia4 = models.FloatField("D4")
    dia5 = models.FloatField("D5")
    dia6 = models.FloatField("D6")
    dia7 = models.FloatField("D7")
    dia8 = models.FloatField("D8")
    dia9 = models.FloatField("D9")
    
    class Meta:
        verbose_name_plural = "Medições por dias"
        verbose_name = "Medição por dias"