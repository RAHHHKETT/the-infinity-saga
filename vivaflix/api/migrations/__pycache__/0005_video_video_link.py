# Generated by Django 5.1.6 on 2025-03-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
