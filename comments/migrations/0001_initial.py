# Generated by Django 3.2.7 on 2021-11-09 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='books.book')),
                ('comment', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comments',
                'managed': False,
            },
        ),
    ]
