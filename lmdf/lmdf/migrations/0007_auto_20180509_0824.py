# Generated by Django 2.0.4 on 2018-05-09 08:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lmdf', '0006_auto_20180503_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='patient',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
