# Generated by Django 3.2.9 on 2021-12-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_url', models.URLField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.PositiveSmallIntegerField()),
                ('title', models.CharField(max_length=256)),
                ('photo_url', models.URLField()),
                ('transaction_number', models.CharField(max_length=12)),
            ],
        ),
    ]