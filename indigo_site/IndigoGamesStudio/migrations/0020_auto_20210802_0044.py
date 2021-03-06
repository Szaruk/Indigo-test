# Generated by Django 3.2.4 on 2021-08-01 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndigoGamesStudio', '0019_auto_20210802_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='social_icon_first',
            field=models.CharField(choices=[('icon-linkedin-squared', 'icon-linkedin-squared'), ('icon-github-circled-alt2', 'icon-github-circled-alt2'), ('https://img.icons8.com/ios/50/000000/sketchfab.png', 'https://img.icons8.com/ios/50/000000/sketchfab.png'), ('https://img.icons8.com/windows/32/000000/artstation.png', 'https://img.icons8.com/windows/32/000000/artstation.png')], default='icon-linkedin-squared', max_length=255),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='social_icon_fourth',
            field=models.CharField(blank=True, choices=[('icon-linkedin-squared', 'icon-linkedin-squared'), ('icon-github-circled-alt2', 'icon-github-circled-alt2'), ('https://img.icons8.com/ios/50/000000/sketchfab.png', 'https://img.icons8.com/ios/50/000000/sketchfab.png'), ('https://img.icons8.com/windows/32/000000/artstation.png', 'https://img.icons8.com/windows/32/000000/artstation.png')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='social_icon_second',
            field=models.CharField(blank=True, choices=[('icon-linkedin-squared', 'icon-linkedin-squared'), ('icon-github-circled-alt2', 'icon-github-circled-alt2'), ('https://img.icons8.com/ios/50/000000/sketchfab.png', 'https://img.icons8.com/ios/50/000000/sketchfab.png'), ('https://img.icons8.com/windows/32/000000/artstation.png', 'https://img.icons8.com/windows/32/000000/artstation.png')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='social_icon_third',
            field=models.CharField(blank=True, choices=[('icon-linkedin-squared', 'icon-linkedin-squared'), ('icon-github-circled-alt2', 'icon-github-circled-alt2'), ('https://img.icons8.com/ios/50/000000/sketchfab.png', 'https://img.icons8.com/ios/50/000000/sketchfab.png'), ('https://img.icons8.com/windows/32/000000/artstation.png', 'https://img.icons8.com/windows/32/000000/artstation.png')], max_length=255, null=True),
        ),
    ]
