from _decimal import Decimal

from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseNotAllowed
import json
from datetime import datetime

from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_csrf_token(request, *args, **kwargs):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])
