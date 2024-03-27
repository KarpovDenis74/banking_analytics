# Generated by Django 3.2.10 on 2024-03-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_is_email_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='open_pass',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=25, verbose_name='Код подтверждения email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('admin', 'admin')], default='user', max_length=10, verbose_name='Роль'),
        ),
    ]