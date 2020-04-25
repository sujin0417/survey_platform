# Generated by Django 3.0.5 on 2020-04-14 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='답')),
                ('ans_valid', models.IntegerField(verbose_name='사용가능 여부')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem', verbose_name='문제')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='사용자')),
            ],
            options={
                'verbose_name': '답변',
                'verbose_name_plural': '답변',
                'db_table': 'answer',
            },
        ),
    ]
