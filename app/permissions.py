from rest_framework.permissions import BasePermission

from app.models import User


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        username = request.data.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            return True
        return False
