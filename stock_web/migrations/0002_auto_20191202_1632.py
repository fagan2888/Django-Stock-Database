# Generated by Django 2.2.6 on 2019-12-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forcereset',
            name='force_password_change',
            field=models.BooleanField(default=True),
        ),
    ]
