from django.shortcuts import render
import requests
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from homeward_test_app_1.consume_qualia_api import QualiaClient


def get_qualia(request):
    client = QualiaClient()
    client.get_all_order_ids()

# def index(request):
#     r = requests.get('http://httpbin.org/status/418')
#     print(r.text)
#     return HttpResponse('<pre>' + r.text + '</pre>')