# Generated by Django 4.0.6 on 2022-07-21 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tam', '0015_super'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super',
            name='bio',
        ),
        migrations.AddField(
            model_name='super',
            name='about_me',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
