# Generated by Django 4.2.5 on 2023-12-16 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsgatherers', '0007_remove_news_obj_is_cluster_head_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_cluster_head',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 15, 28, 5, 236752, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='news_obj',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 15, 28, 5, 238521, tzinfo=datetime.timezone.utc)),
        ),
    ]