# Generated by Django 4.1.4 on 2022-12-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_ticket_delete_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='author',
            field=models.CharField(default='John Smith', max_length=80),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='comment',
            field=models.CharField(default='Lorem Ipsum', max_length=5000),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(default='Low', max_length=6),
        ),
    ]
