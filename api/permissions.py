from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user or not request.user.is_authenticated:
            return False
        return bool(
            request.user.is_admin or
            request.user.is_superuser
        )

# class Permission1(BasePermission):
#     massage = "Нет прав на данное действие"

#     def has_permission(self, request, view):
#         if request.user.is_admin or (
#                 request.user.is_staff or
#                 request.user.is_superuser):
#             return True
#         return False


# class ReviewCommentPermission(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.method in SAFE_METHODS or (
#             request.user == obj.author or
#             request.user.is_admin or
#             request.user.is_moderator or
#             request.user.is_staff or request.user.is_superuser)
