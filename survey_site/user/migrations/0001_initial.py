# Generated by Django 3.0.5 on 2020-04-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_id', models.UUIDField(verbose_name='할당 아이디')),
                ('finished_code', models.CharField(default='0', max_length=32, verbose_name='Finished_code')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'user',
            },
        ),
    ]
