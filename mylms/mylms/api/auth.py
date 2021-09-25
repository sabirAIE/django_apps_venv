from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#imports for Custom Authentication
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed



"""
@ Here we are going to create a class based View that inherits from ObtainAuthToken and define a function POST
    This customizes the return policy. This token generation method is called the Api Endpoint exposing.
"""
class getCustomAuthToken_API(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serial_data = self.serializer_class(data=request.data, context={'request':request})
        serial_data.is_valid(raise_exception=True)
        user = serial_data.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)

        return Response({
            'token':token.key,
            'user_id':user.pk,
            'email_id':user.email
        })

"""
@ Here we are creating a Custom Authentication for Users
"""
class myCustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        userName = request.GET.get('username')

        if userName is None:
            return None
        try:
            user = User.objects.get(username=userName)
        except User.DoesNotExist:
            raise AuthenticationFailed('No such User found')
        return (user,None)