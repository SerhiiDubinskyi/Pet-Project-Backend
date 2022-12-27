# Generated by Django 4.1.3 on 2022-12-27 21:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('age', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(250)])),
                ('photo', models.URLField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('telegram', models.CharField(max_length=30)),
                ('facebook', models.CharField(max_length=30)),
                ('instagram', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=1000)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['created_at', 'name'],
            },
        ),
        migrations.CreateModel(
            name='PetProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('age', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(250)])),
                ('photo', models.URLField(null=True)),
                ('color', models.CharField(max_length=50)),
                ('size', models.PositiveSmallIntegerField()),
                ('description', models.TextField(blank=True, max_length=2000)),
                ('is_vaccinated', models.BooleanField(default=False)),
                ('is_sterilized', models.BooleanField(default=False)),
                ('is_microchipped', models.BooleanField(default=False)),
                ('is_house_trained', models.BooleanField(default=False)),
                ('is_good_with_other_animals', models.BooleanField(default=False)),
                ('is_good_with_strangers', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petfinder.userprofile')),
            ],
            options={
                'verbose_name': 'Профиль питомца',
                'verbose_name_plural': 'Профили Питомцев',
                'ordering': ['-created_at', 'updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lost_date', models.DateTimeField()),
                ('lost_location', models.CharField(max_length=100)),
                ('found_date', models.DateField(null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('found_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='petfinder.userprofile')),
                ('lost_pet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='petfinder.petprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
