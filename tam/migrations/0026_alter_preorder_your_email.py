# Generated by Django 4.0.6 on 2022-07-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tam', '0025_preorder_item_cost_alter_preorder_menu_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preorder',
            name='your_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]