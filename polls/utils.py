from functools import wraps
import random

from django.contrib.auth.models import User


def get_or_set_user_id(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # I think that method is not the best, but I didn't found
        # any other way, because I never worked with cookies and sessions before
        request = args[0]
        need_set_cookie = False

        if request.user.is_authenticated:
            kwargs['user_id'] = request.user.id
        else:
            cookie = request.headers.get('Cookie')

            if 'user_id' not in cookie:
                user, created = User.objects.get_or_create(username=cookie)
                user_id = user.id
                need_set_cookie = True

            else:
                cookie_fields = cookie.split('; ')
                for field in cookie_fields:
                    if field.startswith('user_id'):
                        user_id = field.split('=')[1]
                        break
            kwargs['user_id'] = user_id

        response = function(*args, **kwargs)

        if need_set_cookie:
            response.set_cookie('user_id', user_id)
        return response
    return wrapper
