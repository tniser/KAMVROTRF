# Generated by Django 4.1.5 on 2023-01-20 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0009_alter_menucategory_category_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menucategory',
            old_name='category_type',
            new_name='category_menu',
        ),
    ]