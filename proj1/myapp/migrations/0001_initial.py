# Generated by Django 3.2.12 on 2023-07-28 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=30)),
                ('bauthor', models.CharField(max_length=30)),
            ],
        ),
    ]
