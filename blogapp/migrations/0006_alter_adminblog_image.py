# Generated by Django 5.1.2 on 2024-12-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_adminblog_image_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminblog',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
