# Generated by Django 5.0.6 on 2024-07-31 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chiqish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oquvchi_id', models.IntegerField()),
                ('sana', models.DateField()),
                ('vaqt', models.TimeField()),
            ],
        ),
    ]
