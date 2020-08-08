# Generated by Django 3.0.8 on 2020-08-08 01:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200805_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsstory',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='newsstory',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsstory',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]