from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from json import dumps
from .models import Url
from .forms import UrlForm


def get_shortened_url(long_url: str):
    url_obj = Url()
    url_obj.long_url = long_url
    short_url, new_object = url_obj.generate_shortened_url(long_url)
    url_obj.save() if new_object is True else None
    return url_obj

def gen_url(request: HttpRequest):
    if request.method == 'GET':
        form = UrlForm()
        return render(request, 'urlShort/gen_url.html', {'form': form})
    form = UrlForm(request.POST)
    if form.is_valid():
        url = form.cleaned_data.get('url')
        if form.check_url(url) is False:
            messages.warning(request, 'Invalid URL')
            return redirect('generate-url')
        url_obj = get_shortened_url(url)
        return render(request, 'urlShort/short_url.html', {'short_url': url_obj.short_url})
    
def redirect_url(request: HttpRequest, short_url: str):
    
        url_obj = Url.objects.filter(short_url=short_url)
        if url_obj.exists():
            url_obj = url_obj.first()
            url_obj.clicks += 1
            url_obj.save()
            return redirect(url_obj.long_url)
    
        messages.warning(request, 'The URL you tried to access does not exist. Please generate a new one!')
        return redirect('generate-url')

def about(request: HttpRequest):
    return render(request, 'urlShort/about.html')

def api_shortener(request: HttpRequest):
    long_url = request.headers.get('long_url')
    
    if long_url is None:
        return HttpResponse(dumps({
            "error": "please provide a 'long_url' in the request headers"
            }))
    url_obj = get_shortened_url(long_url)
    return HttpResponse(dumps({
        'short_url': url_obj.short_url,
        'long_url': url_obj.long_url,
        'clicks': url_obj.clicks,
        'created_at': url_obj.created,
    }))