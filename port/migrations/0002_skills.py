# Generated by Django 3.0.6 on 2022-04-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='profile/')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]