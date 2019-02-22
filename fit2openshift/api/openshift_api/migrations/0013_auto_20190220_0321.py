# Generated by Django 2.1.2 on 2019-02-20 03:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0012_host_nodechangelog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]