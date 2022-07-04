# Generated by Django 3.2.7 on 2022-04-19 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_needy_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaderboard',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='solved_cases',
            name='solved_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.RemoveField(
            model_name='forms',
            name='needy_id',
        ),
        migrations.AddField(
            model_name='forms',
            name='needy_id',
            field=models.ManyToManyField(to='account.Needy'),
        ),
        migrations.RemoveField(
            model_name='forms',
            name='user_id',
        ),
        migrations.AddField(
            model_name='forms',
            name='user_id',
            field=models.ManyToManyField(to='account.People'),
        ),
        migrations.RemoveField(
            model_name='leaderboard',
            name='user_id',
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='user_id',
            field=models.ManyToManyField(to='account.People'),
        ),
        migrations.RemoveField(
            model_name='solved_cases',
            name='needy_id',
        ),
        migrations.AddField(
            model_name='solved_cases',
            name='needy_id',
            field=models.ManyToManyField(to='account.Needy'),
        ),
        migrations.RemoveField(
            model_name='solved_cases',
            name='ngo_id',
        ),
        migrations.AddField(
            model_name='solved_cases',
            name='ngo_id',
            field=models.ManyToManyField(to='account.Ngo'),
        ),
        migrations.RemoveField(
            model_name='solved_cases',
            name='user_id',
        ),
        migrations.AddField(
            model_name='solved_cases',
            name='user_id',
            field=models.ManyToManyField(to='account.People'),
        ),
    ]