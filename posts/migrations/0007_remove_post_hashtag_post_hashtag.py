# Generated by Django 4.1.3 on 2022-11-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_hashtag_post_hashtag'),
    ]

    operations = [
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
