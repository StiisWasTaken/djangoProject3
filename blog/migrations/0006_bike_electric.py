# Generated by Django 3.2 on 2021-05-09 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_bike'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='electric',
            field=models.BooleanField(default=False),
        ),
    ]