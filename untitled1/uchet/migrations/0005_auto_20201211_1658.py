# Generated by Django 3.1.4 on 2020-12-11 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uchet', '0004_auto_20201211_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
