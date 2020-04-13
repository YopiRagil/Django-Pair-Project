# Generated by Django 3.0.5 on 2020-04-13 01:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dribbble_app', '0006_auto_20200413_0148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='design',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 4, 13, 1, 49, 23, 108612, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 4, 13, 1, 49, 23, 107734, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 13, 1, 49, 23, 80164, tzinfo=utc)),
        ),
    ]