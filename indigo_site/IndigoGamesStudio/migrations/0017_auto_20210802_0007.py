# Generated by Django 3.2.4 on 2021-08-01 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndigoGamesStudio', '0016_auto_20210802_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='social_icon_first_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='social_icon_second_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='social_icon_third_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='social_media_first_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='social_media_second_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
