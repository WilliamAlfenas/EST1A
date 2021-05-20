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

#preencher com a questão 10
class Doencas(models.Model):
    nome = models.CharField("Nome popular", max_length=200, unique=True)
    nome_tecnico = models.CharField("Nome Técnico", max_length=300, unique=True)
    def __str__(self): 
        return f'{self.nome}/{self.nome_tecnico}'
    class Meta:
        verbose_name_plural = "Teve alguma destas doenças"
        verbose_name = "Teve alguma destas doenças"

#preencher com a questão 15
class Medicoes_Indicadas(models.Model):
    nome = models.CharField("Nome", max_length=200, unique=True)
    def __str__(self): 
        return f'{self.nome}'
    class Meta:
        verbose_name_plural = "Medicações Regulares"
        verbose_name = "Medicação regular"

#preencher com a questão 16
class Medicoes_Estudo(models.Model):
    nome = models.CharField("Nome", max_length=200, unique=True)
    def __str__(self): 
        return f'{self.nome}'
    class Meta:
        verbose_name_plural = "Medicações em Estudo"
        verbose_name = "Medicação em Estudo"

#preencher com a questão 19, 20, 21
class Agravantes(models.Model):
    nome = models.CharField("Nome", max_length=200, unique=True)
    def __str__(self): 
        return f'{self.nome}'
    class Meta:
        verbose_name_plural = "Habitos agravantes"
        verbose_name = "Habito agravante"

class Medicacao_Diaria(AutoDesc, models.Model):
    nome = models.CharField("Nome", max_length=200, unique=True)
    descricao = models.CharField("Descrição", max_length=400)
    class Meta:
        verbose_name_plural = "Medicações diárias"
        verbose_name = "Medicação Diária"

class Paciente(models.Model):
    form_consentimento = models.FileField("Formulário de Consentimento", upload_to='consentimento/%Y/%m/%d/', null=True, blank=True)
    tipo_paciente = models.CharField("Tipo de Paciente", max_length=128, 
        choices=[
            (t, t)
            for t in [
                'Profilaxia',
                'Assintomático',
                'Sintomático'
            ]
        ], default='Profilaxia')
    nome = models.CharField("Nome completo", max_length=200, unique=True)
    nome_mae = models.CharField("Nome da Mãe", max_length=200)
    dt_nasc = models.DateField("Data de Nascimento", null = True, blank= True)
    cidade_nasc = models.ForeignKey(Cidade, on_delete = models.SET_NULL, null = True,
        related_name="cidade_nasc",
        verbose_name="Cidade de Nascimento", blank= True)

    idade = models.IntegerField("Idade", blank= True, null = True)
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
            ] + ['não sabe']
        ], null=True)
    etnia = models.CharField("Etnia", max_length=32, 
        choices=[
            (t, t)
            for t in [
                'Branco',
                'Negro',
                'Pardo',
                'Indígena',
                'Amarelo'
            ]
        ], default='Branco')
    alergias = models.ManyToManyField(Alergia, null = True, blank= True, verbose_name="Alergia a remédio - se sim, qual(is)")

    jah_covid = models.CharField("Já teve Covid 19", max_length=128, 
        choices=[
            (t, t)
            for t in [
                'Não',
                '1º Contato',
                '2º Contato',
                '3º ou + vezes',
                'POSITIVO APÓS SOROLOGIA SEM SINTOMAS'
            ]
        ], default='Não')

    jah_doencas = models.ManyToManyField(Doencas, null = True
        , verbose_name="Já teve alguma dessas doenças")
        
    dt_ini_sintomas = models.DateField("Data de Início dos Sintomas", null = True, blank= True)
    sintomas = models.ManyToManyField(Sintoma, null = True, blank= True, verbose_name="Teve sintomas - se sim, qual(is)")
    dt_ini_trat = models.DateField("Data de Início do Tratamento com o Grupo", null = True, blank= True)

    proc_ajuda_antes = models.CharField("Procurou ajuda antes de iniciar nosso tratamento", max_length=32, 
        choices=[
            (t, t)
            for t in [
                'Não',
                'Publico',
                'Privado',
                'Publico e Privado'
            ]
        ], default='Não')

    internado_antes = models.CharField("Já ficou internado para tratamento do Covid", max_length=32, 
        choices=[
            (t, t)
            for t in [
                'Não',
                'Enfermaria',
                'UTI'
            ]
        ], default='Não')
    internado_tempo = models.CharField("Tempo de internação", max_length=32, 
        choices=[
            (t, t)
            for t in [
                'Não foi internado',
                '00 - 05 dias',
                '05 - 10 dias',
                '10 - 15 dias',
                '+ 15 dias'
            ]
        ], default='Não foi internado')

    motivo_test_covid = models.CharField("Motivo para o Teste Covid", max_length=128, 
        choices=[
            (t, t)
            for t in [
                'Não fez por Motivos Financeiros',
                'Não fez pq não teve sintomas',
                'Não fez pq os sintomas estavam leves',
                'Não fez pq não nenhum médico solicitou',
                'Fez o Teste Rapido',
                'Fez o RT PCR',
                'Fez a Sorologia'
            ]
        ], default='Não fez por Motivos Financeiros')

    medic_reg_indicada = models.ManyToManyField(Medicoes_Indicadas, null = True, blank= True, 
        verbose_name="Medicações regulares indicadas por outros profissionais da saúde")

    medic_est_associada = models.ManyToManyField(Medicoes_Estudo, null = True, blank= True, 
        verbose_name="Medicações em Estudo indicadas ou tomadas por contra própria")
    
    tomou_antes_ch = models.CharField("Tomou Medicações em Estudo antes do tratamento", max_length=128, 
        choices=[
            (t, t)
            for t in [
                'Sim, tomou ANTES de iniciar o Tratamento',
                'Sim, tomou APÓS iniciar o Tratamento',
                'Não'
            ]
        ], default='Não')

    comorbidades = models.ManyToManyField(Comorbidade, null = True, blank= True)
    medicacao_diaria2 = models.ManyToManyField(Medicacao_Diaria, null = True, blank= True,
    verbose_name="Medicação Diária")

    agravantes = models.ManyToManyField(Agravantes, null = True, blank= True)
    
    cidade = models.ForeignKey(Cidade, on_delete = models.SET_NULL, null = True,
        verbose_name="Residência atual")

    exame = models.FileField("Exame", upload_to='exames/%Y/%m/%d/', null=True, blank=True)
    origem = models.ForeignKey(Origem, on_delete=models.SET_NULL, null = True, blank = True, verbose_name = "Indicação")


    #não especificado

    fase = models.ForeignKey(Fase, on_delete = models.SET_NULL, null = True)
    tratamentos = models.ManyToManyField(Forma_Tratamento, null = True,
        verbose_name="Posologia")
    #outros_tratamentos = models.CharField("Outros Tratamentos", max_length=2000, blank= True, null = True)
    tempo_rec = models.IntegerField("Tempo de uso da Invermectina", blank= True, null = True)
    questionario = models.FileField("Questionário", upload_to='questionarios/%Y/%m/%d/', null=True, blank=True)
    #diag_final = models.CharField("Diagnóstico Final", max_length=200, blank=True)
    diagfinal = models.ForeignKey(DiagFinal, verbose_name="Diagnóstico Final", blank=True, null=True, on_delete=models.SET_NULL)

    @property
    def imc(self):
        if self.altura == 0: return 0
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
    dia10 = models.BooleanField("D10", null = False, blank= True, default=False)
    dia11 = models.BooleanField("D11", null = False, blank= True, default=False)
    dia12 = models.BooleanField("D12", null = False, blank= True, default=False)
    dia13 = models.BooleanField("D13", null = False, blank= True, default=False)
    dia14 = models.BooleanField("D14", null = False, blank= True, default=False)
    dia15 = models.BooleanField("D15", null = False, blank= True, default=False)
    
    class Meta:
        verbose_name_plural = "Sintomas por dias"
        verbose_name = "Sintoma por dias"
    
class Medicoes_dia(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null= False)
    
    @property
    def calc_intervalo(): pass
    
    medicao = models.CharField("Tipo de Medição", max_length=32, 
        choices=[
            (t, t)
            for t in [
                'Temperatura',
                'Frequência cardiáca',
                'Frequência respiratória',
                'Pressão Arterial Sistólica',
                'Pressão Arterial Diastólica',
                'Saturação de O2'
            ]
        ], default='Temperatura')
    dia1 = models.FloatField("D1", null = True, blank= True)
    dia2 = models.FloatField("D2", null = True, blank= True)
    dia3 = models.FloatField("D3", null = True, blank= True)
    dia4 = models.FloatField("D4", null = True, blank= True)
    dia5 = models.FloatField("D5", null = True, blank= True)
    dia6 = models.FloatField("D6", null = True, blank= True)
    dia7 = models.FloatField("D7", null = True, blank= True)
    dia8 = models.FloatField("D8", null = True, blank= True)
    dia9 = models.FloatField("D9", null = True, blank= True)
    dia10 = models.FloatField("D10", null = True, blank= True)
    dia11 = models.FloatField("D11", null = True, blank= True)
    dia12 = models.FloatField("D12", null = True, blank= True)
    dia13 = models.FloatField("D13", null = True, blank= True)
    dia14 = models.FloatField("D14", null = True, blank= True)
    dia15 = models.FloatField("D15", null = True, blank= True)
    
    class Meta:
        verbose_name_plural = "Medições por dias"
        verbose_name = "Medição por dias"

class MetricasExame(AutoDesc, models.Model):
    nome = models.CharField("Nome", max_length=200, unique=True)
    descricao = models.CharField("Descrição", max_length= 400)
    class Meta:
        verbose_name_plural = "Métricas de Exame"
        verbose_name = "Métrica"
    
class ResultadosExames(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null= False)

    data = models.DateField("Data", null = True, blank= True)
    
    met1 = models.ForeignKey(MetricasExame, related_name='m1', on_delete=models.SET_NULL, null= True, blank= True)
    val1 = models.FloatField("Valor", null= True, blank= True)
    
    met2 = models.ForeignKey(MetricasExame, related_name='m2', on_delete=models.SET_NULL, null= True, blank= True)
    val2 = models.FloatField("Valor", null= True, blank= True)