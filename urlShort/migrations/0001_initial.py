# Generated by Django 5.0.3 on 2024-03-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField()),
                ('short_url', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
