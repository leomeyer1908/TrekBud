# Generated by Django 3.2.7 on 2023-10-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='budget_constraints',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dietary_restrictions',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='emergency_contact',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='notification_preferences',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='preferred_airlines',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='preferred_travel_dates',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_privacy',
            field=models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default='public', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='travel_style_preferences',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='trip_duration',
            field=models.IntegerField(null=True),
        ),
    ]
