# Generated by Django 4.0.1 on 2022-10-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addfood',
            name='carbs',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='addfood',
            name='fats',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='addfood',
            name='protein',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20),
        ),
    ]