# Generated by Django 3.2.9 on 2021-11-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cazzo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cazzo',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
