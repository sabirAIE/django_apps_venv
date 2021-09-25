from django.db.models import query
from .models import studentModel
from .serializers import studentModelSerializer
from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.filters import OrderingFilter
#here we are importing the custom modified version of PageNumberPagination
from .myPagination import myCustomPagination, customLimitOffsetPagination,customCursorPagination
"""
# Lets Create a Class Based API using generic ListAPIView. Then we will apply the 
@ PageNumberPagination-
    - To apply Pagination Globally we need to set in Settings by the name 
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination'
        'PAGE_SIZE': Whatever number you want

    -Note that you need to set both the pagination class, and the page size that
         should be used. Both DEFAULT_PAGINATION_CLASS and PAGE_SIZE are None by default.
    
    - We can not directly use the modified version of PageNumberPagination in our view. We need to override
        The functionalities to make use of. So Create a sub Class and Override. We can create here or we can
        also create the class in new file import here and use.

@ LimitOffsetPagination-
    - This pagination style mirrors the syntax used when looking up multiple database records. 
        The client includes both a "limit" and an "offset" query parameter. The limit indicates the
        maximum number of items to return, and is equivalent to the page_size in other styles. The offset
        indicates the starting position of the query in relation to the complete set of unpaginated items.
    
    -To apply Pagination Globally we need to set in Settings by the name 
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination'
        'PAGE_SIZE': Whatever number you want
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100

@ CursorPagination-
    Proper use of cursor based pagination requires a little attention to detail. You'll need to think 
    about what ordering you want the scheme to be applied against. The default is to order by "-created".
    This assumes that there must be a 'created' timestamp field on the model instances, and will present 
    a "timeline" style paginated view, with the most recently added items first.

    You can modify the ordering by overriding the 'ordering' attribute on the pagination class, or by 
    using the OrderingFilter filter class together with CursorPagination. When used with OrderingFilter 
    you should strongly consider restricting the fields that the user may order by.
"""

class getStudentListPerPage_API(ListAPIView):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer
    
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Now we will apply the Pagination here PageNumberPagination
    pagination_class = myCustomPagination

# here we are going to write a function to List and Create. We will use ListCreatAPIView to over come this
class studentListCreate_API(ListCreateAPIView):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


# Let's write class based API using the ListAPIView, and an added functionality of pagination using
    #LimitOffsetPagination. We need to override the functions that are default set. Check 

class studentListLimitOffsetPagination(ListAPIView):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Here we are going to Set the Pagination function
    pagination_class = customLimitOffsetPagination
    

# Let's Create a class Based API using ListAPIView and add custom cursor pagination using 
    # CursorPagination, We need to override the functions that are default set.
class studentListCursorPagination_API(ListAPIView):
    queryset = studentModel.objects.all()
    serializer_class = studentModelSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    #here we are going to set the pagination function
    pagination_class = customCursorPagination