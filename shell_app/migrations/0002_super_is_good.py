# Generated by Django 2.2.4 on 2021-04-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shell_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='super',
            name='is_good',
            field=models.BooleanField(default=1, verbose_name=True),
            preserve_default=False,
        ),
    ]
