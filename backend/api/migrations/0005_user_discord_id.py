# Generated by Django 3.0.2 on 2020-01-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200112_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='discord_id',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]
