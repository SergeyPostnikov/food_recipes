# Generated by Django 4.2.5 on 2023-09-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='preferences', to='recipes.category'),
        ),
    ]