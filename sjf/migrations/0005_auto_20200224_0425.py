# Generated by Django 3.0.3 on 2020-02-24 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjf', '0004_auto_20200220_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='img_url',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]