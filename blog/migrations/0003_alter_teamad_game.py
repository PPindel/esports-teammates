# Generated by Django 3.2.18 on 2023-03-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230320_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamad',
            name='game',
            field=models.CharField(choices=[('LOL', 'League of Legends'), ('WOW', 'World of Warcraft'), ('DOTA2', 'Defense of the Ancients 2'), ('DIA4', 'Diablo 4'), ('POE', 'Path of Exile'), ('OW2', 'Overwatch 2'), ('SMITE', 'Smite'), ('DAD', 'Dark and Darker')], default='LOL', max_length=5),
        ),
    ]
