# Generated by Django 4.2 on 2023-05-28 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_comment_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
