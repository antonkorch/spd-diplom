# Generated by Django 4.2.7 on 2024-03-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postimage_remove_post_images_post_image_delete_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
