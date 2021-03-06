# Generated by Django 4.0.4 on 2022-05-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, verbose_name='Email почта')),
                ('number_of_telephone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
