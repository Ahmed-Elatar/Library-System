# Generated by Django 3.2.7 on 2021-10-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_books_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='whoborrowed',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]