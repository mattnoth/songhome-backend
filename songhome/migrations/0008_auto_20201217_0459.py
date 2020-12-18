# Generated by Django 3.1.4 on 2020-12-17 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songhome', '0007_auto_20201217_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(default='media/audio/default.mp3', upload_to='media/audio/'),
        ),
    ]