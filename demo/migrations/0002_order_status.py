# Generated by Django 3.1.4 on 2022-06-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Новая'), ('repairing', 'Ремонтируется'), ('renovated', 'Отремонтировано')], default='new', max_length=254, verbose_name='Статус'),
        ),
    ]