# Generated by Django 4.2.5 on 2023-12-08 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsgatherers', '0009_merge_0004_url_0008_merge_20231027_1839'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='youtube_csv_data',
            new_name='youtube_data',
        ),
    ]
