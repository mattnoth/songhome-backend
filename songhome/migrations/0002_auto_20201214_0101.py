# Generated by Django 3.1.4 on 2020-12-14 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songhome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='isrc_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='lyrics',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='pub_percent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
