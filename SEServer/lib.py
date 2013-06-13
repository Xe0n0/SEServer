import logging
from functools import wraps
import datetime
from json import dumps
import sys

from django.utils.decorators import available_attrs
from django.http import HttpResponseNotAllowed, HttpResponseNotModified, HttpResponse

logger = logging.getLogger('django.request')


def json_response(func):
    dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None

    @wraps(func, assigned=available_attrs(func))
    def inner(request=None, *args, **kwargs):
        status_code = 200
        response = func(request, *args, **kwargs)
        content = response
        if isinstance(response, tuple):
            content = response[0]
            status_code = response[1]

        return HttpResponse(dumps(content, default=dthandler, ensure_ascii=False, separators=(',',':')),
          mimetype="application/json", status=status_code)

    return inner

def auth_required(func):

    @wraps(func, assigned=available_attrs(func))
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated():
            return func(request, *args, **kwargs)
        else:
            return HttpResponse(dumps({'error_code': 'NotLoggedIn'}), mimetype="application/json", status=403)
    return inner

def require_params(required_params_list):
    """
    Decorator to make a view only accept if required params provided  Usage::

        @require_params(["username", "password"])
        def my_view(request):
            # I can directly use `username` and `password` now
            # ...

    Note that request methods should be in uppercase.
    """
    def decorator(func):
        @wraps(func, assigned=available_attrs(func))
        def inner(request, *args, **kwargs):
            args = [request.POST.get(key, None) for key in required_params_list]
            print >> sys.stderr, args
            if None in args:

                return {
                    'status': 103,
                    'user_info': u'bad params',
                }

            return func(request, *args, **kwargs)
        return inner
    return decorator