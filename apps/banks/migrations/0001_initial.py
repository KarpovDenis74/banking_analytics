# Generated by Django 3.2.7 on 2021-09-17 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_name', models.CharField(max_length=256, verbose_name='Польное наименование')),
                ('sort_name', models.CharField(max_length=256, verbose_name='Cjrращенное наименование')),
            ],
            options={
                'ordering': ['sort_name'],
            },
        ),
    ]