# Generated by Django 4.1 on 2022-09-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField()),
                ('title', models.TextField()),
                ('rating', models.IntegerField()),
                ('release_date', models.DateField()),
                ('review', models.TextField()),
            ],
        ),
    ]
