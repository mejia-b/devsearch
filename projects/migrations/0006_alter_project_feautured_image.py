# Generated by Django 3.2.6 on 2022-01-04 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_feautured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='feautured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
