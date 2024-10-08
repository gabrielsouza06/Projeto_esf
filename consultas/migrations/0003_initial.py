# Generated by Django 4.2.6 on 2024-08-12 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('consultas', '0002_initial'),
        ('estabelecimento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prontuario',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prontuarios_paciente', to='usuarios.usuario'),
        ),
        migrations.AddField(
            model_name='prontuario',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prontuarios_profissional', to='usuarios.usuario'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='estabelecimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas_estabelecimento', to='estabelecimento.estabelecimento'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas_paciente', to='usuarios.usuario'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas_profissional', to='usuarios.usuario'),
        ),
    ]
