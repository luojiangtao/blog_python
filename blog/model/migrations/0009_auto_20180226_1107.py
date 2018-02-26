# Generated by Django 2.0.2 on 2018-02-26 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0008_auto_20180226_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=32, verbose_name='username,haha')),
                ('password', models.CharField(default='aaa', max_length=32)),
            ],
            options={
                'db_table': 'admin2',
            },
        ),
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(default='aaa', max_length=32),
        ),
        migrations.AlterField(
            model_name='admin',
            name='username',
            field=models.CharField(blank=True, max_length=32, verbose_name='username,haha'),
        ),
    ]
