from django.contrib import admin
from .models import (
    FutsalInfo,
    Facility,
    Booking,
    ContactMessage,
    GalleryImage
)


@admin.register(FutsalInfo)
class FutsalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'price_per_hour')


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'time_slot', 'created_at')
    list_filter = ('date',)
    search_fields = ('name', 'phone')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption',)
