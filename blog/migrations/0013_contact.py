# Generated by Django 3.0.5 on 2020-06-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_commentsposts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=250)),
                ('lName', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('Tel', models.CharField(max_length=15)),
                ('Message', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
