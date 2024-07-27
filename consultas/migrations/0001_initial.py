# Generated by Django 5.0.6 on 2024-07-27 17:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_consulta', models.DateTimeField()),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('paciente', models.ForeignKey(limit_choices_to={'is_paciente': True}, on_delete=django.db.models.deletion.CASCADE, related_name='consultas_como_paciente', to=settings.AUTH_USER_MODEL)),
                ('profissional', models.ForeignKey(limit_choices_to={'is_profissional': True}, on_delete=django.db.models.deletion.CASCADE, related_name='consultas_como_profissional', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]