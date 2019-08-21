# Generated by Django 2.2.1 on 2019-08-21 21:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='away_goals',
            new_name='league_id',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='home_goals',
            new_name='match_awayteam_id',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='date',
            new_name='match_date',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team',
        ),
        migrations.RemoveField(
            model_name='match',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
        migrations.AddField(
            model_name='match',
            name='match_awayteam_name',
            field=models.CharField(default=django.utils.timezone.now, help_text='Away Team Name', max_length=50, verbose_name='Team Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='match_awayteam_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='match_hometeam_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='match_hometeam_name',
            field=models.CharField(default=django.utils.timezone.now, help_text='Home Team Name', max_length=50, verbose_name='Team Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='match_hometeam_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='match_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='team_key',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='team_name',
            field=models.CharField(default=django.utils.timezone.now, help_text='Team Name', max_length=50, verbose_name='Team Name'),
            preserve_default=False,
        ),
    ]
