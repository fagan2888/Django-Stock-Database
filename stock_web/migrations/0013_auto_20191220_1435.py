# Generated by Django 2.2.6 on 2019-12-20 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_web', '0012_auto_20191219_1843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reagents',
            options={'ordering': ['name'], 'verbose_name_plural': 'Reagents'},
        ),
        migrations.AddField(
            model_name='inventory',
            name='witness',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='4+', to=settings.AUTH_USER_MODEL),
        ),
    ]
