from django.shortcuts import render, redirect
from .models import (
    FutsalInfo,
    Facility,
    Booking,
    ContactMessage,
    GalleryImage
)
from django.contrib import messages

# 1️⃣ HOME PAGE
def home(request):
    futsal = FutsalInfo.objects.first()
    facilities = Facility.objects.all()
    gallery = GalleryImage.objects.all()

    context = {
        'futsal': futsal,
        'facilities': facilities,
        'gallery': gallery,
    }
    return render(request, 'futsal/home.html', context)