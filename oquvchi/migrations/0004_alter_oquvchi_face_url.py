# Generated by Django 5.0.6 on 2024-06-27 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oquvchi', '0003_oquvchi_manzil_oquvchi_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oquvchi',
            name='face_url',
            field=models.ImageField(upload_to='media'),
        ),
    ]
