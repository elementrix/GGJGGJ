# Generated by Django 2.1.1 on 2020-10-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201005_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postCover',
            field=models.ImageField(null=True, upload_to='images/postCover/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postCover2',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
