# Generated by Django 2.2.12 on 2020-06-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0016_auto_20200616_1555'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Merit',
            new_name='Asset',
        ),
        migrations.RenameModel(
            old_name='MeritDetails',
            new_name='AssetDetails',
        ),
        migrations.RenameModel(
            old_name='Flaw',
            new_name='Liability',
        ),
        migrations.RenameModel(
            old_name='FlawDetails',
            new_name='LiabilityDetails',
        ),
        migrations.RenameField(
            model_name='assetdetails',
            old_name='relevant_merit',
            new_name='relevant_asset',
        ),
        migrations.RenameField(
            model_name='liabilitydetails',
            old_name='relevant_flaw',
            new_name='relevant_liability',
        ),
        migrations.RemoveField(
            model_name='contractstats',
            name='flaws',
        ),
        migrations.RemoveField(
            model_name='contractstats',
            name='merits',
        ),
        migrations.AddField(
            model_name='contractstats',
            name='assets',
            field=models.ManyToManyField(blank=True, through='characters.AssetDetails', to='characters.Asset'),
        ),
        migrations.AddField(
            model_name='contractstats',
            name='liabilities',
            field=models.ManyToManyField(blank=True, through='characters.LiabilityDetails', to='characters.Liability'),
        ),
    ]