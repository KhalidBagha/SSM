# Generated by Django 4.1.7 on 2023-03-26 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebook_pages',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='facebook_pages',
            name='audience',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='facebook_pages',
            name='category',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='facebook_pages',
            name='email',
            field=models.EmailField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='facebook_pages',
            name='keyword',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='facebook_pages',
            name='link',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='facebook_pages',
            name='location',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='facebook_pages',
            name='phone',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='facebook_pages',
            name='rating',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='facebook_pages',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='facebook_pages',
            name='website',
            field=models.URLField(max_length=250, null=True),
        ),
    ]