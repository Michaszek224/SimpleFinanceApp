# Generated by Django 4.2.4 on 2023-10-18 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financeApp', '0002_delete_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='money',
            old_name='lastIncome',
            new_name='lastTransaction',
        ),
        migrations.RemoveField(
            model_name='money',
            name='lastOutcome',
        ),
    ]