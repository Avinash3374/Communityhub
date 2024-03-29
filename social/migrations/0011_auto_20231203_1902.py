# Generated by Django 3.1.7 on 2023-12-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_notification_thread'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/post_photos')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ManyToManyField(blank=True, to='social.Image'),
        ),
    ]
