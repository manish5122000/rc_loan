# Generated by Django 3.1.7 on 2021-05-11 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=30)),
                ('Pin_code', models.PositiveIntegerField()),
                ('Work_Type', models.CharField(choices=[('Student', 'Student'), ('Driver', 'Driver'), ('Employee', 'Employee'), ('Shop owner', 'Shop owner'), ('Delivery boy', 'Delivery boy'), ('Other', 'Other')], max_length=20)),
                ('Address_Type', models.CharField(choices=[('Home with Family', 'Home with Family'), ('Rented with Family', 'Rented with Family'), ('Rented with Friends', 'Rented with Friends'), ('Hostel/PG', 'Hostel/PG')], max_length=50)),
                ('Aadhar_Card_Number', models.PositiveBigIntegerField()),
                ('Pan_Card_Number', models.CharField(max_length=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_info_Admin',
            fields=[
                ('personal_information_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='customer.personal_information')),
            ],
            bases=('customer.personal_information',),
        ),
    ]
