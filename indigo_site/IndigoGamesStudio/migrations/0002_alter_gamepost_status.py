# Generated by Django 3.2.4 on 2021-06-22 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndigoGamesStudio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamepost',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=25),
        ),
    ]
