# Generated by Django 5.0.2 on 2024-03-17 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GOMA', '0006_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='contenido',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_at',
            new_name='fecha_actualizacion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='fecha_creacion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='imagen',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
