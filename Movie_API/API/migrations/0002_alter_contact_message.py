# Generated by Django 4.1.7 on 2023-08-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("API", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="Message",
            field=models.CharField(max_length=200),
        ),
    ]
