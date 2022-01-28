from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


# class LoginAndUserMixin(AccessMixin):
#     """Checks if this is the user's portfolio"""
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated and request.user.pk !=

