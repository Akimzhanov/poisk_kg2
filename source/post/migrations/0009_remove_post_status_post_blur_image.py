# Generated by Django 4.1.3 on 2022-11-24 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_post_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='blur_image',
            field=models.ImageField(blank=True, upload_to='blur_images'),
        ),
    ]
