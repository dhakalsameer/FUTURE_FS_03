from django.shortcuts import render, redirect
from .models import (
    FutsalInfo,
    Facility,
    Booking,
    ContactMessage,
    GalleryImage
)
from django.contrib import messages
import datetime

# 1️⃣ HOME PAGE
def home(request):
    futsal = FutsalInfo.objects.first()
    
    # Static images from the static/gallery folder
    static_gallery_images = [
        {'static_path': 'gallery/attack.jpg'},
        {'static_path': 'gallery/ball.jpg'},
        {'static_path': 'gallery/boot.jpg'},
        {'static_path': 'gallery/futsal.jpg'},
        {'static_path': 'gallery/ground.jpeg'},
    ]

    facilities = Facility.objects.all()

    context = {
        'futsal': futsal,
        'gallery': static_gallery_images,
        'facilities': facilities,
    }
    return render(request, 'futsal/home.html', context)


# 2️⃣ PRICING & BOOKING PAGE
def pricing_booking(request):
    futsal = FutsalInfo.objects.first()

    # Define all possible time slots (e.g., hourly from 9 AM to 10 PM)
    all_possible_time_slots = [
        "09:00 AM - 10:00 AM", "10:00 AM - 11:00 AM", "11:00 AM - 12:00 PM",
        "12:00 PM - 01:00 PM", "01:00 PM - 02:00 PM", "02:00 PM - 03:00 PM",
        "03:00 PM - 04:00 PM", "04:00 PM - 05:00 PM", "05:00 PM - 06:00 PM",
        "06:00 PM - 07:00 PM", "07:00 PM - 08:00 PM", "08:00 PM - 09:00 PM",
        "09:00 PM - 10:00 PM",
    ]

    selected_date_str = request.GET.get('date', datetime.date.today().isoformat())
    try:
        selected_date = datetime.date.fromisoformat(selected_date_str)
    except ValueError:
        selected_date = datetime.date.today()
        selected_date_str = selected_date.isoformat()

    booked_slots_on_selected_date = Booking.objects.filter(date=selected_date).values_list('time_slot', flat=True)
    available_slots = [slot for slot in all_possible_time_slots if slot not in booked_slots_on_selected_date]

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date_str = request.POST.get('date')
        time_slot = request.POST.get('time_slot')

        try:
            booking_date = datetime.date.fromisoformat(date_str)
        except ValueError:
            messages.error(request, 'Invalid date format.')
            return redirect('pricing')

        # Check if the requested slot is actually in the available slots
        if time_slot not in all_possible_time_slots:
            messages.error(request, 'Invalid time slot selected.')
            return redirect('pricing')

        # Check for existing booking
        if Booking.objects.filter(date=booking_date, time_slot=time_slot).exists():
            messages.error(request, f'The slot {time_slot} on {booking_date} is already booked!')
            return redirect('pricing')
        
        # Check if the requested slot is in the past
        # Note: This comparison for time is simplistic as time_slot is a string.
        # A more robust solution would involve proper time parsing.
        now = datetime.datetime.now()
        current_time_str = now.strftime("%I:%M %p") # Use %I for 12-hour clock for comparison
        requested_start_time_str = time_slot.split(' - ')[0]

        # Convert both to datetime objects for accurate comparison if needed
        # For now, simplistic string comparison for start times for date == today
        if booking_date < datetime.date.today() or \
           (booking_date == datetime.date.today() and 
            datetime.datetime.strptime(requested_start_time_str, "%I:%M %p").time() < now.time()):
            messages.error(request, 'Cannot book a slot in the past.')
            return redirect('pricing')


        Booking.objects.create(
            name=name,
            phone=phone,
            date=booking_date,
            time_slot=time_slot,
        )
        messages.success(request, f'Booking request for {time_slot} on {booking_date} submitted successfully!')
        return redirect('pricing')

    context = {
        'futsal': futsal,
        'all_possible_time_slots': all_possible_time_slots,
        'available_slots': available_slots,
        'selected_date': selected_date_str, # Pass back for frontend display
    }
    return render(request, 'futsal/pricing.html', context)



# 3️⃣ ABOUT PAGE
def about(request):
    futsal = FutsalInfo.objects.first()
    facilities = Facility.objects.all()

    return render(request, 'futsal/about.html', {
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


# 5️⃣ GALLERY PAGE
def gallery(request):
    futsal = FutsalInfo.objects.first()
    gallery = GalleryImage.objects.all()

    context = {
        'futsal': futsal,
        'gallery': gallery,
    }
    return render(request, 'futsal/gallery.html', context)
