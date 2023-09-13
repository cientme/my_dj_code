from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False

        # # It will work when you give post request to user.
        # if request.method == 'POST':
        #     return True
        # return False