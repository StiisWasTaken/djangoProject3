# Generated by Django 3.2 on 2021-05-09 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_title_post_titles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('type', models.TextField()),
                ('weight', models.FloatField()),
                ('production_year', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('wheel_size', models.FloatField()),
            ],
        ),
    ]
