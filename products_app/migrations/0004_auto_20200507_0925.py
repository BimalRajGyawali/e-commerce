# Generated by Django 3.0.5 on 2020-05-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0003_auto_20200507_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetails',
            name='expiry_date',
            field=models.CharField(max_length=100),
        ),
    ]
