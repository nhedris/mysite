# Generated by Django 3.2.20 on 2023-11-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_contct_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]