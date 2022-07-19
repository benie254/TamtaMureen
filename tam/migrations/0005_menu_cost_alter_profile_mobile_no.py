# Generated by Django 4.0.6 on 2022-07-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tam', '0004_alter_menu_status_alter_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile_no',
            field=models.PositiveIntegerField(),
        ),
    ]