# Generated by Django 4.0.3 on 2022-03-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main', 'tag__name'], 'verbose_name': 'Сфера', 'verbose_name_plural': 'Сферы'},
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', through='articles.Scope', to='articles.tag'),
        ),
    ]
