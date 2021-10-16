# Generated by Django 3.2.7 on 2021-10-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nid', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
