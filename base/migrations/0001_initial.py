# Generated by Django 4.0.1 on 2022-05-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_food', models.CharField(max_length=200)),
                ('calorie', models.IntegerField()),
            ],
        ),
    ]
