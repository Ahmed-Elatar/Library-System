# Generated by Django 3.2.7 on 2021-10-06 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=200)),
                ('cat', models.CharField(max_length=20)),
            ],
        ),
    ]
