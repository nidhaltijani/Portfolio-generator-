# Generated by Django 4.1.2 on 2022-12-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]