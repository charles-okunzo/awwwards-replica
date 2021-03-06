# Generated by Django 4.0.5 on 2022-06-12 18:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards_app', '0002_project_date_posted_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='awwwards_app.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
