# Generated by Django 5.0.6 on 2024-05-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_event_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='manager',
            field=models.CharField(blank=True, max_length=63, null=True, verbose_name=''),
        ),
    ]
