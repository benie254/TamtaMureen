# Generated by Django 4.0.6 on 2022-07-25 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tam', '0022_rename_menu_preorder_menu_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preorder',
            name='menu_item',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
