# Generated by Django 3.2.7 on 2021-10-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_books_bookuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bookuser',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
    ]
