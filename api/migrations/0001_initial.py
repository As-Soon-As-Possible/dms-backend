# Generated by Django 3.2.9 on 2021-11-24 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=19)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=19)),
                ('max_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=19)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=19)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('additional_info', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('qualification', models.CharField(max_length=100)),
            ],
        ),
    ]