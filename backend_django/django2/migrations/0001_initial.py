# Generated by Django 4.0.2 on 2022-02-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=3)),
                ('key', models.CharField(max_length=10)),
                ('drivers', models.CharField(max_length=50)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('notes', models.TextField()),
                ('truck', models.ManyToManyField(blank=True, related_name='tools', to='django2.Truck')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggested_tools', models.CharField(max_length=1000)),
                ('address', models.TextField()),
                ('scheduled', models.TextField()),
                ('comments', models.TextField()),
                ('truck', models.ManyToManyField(blank=True, related_name='jobs', to='django2.Truck')),
            ],
        ),
    ]
