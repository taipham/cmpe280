# Generated by Django 2.2.5 on 2019-12-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191205_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='myage',
            field=models.CharField(default='30', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='mygender',
            field=models.CharField(default='Male', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='myname',
            field=models.CharField(default='Test', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NewProfile',
        ),
    ]
