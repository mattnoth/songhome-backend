# Generated by Django 3.1.4 on 2020-12-17 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songhome', '0006_auto_20201214_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(default='media/images/default.jpg', upload_to='media/images/'),
        ),
    ]
