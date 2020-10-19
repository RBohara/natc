from django.shortcuts import render
from .models import GalleryFile

# Create your views here.


def gallery(request):
    gallery_files = GalleryFile.objects.all()
    context = {'gallery_files': gallery_files}
    return render(request, 'gallery/gallery.html', context)
