# Generated by Django 3.1.1 on 2022-12-26 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMP_ID', models.CharField(help_text='reference number', max_length=20)),
                ('ENAME', models.CharField(max_length=100)),
                ('POST', models.CharField(max_length=100)),
                ('SALARY', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]