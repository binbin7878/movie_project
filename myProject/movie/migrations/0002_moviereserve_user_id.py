# Generated by Django 4.2.7 on 2023-11-25 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviereserve',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movie.profile'),
        ),
    ]
