# Generated by Django 3.0.5 on 2020-06-04 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='editorspick',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
