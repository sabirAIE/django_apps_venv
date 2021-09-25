from rest_framework import permissions
from rest_framework.permissions import BasePermission
from .models import studentModel
"""
We can make define different Clsses and override the has_permission function and call the Class in our Views
here we have defined two custom permissions
"""
class MyCustomPermission(BasePermission):
    message = "only Get Method is allowed in this API"
    
    """
    has_permission function overrides the basePermission function and based on the Logic we can get access to the
    API. Here we have implemented an basic Request logic based on the Request Method We are allowing the user to
    perform an operation.
    """
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method =='POST' or request.method =='PUT':
            return True
        return False

#to block a perticuler IP Address we make logic like, I have Written this is for an axample
class BlockListPermission(BasePermission):
    def has_permission(self, request, view):
        ip_address = request.META['REMOTE_ADDR']
        bloked = studentModel.objects.filter(id= ip_address).exists()
        return not bloked