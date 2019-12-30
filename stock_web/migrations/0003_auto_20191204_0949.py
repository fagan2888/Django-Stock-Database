# Generated by Django 2.2.6 on 2019-12-04 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_web', '0002_auto_20191202_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='internal',
            options={'verbose_name_plural': 'Internal IDs'},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'Inventory Items'},
        ),
        migrations.AlterModelOptions(
            name='reagents',
            options={'verbose_name_plural': 'Reagents'},
        ),
        migrations.AlterModelOptions(
            name='solutions',
            options={'verbose_name_plural': 'Solutions'},
        ),
        migrations.AlterModelOptions(
            name='storage',
            options={'verbose_name_plural': 'Storage'},
        ),
        migrations.AlterModelOptions(
            name='suppliers',
            options={'verbose_name_plural': 'Suppliers'},
        ),
    ]
