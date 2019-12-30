# Generated by Django 2.2 on 2019-06-12 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('nid', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=1)),
                ('birthday', models.CharField(max_length=20)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activitys', to='chart.Activity')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='chart.ActivityTag'),
        ),
    ]