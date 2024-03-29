# Generated by Django 3.0.4 on 2020-09-10 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maths', '0006_auto_20200910_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric2',
            name='metric',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metric5',
            name='metric',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metric6',
            name='metric',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('metric', models.CharField(max_length=100, null=True)),
                ('subject1', models.IntegerField(null=True)),
                ('subject2', models.IntegerField(null=True)),
                ('value', models.FloatField(max_length=1000, null=True)),
                ('file', models.FileField(null=True, upload_to='upload/files')),
                ('remarks', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
