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
                ('currency', models.DecimalField(max_digits=19, decimal_places=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('context', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(related_name='creator_notification_set', to='trap.Mouse')),
                ('receiver', models.ForeignKey(related_name='receiver_notification_set', to='trap.Mouse')),
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
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.DecimalField(max_digits=19, decimal_places=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('from_mouse', models.ForeignKey(related_name='from_mouse_transaction_set', to='trap.Mouse')),
                ('to_mouse', models.ForeignKey(related_name='to_mouse_transaction_set', to='trap.Mouse')),
            ],
        ),
    ]
