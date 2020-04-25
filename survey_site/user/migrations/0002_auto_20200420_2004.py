# Generated by Django 3.0.5 on 2020-04-20 20:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='assigned_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='할당 아이디'),
        ),
    ]