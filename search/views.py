from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
# Create your views here.
def index(request):
    return render(request, 'index.html')


def search(request):
    if request.method == 'POST': 
        search = request.POST['search']
        url = 'https://www.ask.com/web?q=' + search
        res = requests.get(url=url)
        soup = bs(res.text, 'lxml')
        all_listings = soup.find_all('div', {'class' : 'PartialSearchResults-item'})
        final_results = []
        for result in all_listings:
            result_title = result.find(class_='PartialSearchResults-item-title').text
            result_url = result.find('a').get('href')
            result_desc = result.find(class_='PartialSearchResults-item-abstract').text

            final_results.append((result_title, result_url, result_desc))

        results = {
            'final_result': final_results,
            'search' : search
        } 

        return render(request, 'search.html', context=results)
    else:

        return render(request, 'search.html', )