# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 10:02
from __future__ import unicode_literals

from django.db import migrations

from openslides.utils.migrations import (
    add_permission_to_groups_based_on_existing_permission,
)


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_item_duration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={
                'default_permissions': (),
                'permissions': (
                    ('can_see', 'Can see agenda'),
                    ('can_manage', 'Can manage agenda'),
                    ('can_manage_list_of_speakers', 'Can manage list of speakers'),
                    ('can_see_hidden_items', 'Can see hidden items and time scheduling of agenda')
                )
            },
        ),
        migrations.RunPython(add_permission_to_groups_based_on_existing_permission(
            'can_manage', 'item', 'agenda', 'can_manage_list_of_speakers', 'Can manage list of speakers'
        )),
    ]
