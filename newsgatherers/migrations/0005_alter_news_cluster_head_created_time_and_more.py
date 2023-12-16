# Generated by Django 4.2.5 on 2023-12-16 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsgatherers', '0004_alter_news_cluster_head_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_cluster_head',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 11, 39, 13, 114168, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='news_obj',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 11, 39, 13, 118001, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='news_obj',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
