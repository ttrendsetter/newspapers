# Generated by Django 4.1 on 2022-08-22 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article__date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='_date',
            new_name='date',
        ),
    ]