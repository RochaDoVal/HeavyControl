# Generated by Django 5.2 on 2025-04-12 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('atividade', models.CharField(max_length=100)),
                ('horimetro_final', models.IntegerField()),
                ('horimetro_abastecimento', models.IntegerField()),
                ('quantidade_litros', models.IntegerField()),
            ],
        ),
    ]
