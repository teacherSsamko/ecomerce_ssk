from django.shortcuts import redirect
from .models import Fcuser


def login_required(function):
    def wrap(request, *arg, **kwargs):
        print('login_required!')
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login/')
        return function(request, *arg, **kwargs)

    return wrap


def admin_required(function):
    def wrap(request, *arg, **kwargs):
        print('login_required!')
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login/')

        user = Fcuser.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/')

        return function(request, *arg, **kwargs)

    return wrap
