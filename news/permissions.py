from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif bool(request.user and request.user.is_authenticated):
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        elif request.method in SAFE_METHODS:
            return True