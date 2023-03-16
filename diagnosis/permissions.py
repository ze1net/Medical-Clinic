# from rest_framework.permissions import BasePermission, SAFE_METHODS
#
# class IsAdminOrDiagnosisOwner(BasePermission):
#     """
#     Custom permission to allow admins to read, update, and delete their own diagnosis and deny all other users from modifying any diagnosis.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         elif request.user.is_staff and obj.owner == request.user:
#             return True
#         else:
#             return False
#
#
# class IsDiagnosisOwner(BasePermission):
#     """
#     Custom permission to allow users to read their own diagnosis and deny access to all other diagnosis.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         elif obj.owner == request.user:
#             return True
#         else:
#             return False


from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrDiagnosisOwner(BasePermission):
    """
    Custom permission to allow admins to read, update, and delete their own diagnosis and deny all other users from modifying any diagnosis.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_staff and obj.owner == request.user:
            return True
        elif obj.owner == request.user:
            return True
        else:
            return False


class IsDiagnosisOwner(BasePermission):
    """
    Custom permission to allow users to read their own diagnosis and deny access to all other diagnosis.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif obj.owner == request.user:
            return True
        else:
            return False
