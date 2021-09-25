from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination

class myCustomPagination(PageNumberPagination):
    page_size = 5                       # Results per page
    page_query_param = 'p'              # Query parameter befault 'page'
    page_size_query_param = 'records'   # Client side result size parameter
    max_page_size = 7                   # fix the max result size
    # last_page_strings = 'end'

"""
@ LimitOffsetPagination is used where we want to have a flexible way to get data
    - Limit is the result per page
    - offset is the number from where you want the result

"""
class customLimitOffsetPagination(LimitOffsetPagination):
    max_limit =10                       # Max Result per page
    default_limit = 6                   # default result per page
    limit_query_param = 'limit'         # as name suggested client siide Limit url parameter
    offset_query_param = 'offset'       # as name suggest client side Limit url parameter


"""
@ CursorPagination-
    The cursor-based pagination presents an opaque "cursor" indicator that the client may use to page through 
    the result set. This pagination style only presents forward and reverse controls, and does not allow the 
    client to navigate to arbitrary positions.
"""
class customCursorPagination(CursorPagination):
    page_size = 4
    cursor_query_param = 'cursor'    # We can change what ever we want this is set to 'cursor'