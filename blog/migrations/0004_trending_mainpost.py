# Generated by Django 3.0.5 on 2020-06-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_trending'),
    ]

    operations = [
        migrations.AddField(
            model_name='trending',
            name='mainpost',
            field=models.BooleanField(default=False),
        ),
    ]