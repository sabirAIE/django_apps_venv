from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .auth import getCustomAuthToken_API
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView
from .views import *

router = DefaultRouter()

router.register('getStudentWithAuthToken', getStudentsWithTokenAuth_API, basename='get_data_with_token_api')


"""
@ Here obtain_auth_token is a View Based Token Generator which can be called using Http POST request and in 
    return it gives a JSON (JavaScript Object notation) object with key "token". just send a http POST request
    with the user name and password

@ Here the second url is for getting the customToken with other user information which is defined in the 
    auth.py file. This method is requires to send username with the request
"""

app_name='api'
urlpatterns = [
    path('getToken_API/',obtain_auth_token,name='obtain_token_api'),
    path('getTokenInfo_API/', getCustomAuthToken_API.as_view(), name='get_token_info_api'),
    path('',include(router.urls),name='get_students_with_token_api'),
    # Here are three urls to get, refresh, verify the tokens as per need this requires username and password 
    # to be sent with the request
    path('getToken/', TokenObtainPairView.as_view(),name='get_token_api'),
    path('refreshToken/', TokenRefreshView.as_view(),name='token_refresh_api'),
    path('verifyToken/', TokenVerifyView.as_view(),name='token_verify_api')
]
