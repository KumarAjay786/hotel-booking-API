from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Add any custom fields here

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'


CustomUser.groups.field.remote_field.related_name = 'custom_user_groups'
CustomUser.user_permissions.field.remote_field.related_name = 'custom_user_permissions'
