# Generated by Django 3.1.5 on 2021-02-07 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('emp_name', models.CharField(max_length=100)),
                ('vac_start', models.DateField()),
                ('vac_end', models.DateField()),
                ('no_of_days', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='Pending', max_length=20)),
            ],
        ),
    ]
