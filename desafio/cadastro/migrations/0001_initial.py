# Generated by Django 3.0.3 on 2020-03-01 19:51

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
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=30)),
            ],
        ),
    ]