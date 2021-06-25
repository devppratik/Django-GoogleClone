from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
# Create your views here.
def index(request):
    return render(request, 'index.html')
