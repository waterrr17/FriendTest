# Generated by Django 2.0.13 on 2020-08-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='current_guess',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='question1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='question10',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='question2',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='question3',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='question4',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='question5',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='question6',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='question7',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='question8',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='question9',
            field=models.BooleanField(default=False),
        ),
    ]
