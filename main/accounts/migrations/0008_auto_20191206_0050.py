# Generated by Django 2.2.5 on 2019-12-06 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20191205_0745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='myage',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='mygender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='mylanguage',
            new_name='Language',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='myname',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='mysport',
            new_name='Sport',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='myteam',
            new_name='Team',
        ),
    ]
