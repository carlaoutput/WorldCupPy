# Generated by Django 2.0.7 on 2018-07-08 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('startTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Scored',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leftScore', models.IntegerField(default=0)),
                ('rightScore', models.IntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldcup.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('teamName', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('isEliminated', models.BooleanField(default=False)),
                ('totalGoals', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='LeftTeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leftteam', to='worldcup.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='RightTeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rightteam', to='worldcup.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='scored',
            unique_together={('match',)},
        ),
        migrations.AlterUniqueTogether(
            name='match',
            unique_together={('RightTeam', 'LeftTeam', 'date')},
        ),
    ]
