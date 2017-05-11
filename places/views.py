from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views.generic.detail import DetailView

from .forms import CategoryForm, PlaceForm
from .models import Category, Place

@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the places index.")

def category_create(request):
    form = CategoryForm(request.POST or None)
    print request.POST.get("name")
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('list_category'))


    #if request.method == "POST":
    #    print request.POST.get("content")
    #    name = request.POST.get("name")

    context = {
        "form" : form,
    }

    return render(request, "category_form.html",  context)

def category_list(request):
    categories = Category.objects.all()

    context = {
        "categories" : categories,
    }

    return render(request, "category_list.html",  context)

def place_list(request):
    if request.user.is_authenticated():
        logged_in_user = request.user
        logged_in_user_places = Place.objects.filter(user=logged_in_user)
    else:
        logged_in_user_places = ""

    context = {
        "places" : logged_in_user_places,
    }

    return render(request, "place/place_list.html",  context)

def place_create(request):
    form = PlaceForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('list_place'))

    context = {
        "place_form": form,
    }

    return render(request, "place/place_create.html",  context)

def place_delete(request):
    Place.objects.filter(id=6).delete()
    return HttpResponseRedirect(reverse('list_place'))

    context = {
        "form": form,
    }

    return render(request, "place/place_create.html",  context)

@login_required
def logoutView(request):
    if request.method == 'POST':
        logout(request)
        print('logout done')
    return render(request, 'about.html')

class PlaceDetailView(DetailView):
    model = Place
    template_name = 'place/place_detail.html'
