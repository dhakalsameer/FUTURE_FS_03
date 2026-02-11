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


# 2️⃣ PRICING & BOOKING PAGE
def pricing_booking(request):
    futsal = FutsalInfo.objects.first()

    if request.method == 'POST':
        Booking.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            date=request.POST.get('date'),
            time_slot=request.POST.get('time_slot'),
        )
        messages.success(request, 'Booking request submitted successfully!')
        return redirect('pricing')

    return render(request, 'futsal/pricing.html', {'futsal': futsal})



# 3️⃣ ABOUT PAGE
def about(request):
    futsal = FutsalInfo.objects.first()
    facilities = Facility.objects.all()

    return render(request, 'website/about.html', {
        'futsal': futsal,
        'facilities': facilities
    })


# 4️⃣ CONTACT PAGE
def contact(request):
    futsal = FutsalInfo.objects.first()

    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )
        messages.success(request, 'Message sent successfully!')
        return redirect('contact')

    return render(request, 'futsal/contact.html', {'futsal': futsal})
