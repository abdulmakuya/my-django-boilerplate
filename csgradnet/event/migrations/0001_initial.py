# Generated by Django 2.2a1 on 2019-02-11 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Description', models.TextField(max_length=500, null=True)),
                ('eventDate', models.DateTimeField(max_length=50, null=True)),
                ('eventVenue', models.CharField(max_length=50, null=True)),
                ('eventFee', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
