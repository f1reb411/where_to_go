# Generated by Django 3.0.14 on 2022-02-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description_short', models.TextField(blank=True)),
                ('description_long', models.TextField(blank=True)),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
    ]
