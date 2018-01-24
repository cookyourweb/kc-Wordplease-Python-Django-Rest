from datetime import datetime

from rest_framework.permissions import BasePermission


class BlogPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False


class BlogDetailPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' and view.action == 'retrieve':
            return True
        if request.method == 'POST' and request.user.is_authenticated:
            return True
        return False


class PostPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' and view.action == 'retrieve':
            return True
        elif request.method in ['PUT', 'POST', 'DELETE'] and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Si soy administrador o pido los datos de mi propio post, entonces puedo verlos
        if request.user == obj.user or request.user.is_superuser:
            return True
        else:
            if view.action == 'update' or view.action == 'destroy':
                return False
            else:
                now = datetime.now()
                if now.date() > obj.publish_date:
                    return True
        return False
