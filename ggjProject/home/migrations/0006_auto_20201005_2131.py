# Generated by Django 3.1 on 2020-10-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_post_postcover2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postCover',
            field=models.ImageField(blank=True, null=True, upload_to='images/postCover/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postCover2',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
