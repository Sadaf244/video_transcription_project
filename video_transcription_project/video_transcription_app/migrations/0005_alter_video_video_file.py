# Generated by Django 4.2 on 2023-04-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_transcription_app', '0004_alter_video_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]