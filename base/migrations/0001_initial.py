# Generated by Django 4.1.1 on 2022-09-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('ex_title', models.CharField(max_length=60)),
                ('ex_load', models.CharField(max_length=20)),
                ('ex_reps', models.CharField(max_length=20)),
            ],
        ),
    ]
