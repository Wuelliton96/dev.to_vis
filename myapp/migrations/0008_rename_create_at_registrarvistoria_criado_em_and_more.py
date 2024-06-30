# Generated by Django 4.2.11 on 2024-05-04 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_inspetor_options_rename_code_vistoria_codigo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrarvistoria',
            old_name='create_at',
            new_name='criado_em',
        ),
        migrations.RenameField(
            model_name='registrarvistoria',
            old_name='dt_end',
            new_name='dt_fim',
        ),
        migrations.RenameField(
            model_name='registrarvistoria',
            old_name='dt_start',
            new_name='dt_inicio',
        ),
        migrations.RenameField(
            model_name='vistoria',
            old_name='esta_locado',
            new_name='esta_vistoriado',
        ),
        migrations.AlterField(
            model_name='registrarvistoria',
            name='vistoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reg_locacao', to='myapp.vistoria'),
        ),
    ]
