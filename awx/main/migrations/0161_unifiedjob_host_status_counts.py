# Generated by Django 3.2.12 on 2022-04-27 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0160_alter_schedule_rrule'),
    ]

    operations = [
        migrations.AddField(
            model_name='unifiedjob',
            name='host_status_counts',
            field=models.JSONField(blank=True, default=None, editable=False, help_text='Playbook stats from the Ansible playbook_on_stats event.', null=True),
        ),
    ]