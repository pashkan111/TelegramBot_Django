# Generated by Django 3.2.4 on 2021-06-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='user',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='sales_prise',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True),
        ),
    ]