# Generated by Django 3.0.4 on 2020-09-01 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0003_metric5_metric6'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric2',
            name='metric',
            field=models.CharField(max_length=100),
        ),
    ]