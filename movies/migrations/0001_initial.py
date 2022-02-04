# Generated by Django 4.0.2 on 2022-02-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0003_genre_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('types', models.CharField(choices=[('director', 'Director'), ('writer', 'Writer'), ('actor', 'Actor')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=5000)),
                ('release_year', models.IntegerField()),
                ('mpa_rating', models.CharField(choices=[('G', 'G'), ('PG', 'Pg'), ('PG-13', 'Pg13'), ('R', 'R'), ('NC-17', 'Nc17')], max_length=5)),
                ('imdb_rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('duration', models.IntegerField()),
                ('genres', models.ManyToManyField(to='genres.Genre')),
            ],
        ),
    ]