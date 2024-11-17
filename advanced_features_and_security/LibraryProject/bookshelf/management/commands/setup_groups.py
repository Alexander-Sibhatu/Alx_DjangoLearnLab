from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Set up default groups and permissions.'

    def handle(self, *args, **kwargs):
        groups_permissions = {
            'Editors': ['can_edit', 'can_create'],
            'Viewers': ['can_view'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }

        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_codename in permissions:
                try:
                    permission = Permission.objects.get(codename=perm_codename, content_type__app_label='bookshelf')
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stderr.write(f"Permission {perm_codename} not found.")

        self.stdout.write("Groups and permissions have been set up successfully.")
