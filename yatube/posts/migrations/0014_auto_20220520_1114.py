# Generated by Django 2.2.16 on 2022-05-20 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20220520_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='pub_date',
        ),
    ]
