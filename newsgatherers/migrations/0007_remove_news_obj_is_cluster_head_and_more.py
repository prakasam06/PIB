# Generated by Django 4.2.5 on 2023-12-16 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsgatherers', '0006_alter_news_cluster_head_created_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news_obj',
            name='is_cluster_head',
        ),
        migrations.RemoveField(
            model_name='news_obj',
            name='is_clustered',
        ),
        migrations.AlterField(
            model_name='news_cluster_head',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 13, 19, 2, 675628, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='news_obj',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 13, 19, 2, 677284, tzinfo=datetime.timezone.utc)),
        ),
    ]
