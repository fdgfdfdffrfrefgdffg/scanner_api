# Generated by Django 5.0.6 on 2024-06-26 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oquvchi', '0002_remove_oquvchi_face_img_oquvchi_face_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='oquvchi',
            name='manzil',
            field=models.CharField(default='.', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oquvchi',
            name='phone',
            field=models.CharField(default='.', max_length=15),
            preserve_default=False,
        ),
    ]
