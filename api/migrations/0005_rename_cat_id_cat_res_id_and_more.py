# Generated by Django 4.0.2 on 2022-03-09 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_iteams_res'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat_res',
            old_name='cat_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='cat_res',
            old_name='res',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='iteams',
            old_name='cat',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='iteams',
            old_name='iteam_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='iteams',
            old_name='res',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='Res_id',
            new_name='id',
        ),
    ]
