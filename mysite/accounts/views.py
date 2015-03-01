# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth
from forms import LoginForm
from models import User


def ajax_login(request):
    args = {}
    args.update(csrf(request))
    args['form'] = LoginForm()

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                username = 'admin'
                password = request.POST.get('password')
                user = auth.authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                    return render_to_response("yes.html", user)
            except User.DoesNotExist:
                pass

    return render_to_response("ajax_login.html", args)