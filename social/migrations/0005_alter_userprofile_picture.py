# Generated by Django 4.1.1 on 2022-10-19 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='uploads/profile_picture/default.png', upload_to='uploads/profile_picture'),
        ),
    ]
