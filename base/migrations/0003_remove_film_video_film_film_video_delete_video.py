# Generated by Django 4.1.3 on 2022-12-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_video_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='video_film',
        ),
        migrations.AddField(
            model_name='film',
            name='video',
            field=models.FileField(default=1, upload_to='videos/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
