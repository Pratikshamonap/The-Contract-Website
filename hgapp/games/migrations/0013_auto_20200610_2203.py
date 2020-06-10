# Generated by Django 2.2.12 on 2020-06-10 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0012_game_attendance_is_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('SCHEDULED', 'Scheduled'), ('ACTIVE', 'Active'), ('FINISHED', 'Finished'), ('ARCHIVED', 'Archived'), ('CANCELED', 'Canceled'), ('VOID', 'Void'), ('RECORDED', 'Archived')], default=('SCHEDULED', 'Scheduled'), max_length=25),
        ),
        migrations.AlterField(
            model_name='game_attendance',
            name='outcome',
            field=models.CharField(blank=True, choices=[('WIN', 'Victory'), ('LOSS', 'Loss'), ('DEATH', 'Died'), ('DECLINED', 'Declined Harbinger Invite'), ('RINGER_VICTORY', 'Ringer Victory'), ('RINGER_FAILURE', 'Ringer Failure')], max_length=20, null=True),
        ),
    ]