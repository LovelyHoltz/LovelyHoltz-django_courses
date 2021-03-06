from django.shortcuts import render, redirect

from . models import Artist, Album


def index(request):
    context = {
        "artists": Artist.objects.all()
    }
    return render(request,'artists/index.html', context)

def new(request):
    context = {
        "all_artists": Artist.objects.all()
    }
    return render(request, "artists/new.html", context)

def show(request, artist_id):
    context = {
        'artist': Artist.objects.get(id=artist_id)
    }
    return render(request, 'artists/show.html',context)

def create(request):
    print request.POST
    print("ohw" in request.POST)
    if "ohw" in request.POST:
        print ("we have one hit")
    else:
        print("we have many hits")

    Artist.objects.create(
        name = request.POST['name'],
        date_formed = request.POST['formed'],
        one_hit_wonder = "ohw" in request.POST
    )
    print('we have created artist!!')
    return redirect('/')

def delete(request, artist_id):
        artist_to_delete = Artist.objects.get(id=artist_id)
        artist_to_delete.delete()

        return redirect('/')

#####################################
#ALBUMS-MANY TO ONE AND MANY TO MANY##
#####################################

def create_album(request):
    print request.POST
    Album.objects.create(
        title = request.POST['title'],
        release_date = request.POST['release_date'],
        records_sold = request.POST['records_sold'],
        num_songs = request.POST['num_songs'],
        artist = Artist.objects.get(id=request.POST['artist_id'])
    )
    return redirect('/')
