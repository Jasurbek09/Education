# Generated by Django 3.2.8 on 2021-10-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Siteuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('middle_name', models.CharField(blank=True, max_length=200)),
                ('iin', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('password', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
