# Generated by Django 3.1.3 on 2020-11-12 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historymodel',
            name='pageID',
        ),
    ]
