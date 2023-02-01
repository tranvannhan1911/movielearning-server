# Generated by Django 4.0.8 on 2023-01-16 16:59

import bson.objectid
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core_movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='link_mp4',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='translate',
            name='id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default=bson.objectid.ObjectId, primary_key=True, serialize=False),
        ),
    ]