# Generated by Django 4.2.5 on 2023-12-17 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0003_dailyocr_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyocr',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]