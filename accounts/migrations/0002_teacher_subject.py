# Generated by Django 4.1 on 2022-08-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
