# Generated by Django 4.1.3 on 2022-11-26 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_rename_discription_post_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='discription',
        ),
        migrations.RemoveField(
            model_name='post',
            name='hashtag',
        ),
        migrations.AddField(
            model_name='post',
            name='hashtag',
            field=models.ManyToManyField(null=True, related_name='posts', to='posts.hashtag'),
        ),
    ]