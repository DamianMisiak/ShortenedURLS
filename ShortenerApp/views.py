import random
import string
from django.http import Http404
from django.shortcuts import render, redirect
from ShortenerApp.models import UrlData
from ShortenerApp.forms import Url


def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(7))
            url = form.cleaned_data["url"]
            new_url = UrlData(url=url, slug=slug)
            new_url.save()
            return render(request, 'ShortenerApp/shortened_url.html', {'new_url': new_url})
    else:
        form = Url()

    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'ShortenerApp/base.html', context)


def urlRedirect(request, slugs):
    data = None
    try:
        data = UrlData.objects.get(slug=slugs)
    except UrlData.DoesNotExist:
        print('Coś poszło nie tak')

    if data:
        return redirect(data.url)
    else:
        raise Http404
