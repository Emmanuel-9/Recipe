# Generated by Django 4.0.1 on 2022-01-21 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
