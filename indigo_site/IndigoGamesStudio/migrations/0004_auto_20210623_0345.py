# Generated by Django 3.2.4 on 2021-06-23 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndigoGamesStudio', '0003_gamepost_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamepost',
            name='icon',
            field=models.CharField(choices=[('icon-windows', 'icon-windows'), ('icon-android', 'icon-android')], default='icon-android', max_length=15),
        ),
        migrations.AlterField(
            model_name='gamepost',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]
