# Generated by Django 3.0.3 on 2020-02-19 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='web_site',
        ),
        migrations.AddField(
            model_name='buyer',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='company',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='specifications',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='seller',
            name='distressed',
            field=models.CharField(default='', max_length=200),
        ),
    ]
