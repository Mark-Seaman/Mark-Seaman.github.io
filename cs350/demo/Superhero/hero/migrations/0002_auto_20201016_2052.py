# Generated by Django 3.1.2 on 2020-10-16 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
