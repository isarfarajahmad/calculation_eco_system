# Generated by Django 3.0.4 on 2020-09-01 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0004_auto_20200901_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric2',
            name='metric',
            field=models.CharField(default='1.2.1', editable=False, max_length=100, null=True),
        ),
    ]