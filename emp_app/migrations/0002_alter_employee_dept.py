# Generated by Django 4.2 on 2023-06-06 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.department'),
        ),
    ]
