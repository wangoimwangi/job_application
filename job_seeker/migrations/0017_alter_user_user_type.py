# Generated by Django 4.1 on 2022-11-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_seeker', '0016_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('staff', 'staff'), ('staff', 'applicant')], max_length=20),
        ),
    ]
