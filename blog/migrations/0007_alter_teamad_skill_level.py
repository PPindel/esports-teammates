# Generated by Django 3.2.18 on 2023-05-13 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230512_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamad',
            name='skill_level',
            field=models.CharField(choices=[('Any', 'Any'), ('New player', 'New player'), ('Advanced player', 'Advanced player'), ('Expert player', 'Expert player'), ('Proffessional player', 'Proffessional player')], default='Any', max_length=25),
        ),
    ]
