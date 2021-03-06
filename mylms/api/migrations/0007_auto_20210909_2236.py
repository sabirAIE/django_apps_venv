# Generated by Django 3.2.6 on 2021-09-09 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_singermodel_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='singermodel',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='songmodel',
            name='singer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='song', to='api.singermodel'),
        ),
    ]
