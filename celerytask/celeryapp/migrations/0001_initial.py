# Generated by Django 4.1.2 on 2022-10-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=150)),
                ('count', models.IntegerField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
