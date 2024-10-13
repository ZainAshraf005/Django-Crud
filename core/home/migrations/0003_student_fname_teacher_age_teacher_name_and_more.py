# Generated by Django 5.1.1 on 2024-09-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fname',
            field=models.CharField(default='fname', max_length=200),
        ),
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name='teacher',
            name='name',
            field=models.CharField(default='name is not given', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
