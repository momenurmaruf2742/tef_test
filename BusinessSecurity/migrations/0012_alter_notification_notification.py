# Generated by Django 3.2.7 on 2022-01-05 04:25

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0011_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification',
            field=tinymce.models.HTMLField(),
        ),
    ]