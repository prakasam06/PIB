# Generated by Django 4.2.5 on 2023-12-19 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsgatherers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news_cluster_head',
            old_name='sentiment_analysis_result',
            new_name='SENTIMENT_ANALYSIS_RESULT',
        ),
        migrations.AlterField(
            model_name='news_cluster_head',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 12, 25, 57, 968183, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='news_obj',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 12, 25, 57, 969195, tzinfo=datetime.timezone.utc)),
        ),
    ]
