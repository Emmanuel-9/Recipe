# Generated by Django 4.0.1 on 2022-01-21 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]