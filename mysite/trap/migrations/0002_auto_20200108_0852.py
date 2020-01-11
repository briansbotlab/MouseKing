# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('context', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.DecimalField(max_digits=19, decimal_places=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='mouse',
            old_name='contribution',
            new_name='currency',
        ),
        migrations.RemoveField(
            model_name='mouse',
            name='profit',
        ),
        migrations.AddField(
            model_name='transaction',
            name='from_mouse',
            field=models.ForeignKey(related_name='from_mouse_transaction_set', to='trap.Mouse'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='to_mouse',
            field=models.ForeignKey(related_name='to_mouse_transaction_set', to='trap.Mouse'),
        ),
        migrations.AddField(
            model_name='notification',
            name='creator',
            field=models.ForeignKey(related_name='creator_notification_set', to='trap.Mouse'),
        ),
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(related_name='receiver_notification_set', to='trap.Mouse'),
        ),
    ]
