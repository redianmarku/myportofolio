# Generated by Django 3.0.3 on 2020-03-02 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portofolio',
            name='url',
            field=models.URLField(default='https://redianmarku.herokuapp.com'),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
