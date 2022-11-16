# Generated by Django 4.1.3 on 2022-11-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_registerpersonmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fingerprintprofilemodel',
            name='dt',
        ),
        migrations.RemoveField(
            model_name='fingerprintprofilemodel',
            name='ldt',
        ),
        migrations.RemoveField(
            model_name='fingerprintprofilemodel',
            name='lstatus',
        ),
        migrations.RemoveField(
            model_name='fingerprintprofilemodel',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='fingerprintprofilemodel',
            name='status',
        ),
        migrations.AddField(
            model_name='fingerprintprofilemodel',
            name='checkinstatus',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='fingerprintprofilemodel',
            name='checkintime',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='fingerprintprofilemodel',
            name='checkouttime',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='fingerprintprofilemodel',
            name='currentdate',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='fingerprintprofilemodel',
            name='exitstatus',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='fingerprintprofilemodel',
            name='fpid',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='fingerprintprofilemodel',
            name='username',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
