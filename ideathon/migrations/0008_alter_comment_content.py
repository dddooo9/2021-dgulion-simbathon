# Generated by Django 3.2.3 on 2021-05-21 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideathon', '0007_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='content'),
        ),
    ]
