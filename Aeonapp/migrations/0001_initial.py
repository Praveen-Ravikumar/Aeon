# Generated by Django 5.0.6 on 2024-06-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopDetail',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=800)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
