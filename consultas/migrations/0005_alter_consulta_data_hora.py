# Generated by Django 5.0.6 on 2024-07-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0004_remove_consulta_data_consulta_consulta_data_hora_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='data_hora',
            field=models.DateTimeField(),
        ),
    ]
