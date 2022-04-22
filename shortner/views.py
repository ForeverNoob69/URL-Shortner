from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Urls
import uuid
# Create your views here.


def index(request):
    return render(request, "index.html")


def Home(request):
    contest = {"placeholder": "Enter your URL"}
    if request.method == "POST":
        url = request.POST["link"]
        uid = str(uuid.uuid4())[:5]
        new_url = Urls(link=url, uuid=uid)
        new_url.save()
        contest = {
            "variable": "localhost:8000/"+uid,
            "placeholder": url}
        return render(request, "home.html", contest)
    return render(request, "home.html", contest)


# def create(request):
    if request.method == "POST":
        url = request.POST["link"]
        if len(url) == 0:
            return render(request, "home.html")
        uid = str(uuid.uuid4())[:5]
        new_url = Urls(link=url, uuid=uid)
        new_url.save()
        contest = {
            "variable": "localhost:8000/"+uid,
            "placeholder": url}
        return render(request, "home.html", contest)


def go(request, pk):
    url_details = Urls.objects.get(uuid=pk)
    return redirect(url_details.link)
