# Generated by Django 4.2.11 on 2024-04-03 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_rename_user1_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='CreatedUserId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_app.user'),
        ),
    ]
