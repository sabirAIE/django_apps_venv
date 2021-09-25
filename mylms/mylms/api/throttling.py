from rest_framework.throttling import UserRateThrottle

"""
@ This is a custom Throttle class inherites and overrides the scope property. Import and user any where 
    you want. Here the scope property is also defined in the DEFAULT_THROTTLE_RATES settings file.
"""
class customRateThrottle(UserRateThrottle):
    scope = 'customThrottle'