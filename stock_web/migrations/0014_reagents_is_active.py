# Generated by Django 2.2.6 on 2019-12-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_web', '0013_auto_20191220_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='reagents',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
