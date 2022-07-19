# Generated by Django 4.0.6 on 2022-07-19 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tam', '0005_menu_cost_alter_profile_mobile_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tam.menu')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
