
from pprint import pprint
from rest_framework import permissions
from core.utils.apicodes import ApiCode


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class MyBasePermission(permissions.BasePermission):
    message = ApiCode.error(message="Bạn không có quyền để thực hiện hành động này")


class AllowAny(MyBasePermission):
    def has_permission(self, request, view):
        return True

class IsAdminUser(MyBasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

