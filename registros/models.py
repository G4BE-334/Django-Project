from django.db import models
from projetoSiteCactus import settings
from cpf_field.models import CPFField

# Create your models here.

class Cliente(models.Model):
    clienteid = models.AutoField(db_column='ClienteID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', unique=True, max_length=14)  # Field name made lowercase.
    endereco = models.CharField(db_column='Endereco', max_length=100)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=15)  # Field name made lowercase.
    datanasc = models.DateField(db_column='DataNasc')  # Field name made lowercase.
    grupoid = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='GrupoID')  # Field name made lowercase.
    recomendacaoid = models.ForeignKey('Recomendacao', models.DO_NOTHING, db_column='RecomendacaoID', blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.EmailField(db_column='Email', max_length=45)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9)

    class Meta:
        managed = False
        db_table = 'cliente'
    def __str__(self):
        return self.nome

class Grupo(models.Model):
    grupoid = models.AutoField(db_column='GrupoID', primary_key=True)  # Field name made lowercase.
    qtd = models.IntegerField(db_column='Qtd', default=0)  # Field name made lowercase.
    grupo = models.CharField(db_column='Grupo', max_length=20, unique=True)  # Field name made lowercase.
    criadorid = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='CriadorID', null=True, blank = True)

    class Meta:
        managed = False
        db_table = 'grupo'
    def __str__(self):
        return self.grupo

class Recomendacao(models.Model):
    recomendacaoid = models.AutoField(db_column='RecomendacaoID', primary_key=True)  # Field name made lowercase.
    qtd = models.IntegerField(db_column='Qtd', default=0)  # Field name made lowercase.
    recomendadorid = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='RecomendadorID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recomendacao'
    def __str__(self):
        return self.recomendacaoid

