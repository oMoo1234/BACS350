# Generated by Django 3.2.6 on 2021-10-04 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='identity',
            field=models.TextField(default='hi', max_length=100),
        ),
    ]
