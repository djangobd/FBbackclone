# Generated by Django 2.0.6 on 2018-07-01 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FacebookBackend', '0004_auto_20180701_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]