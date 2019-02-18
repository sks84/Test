# Generated by Django 2.0 on 2019-02-10 05:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bridge', '0048_auto_20190210_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertEnq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='addlecture',
            name='update_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 10, 11, 12, 31, 169246)),
        ),
        migrations.AlterField(
            model_name='expert',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='expertenq',
            name='expert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bridge.Expert'),
        ),
        migrations.AddField(
            model_name='expertenq',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bridge.Student'),
        ),
    ]
