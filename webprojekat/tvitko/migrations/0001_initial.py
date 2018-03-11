# Generated by Django 2.0.1 on 2018-01-23 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=140)),
                ('created_at', models.DateField()),
                ('is_retweet', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Veznatabela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tvitko.Hashtag')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tvitko.Tweet')),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='hashtags',
            field=models.ManyToManyField(through='tvitko.Veznatabela', to='tvitko.Hashtag'),
        ),
    ]
