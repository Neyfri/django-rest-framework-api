# Generated by Django 5.0.1 on 2024-02-02 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_persondesc_color_skin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='persondesc',
            name='nickname',
            field=models.CharField(default='Maria', max_length=200),
            preserve_default=False,
        ),
    ]
