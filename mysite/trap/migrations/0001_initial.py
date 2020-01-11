# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('uid', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False, help_text='Unique ID for this particular id.')),
                ('contribution', models.DecimalField(max_digits=19, decimal_places=10)),
                ('profit', models.DecimalField(max_digits=19, decimal_places=10)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subordinate', models.ForeignKey(related_name='subordinate_relationship_set', to='trap.Mouse')),
                ('superior', models.ForeignKey(related_name='superior_relationship_set', to='trap.Mouse')),
            ],
        ),
    ]
