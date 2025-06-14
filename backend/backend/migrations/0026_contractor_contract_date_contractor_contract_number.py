# Generated by Django 5.1.6 on 2025-05-29 17:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_contractor_company_names_combination'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='contract_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractor',
            name='contract_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
