# Generated by Django 3.1.7 on 2021-05-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminss', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='category',
            field=models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Agent', 'Agent'), ('Customer', 'Customer')], default='Customer', max_length=15, null=True),
        ),
    ]