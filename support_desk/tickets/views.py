from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import math
from django.conf import settings


# Create your views here.
def index(request):
    url = f"{settings.END_POINT}tickets.json?per_page={settings.PER_PAGE}&page={get_current_page(request)}"

    res = requests.get(url, auth=HTTPBasicAuth(settings.AUTH_USER, settings.AUTH_PASS))
    data = res.json()
    if not validate_response_status(res):
        return render(request, '505.html', status=500)
    return render(request, 'index.html',
                  {'data': data,
                   'pagination': calculate_pagination(request, data['count'], 25),
                   'current_page': get_current_page(request),
                   'status': validate_response_status(res)
                   })


def list(request, id: int):
    url = f"{settings.END_POINT}tickets/{id}.json"
    res = requests.get(url, auth=HTTPBasicAuth(settings.AUTH_USER, settings.AUTH_PASS))
    data = res.json()
    if not validate_response_status(res):
        return render(request, '505.html', status=500)
    return render(request, 'view.html', {"ticket": data['ticket']})


def calculate_pagination(request, total_pages, per_page):
    page_count = math.ceil(total_pages / per_page)
    return {
        "page_min": 1,
        "page_max": int(page_count),
        "page_range": range(1, page_count + 1),
        "previous_page": get_current_page(request) - 1,
        "next_page": get_current_page(request) + 1
    }


def get_current_page(request):
    page = request.GET.get('page')
    if page is None or not page.isnumeric():
        return 1
    return int(page)


def validate_response_status(res):
    return int(res.status_code) == 200
