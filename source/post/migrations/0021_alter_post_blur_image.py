# Generated by Django 4.1.3 on 2022-12-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_alter_post_blur_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blur_image',
            field=models.ImageField(upload_to='blur_images'),
        ),
    ]