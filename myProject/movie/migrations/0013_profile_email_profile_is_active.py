# Generated by Django 4.2.7 on 2023-12-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_remove_profile_email_remove_profile_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
