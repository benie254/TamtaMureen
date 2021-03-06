# Generated by Django 4.0.6 on 2022-07-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tam', '0013_alter_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile_no',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('away', 'away')], max_length=60, null=True),
        ),
    ]
