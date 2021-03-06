# Generated by Django 3.1.6 on 2021-02-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.IntegerField(max_length=11)),
                ('endereco', models.TextField(max_length=100)),
                ('telefone', models.IntegerField(max_length=11)),
                ('sexo', models.BooleanField(blank=True, null=True)),
                ('grupo', models.CharField(max_length=2)),
            ],
        ),
    ]
