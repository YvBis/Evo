# Generated by Django 3.2.11 on 2022-01-19 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hello', '0003_alter_email_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='auth.user'),
        ),
    ]
