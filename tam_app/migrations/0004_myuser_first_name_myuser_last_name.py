# Generated by Django 4.0.6 on 2022-11-07 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tam_app', '0003_contact_ingredient_quote_alter_myuser_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='last name'),
        ),
    ]