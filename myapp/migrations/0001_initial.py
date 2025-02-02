# Generated by Django 4.2.11 on 2024-05-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inspetor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Inpetor',
                'verbose_name_plural': 'Inspetor',
                'ordering': ['-id'],
            },
        ),
    ]
