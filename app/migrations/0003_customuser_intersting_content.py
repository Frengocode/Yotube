# Generated by Django 5.0.4 on 2024-04-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_commentmodel_content_alter_commentmodel_like_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='intersting_content',
            field=models.CharField(choices=[('Для Взрослых', 'Для Взрослых'), ('Для Детей', 'Для Детей'), ('Для Подростков', 'Для Подростков')], default=1, max_length=45),
            preserve_default=False,
        ),
    ]
