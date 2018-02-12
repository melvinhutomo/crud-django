# Generated by Django 2.0 on 2018-02-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('date_published', models.DateField(null=True)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('book_type', models.PositiveSmallIntegerField(choices=[(1, 'Novel'), (2, 'Documentation'), (3, 'Other')])),
            ],
        ),
    ]
