# Generated by Django 4.2.5 on 2023-10-08 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsgatherers', '0006_youtube_csv_data_video_json_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtube_csv_data',
            name='video_json_data',
        ),
    ]
