# Generated by Django 4.0.2 on 2022-02-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django2', '0003_alter_job_comments_alter_tool_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='scheduled',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='suggested_tools',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
