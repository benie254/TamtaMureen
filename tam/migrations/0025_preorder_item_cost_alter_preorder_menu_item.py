# Generated by Django 4.0.6 on 2022-07-25 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tam', '0024_remove_preorder_email_preorder_your_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='preorder',
            name='item_cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='preorder',
            name='menu_item',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
