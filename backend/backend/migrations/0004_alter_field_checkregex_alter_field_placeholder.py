# Generated by Django 5.1.6 on 2025-04-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_field_placeholder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='checkRegex',
            field=models.CharField(max_length=200, null=True, verbose_name='Регулярное выражение для валидации'),
        ),
        migrations.AlterField(
            model_name='field',
            name='placeholder',
            field=models.CharField(max_length=50, null=True, verbose_name='Подсказка для заполнения поля'),
        ),
    ]
