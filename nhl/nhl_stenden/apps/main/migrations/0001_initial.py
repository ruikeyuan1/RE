# Generated by Django 4.0.3 on 2022-06-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, verbose_name='Почта')),
                ('password', models.CharField(max_length=200, verbose_name='Пароль')),
                ('username', models.CharField(max_length=20, verbose_name='Имя')),
                ('birth_date', models.IntegerField()),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
