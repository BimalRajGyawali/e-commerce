# Generated by Django 3.0.5 on 2020-05-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0002_auto_20200507_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetails',
            name='expiry_date',
            field=models.DateField(),
        ),
    ]