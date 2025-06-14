# Generated by Django 5.1.6 on 2025-05-25 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_alter_document_save_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='save_path',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Путь к сохранённому документу относительно C:\\Users\\servi\\Desktop\\кфу 3 - без матов не описать\\_репорт-креатор\\ReportCreator\\backend\\media\\docs'),
        ),
        migrations.AlterField(
            model_name='documentsvalues',
            name='document_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_id', to='backend.document'),
        ),
        migrations.CreateModel(
            name='TableField',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Русское название поля (для отображения)')),
                ('key_name', models.CharField(max_length=50, verbose_name='Английское название поля (по которому будет доступ в API)')),
                ('is_required', models.BooleanField(default=False, verbose_name='Обязательное поле?')),
                ('related_item', models.CharField(editable=False, max_length=30, verbose_name='К какому виду записи относится это поле (заполняется программно)')),
                ('type', models.CharField(choices=[('TEXT', 'Текстовое поле'), ('NUMBER', 'Числовое поле'), ('DATE', 'Дата и время'), ('CURRENCY', 'Денежная сумма'), ('BOOL', 'Логическое поле'), ('USER', 'ФИО другого участника'), ('COMBOBOX', 'Выпадающий список из других записей')], max_length=10, verbose_name='Тип поля')),
                ('related_info', models.JSONField(editable=False, null=True, verbose_name='Дополнительная информация для этого поля при related_item = COMBOBOX')),
                ('placeholder', models.CharField(max_length=50, null=True, verbose_name='Подсказка для заполнения поля')),
                ('validation_regex', models.CharField(max_length=200, null=True, verbose_name='Регулярное выражение для валидации')),
                ('secure_text', models.BooleanField(default=False, verbose_name='Это защищённое поле?')),
                ('error_text', models.TextField(null=True, verbose_name='Текст ошибки при валидации')),
                ('is_custom', models.BooleanField(default=False, editable=False, verbose_name='Это поле создано пользователем?')),
                ('order', models.IntegerField(verbose_name='Порядок столбца')),
                ('related_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.template', verbose_name='Связанный шаблон')),
            ],
        ),
        migrations.CreateModel(
            name='TableValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_number', models.IntegerField(default=0, verbose_name='Номер строки таблицы')),
                ('value', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_id_table', to='backend.document')),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_field', to='backend.tablefield')),
            ],
        ),
        migrations.AddConstraint(
            model_name='tablefield',
            constraint=models.UniqueConstraint(fields=('key_name', 'related_item'), name='table_field_key_name_related_item_combination'),
        ),
        migrations.AddConstraint(
            model_name='tablefield',
            constraint=models.UniqueConstraint(fields=('order', 'related_template'), name='table_field_order_related_item_combination'),
        ),
        migrations.AlterUniqueTogether(
            name='tablevalues',
            unique_together={('row_number', 'document_id', 'table_id')},
        ),
    ]
