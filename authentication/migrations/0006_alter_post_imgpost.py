# Generated by Django 3.2.25 on 2025-04-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_post_videopost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='IMGpost',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
