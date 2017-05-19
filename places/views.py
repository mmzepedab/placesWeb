from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views.generic.detail import DetailView

from .forms import CategoryForm, PlaceForm, OfferForm
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
    if request.method == 'POST':
        form = PlaceForm(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('list_place'))
    else:
        form = PlaceForm(request.POST or None)

    context = {
        "place_form": form,
    }

    return render(request, "place/place_create.html",  context)

def place_update(request, pk):
    instance = get_object_or_404(Place, id=pk)
    if request.method == 'POST':
        form = PlaceForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('list_place'))
    else:
        form = PlaceForm(request.POST or None, request.FILES or None, instance=instance)

    form.helper.form_action = reverse_lazy('update_place', kwargs={'pk': pk}, )
    context = {
        "place_form": form,
    }

    return render(request, "place/place_update.html",  context)

def place_delete(request, pk):
    Place.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse('list_place'))

@login_required
def logoutView(request):
    if request.method == 'POST':
        logout(request)
        print('logout done')
    return render(request, 'about.html')

class PlaceDetailView(DetailView):
    model = Place
    template_name = 'place/place_detail.html'


# Offer Views
def add_offer_to_place(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == 'POST':
        form = OfferForm(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.place = place
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('list_place'))
    else:
        form = OfferForm(request.POST or None)

    context = {
        "offer_form": form,
        "place": place
    }

    return render(request, "offer/offer_create.html",  context)


def offer_create(request, place_id):
    if request.method == 'POST':
        form = OfferForm(request.POST or None, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('list_place'))
    else:
        form = OfferForm(request.POST or None)

    context = {
        "offer_form": form,
    }

    return render(request, "offer/offer_create.html",  context)