# Generated by Django 2.2.2 on 2022-09-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20220919_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_tittle', models.CharField(default='list - tittle', max_length=500)),
                ('display_image', models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d/')),
                ('product_price', models.CharField(default='0', max_length=500)),
            ],
        ),
    ]
