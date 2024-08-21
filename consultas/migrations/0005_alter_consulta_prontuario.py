# Generated by Django 4.2.6 on 2024-08-18 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0004_consulta_prontuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='prontuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consulta_prontuario', to='consultas.prontuario'),
        ),
    ]