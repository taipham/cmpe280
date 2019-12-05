# Generated by Django 2.2.5 on 2019-12-05 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_auto_20191201_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='language',
            new_name='mylanguage',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='mysport1',
            new_name='mysport',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='mysport2',
        ),
        migrations.CreateModel(
            name='NewProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mysport', models.CharField(max_length=100)),
                ('myteam', models.CharField(max_length=100)),
                ('mylanguage', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
