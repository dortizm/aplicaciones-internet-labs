# Generated by Django 3.2.3 on 2023-09-13 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='almuno',
            name='asingaturas',
            field=models.ManyToManyField(to='course_management.asingatura'),
        ),
    ]