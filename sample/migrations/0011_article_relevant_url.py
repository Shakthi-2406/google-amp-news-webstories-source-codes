# Generated by Django 4.0 on 2022-02-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0010_article_slug_alter_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='relevant_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]