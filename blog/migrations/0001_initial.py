# Generated by Django 5.1.1 on 2024-09-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Статья блога',
                'verbose_name_plural': 'Статьи блога',
            },
        ),
    ]
