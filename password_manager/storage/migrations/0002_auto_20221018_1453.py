# Generated by Django 3.1 on 2022-10-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание'),
        ),
    ]