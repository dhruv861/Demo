# Generated by Django 4.1.4 on 2022-12-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('emp_id', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('working', models.BooleanField()),
                ('department', models.CharField(max_length=20)),
            ],
        ),
    ]
