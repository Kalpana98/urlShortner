from django.shortcuts import render, redirect
import random
from Authentication.models import Url

def index(request):

    if request.method == "POST":
        link = request.POST.get("link")
        short_link = ""

        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        url = Url.objects.all()
        
        for i in url:
            if i.link == link:
                short_link = i.short_link
                break
        else:
            for i in range(0, 6):
                char = random.randint(1, len(chars) - 1)
                alph_num = chars[char]
                short_link += alph_num

            url = Url(link=link, short_link=short_link)
            url.save()

        new_url = "http://127.0.0.1:8000/" + short_link
        return render(request, "index.html", {"new_url": new_url})

    return render(request, "index.html")

def shorten(request, id):
    url = Url.objects.filter(short_link=id)
    link = ""
    for i in url:
        link = i.link
    return redirect(link)
