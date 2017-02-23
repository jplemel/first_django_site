from django.shortcuts import render, redirect, get_object_or_404
from django.conf.urls import url
from .models import Place
from .forms import NewPlaceForm

# Create your views here.

def place_list(request):

    #If a POST request, this must be from user clicking Add button
    #in the form. Check if new place is valid and add to list, then
    #redirect to 'place_list' route- which ends up creating a Generated
    #request for this same method.

    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')



    places = Place.objects.filter(visited=False);
    form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places':places, 'form':form})

def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited':visited})

def place_is_visited(request):

    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = get_object_or_404(Place, pk=pk)
        place.visited = True
        place.save()

    return redirect('place_list')
