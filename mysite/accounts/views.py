# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.context_processors import csrf


def ajax_login(request):
    return render_to_response("ajax_login.html")