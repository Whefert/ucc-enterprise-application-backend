# Generated by Django 5.1.4 on 2024-12-13 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ucc', '0002_remove_courseschedulelecturer_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='ucc.user'),
        ),
    ]