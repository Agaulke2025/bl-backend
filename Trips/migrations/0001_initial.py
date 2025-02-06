# Generated by Django 5.1.5 on 2025-02-06 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('groupCheckIn', models.TextField()),
                ('forecast', models.TextField()),
                ('avyProblems', models.TextField()),
                ('advisory', models.TextField()),
                ('conditions', models.TextField()),
                ('review', models.TextField()),
                ('observations', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
        ),
    ]
