# Generated by Django 3.2.15 on 2022-08-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='url_hash',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tip',
            name='tags',
            field=models.ManyToManyField(related_name='tip_tags', to='blog.Tag'),
        ),
    ]
