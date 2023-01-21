# Generated by Django 4.1.5 on 2023-01-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_rename_menucategories_menucategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menucategory',
            options={'ordering': ['category_name'], 'verbose_name': 'Категория меню', 'verbose_name_plural': ' Категории меню'},
        ),
        migrations.AddField(
            model_name='menucategory',
            name='category_name',
            field=models.TextField(default='Название блюда', max_length=50, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='menucategory',
            name='category_price',
            field=models.FloatField(default=0, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='menucategory',
            name='category_quant',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AddField(
            model_name='menucategory',
            name='category_type',
            field=models.CharField(default='Название категории', max_length=50, verbose_name='Категория'),
        ),
    ]