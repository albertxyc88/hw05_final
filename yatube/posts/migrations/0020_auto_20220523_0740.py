# Generated by Django 2.2.16 on 2022-05-23 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20220523_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(help_text='Комментарий к посту', max_length=200, verbose_name='Комментарий'),
        ),
    ]
