# Generated by Django 4.1.1 on 2022-10-08 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200, null=True)),
                ('price', models.PositiveIntegerField(default=1000)),
                ('band', models.CharField(choices=[('4G', '4G'), ('5G', '5G'), ('3G', '3G')], default='4G', max_length=200)),
                ('display', models.CharField(choices=[('LED', 'LED'), ('AMOLED', 'AMOLED'), ('SMOLED', 'SMOLED')], default='LED', max_length=200)),
            ],
        ),
    ]
