# Generated by Django 3.2.15 on 2022-08-12 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20220812_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tip',
            name='code',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='tip',
            name='description',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='tip',
            name='heading',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='tip',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tip_tags', to='blog.Tag'),
        ),
    ]
