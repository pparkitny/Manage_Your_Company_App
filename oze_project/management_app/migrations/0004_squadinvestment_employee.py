# Generated by Django 3.2.9 on 2021-12-12 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0003_dayname'),
    ]

    operations = [
        migrations.AddField(
            model_name='squadinvestment',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management_app.employee'),
        ),
    ]
