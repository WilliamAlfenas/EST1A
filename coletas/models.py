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

class Tratamento(AutoDesc, models.Model):
    class Meta:
        verbose_name = 'Tratamento antigo'
    nome = models.CharField("Nome", max_length=200, unique=True)
    descricao = models.CharField("Descrição", max_length=400)

class Forma_Tratamento(models.Model):
    substancia = models.CharField("Substância", max_length=200, unique=True)
    descricao = models.CharField("Descrição", max_length=400)

    class Meta:
        verbose_name = 'Forma de Tratamento'
        verbose_name_plural = 'Formas de Tratamento'

    def __str__(self):
        return self.substancia

class Comorbidade(AutoDesc, models.Model):
    nome = models.CharField("Nome", max_length=200, unique=True)
    descricao = models.CharField("Descrição", max_length=400)

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
    alergias = models.ManyToManyField(Alergia, null = True, blank= True, verbose_name="Alergia a remédio - se sim, qual(is)")
    sintomas = models.ManyToManyField(Sintoma, null = True, blank= True, verbose_name="Teve sintomas - se sim, qual(is)")
    
    fase = models.ForeignKey(Fase, on_delete = models.SET_NULL, null = True)
    tratamento = models.ForeignKey(Tratamento, on_delete = models.SET_NULL, null = True, blank = True)
    tratamentos = models.ManyToManyField(Forma_Tratamento, null = True)
    outros_tratamentos = models.CharField("Outros Tratamentos", max_length=400, blank= True)
    comorbidades = models.ManyToManyField(Comorbidade, null = True, blank= True)
    cidade = models.ForeignKey(Cidade, on_delete = models.SET_NULL, null = True)
    medicacao_diaria = models.CharField("Medicação Diária", max_length=400, blank= True)
    tempo_rec = models.IntegerField("Tempo de Recuperação (dias)")
    exame = models.FileField("Exame", upload_to='exames/%Y/%m/%d/', null=True, blank=True)
    questionario = models.FileField("Questionário", upload_to='questionarios/%Y/%m/%d/', null=True, blank=True)
    diag_final = models.CharField("Diagnóstico Final", max_length=200, blank=True)

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
        return f'{s.nome}, {s.idade} anos, IMC {s.imc:.2f} - {s.grau_obesidade} -> {s.tratamento}'

class Dias_Sintoma(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null= False)

    def calc_intervalo(): pass

    @property
    def intervalo(self):
        print(self)
        return 'Dias 1, 2 e 3:'
    
    sintomas1 = models.ManyToManyField(Sintoma, related_name='DiasSin1', null = True, blank= True, verbose_name="Dias 1, 4 e 7")
    sintomas2 = models.ManyToManyField(Sintoma, related_name='DiasSin2', null = True, blank= True, verbose_name="Dias 2, 5 e 8")
    sintomas3 = models.ManyToManyField(Sintoma, related_name='DiasSin3', null = True, blank= True, verbose_name="Dias 3, 6 e 9")
    
    class Meta:
        verbose_name_plural = "Sintomas por dia"
        verbose_name = "Sintomas por dias"