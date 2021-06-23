# Generated by Django 3.1.2 on 2021-04-06 16:34

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=40, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('cost', models.IntegerField(verbose_name='Cost')),
                ('funded', models.IntegerField(default=100, verbose_name='Funded')),
                ('days_left', models.IntegerField(verbose_name='Days left')),
                ('is_new', models.BooleanField(default=True, verbose_name='Is new')),
            ],
        ),
    ]