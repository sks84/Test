# Generated by Django 2.0 on 2019-01-27 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge', '0029_expertreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communication_skill', models.IntegerField()),
                ('domain_knowledge', models.IntegerField()),
                ('team_skill', models.IntegerField()),
                ('open_for_learning', models.IntegerField()),
                ('behaviour', models.IntegerField()),
            ],
        ),
    ]
