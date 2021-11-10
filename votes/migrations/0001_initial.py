# Generated by Django 3.1.7 on 2021-03-07 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivatePoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('password', models.CharField(max_length=20, unique=True)),
                ('time_duration', models.DateTimeField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrivatePollOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('privatepoll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.privatepoll')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublicPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('time_duration', models.DateTimeField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublicPollOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('publicpoll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.publicpoll')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublicPollResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.BooleanField(default=True)),
                ('publicpoll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.publicpoll')),
                ('publicpoll_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.publicpolloption')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrivatePollResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.BooleanField(default=True)),
                ('privatepoll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.privatepoll')),
                ('privatepoll_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.privatepolloption')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]