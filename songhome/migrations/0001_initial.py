# Generated by Django 3.1.4 on 2020-12-14 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('file', models.FileField(default='default.mp3', upload_to='audio/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('release_date', models.DateField(null=True)),
                ('isrc_code', models.IntegerField(blank=True)),
                ('lyrics', models.CharField(blank=True, max_length=5000)),
                ('bpm', models.SmallIntegerField(blank=True)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('key', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pub_percent', models.IntegerField(blank=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writers', to='songhome.song')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='songhome.song')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='songhome.song')),
            ],
        ),
    ]
