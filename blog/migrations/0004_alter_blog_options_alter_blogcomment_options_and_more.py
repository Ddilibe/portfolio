# Generated by Django 4.2.4 on 2023-08-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_alter_blogcomment_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"ordering": ["title"]},
        ),
        migrations.AlterModelOptions(
            name="blogcomment",
            options={"ordering": ["created"]},
        ),
        migrations.AlterField(
            model_name="blog",
            name="tags",
            field=models.ManyToManyField(null=True, to="blog.tagblog"),
        ),
    ]
