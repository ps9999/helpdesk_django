# Generated by Django 2.2.10 on 2021-05-29 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='TicketCategory',
        ),
        migrations.RenameModel(
            old_name='Priority',
            new_name='TicketPriority',
        ),
    ]