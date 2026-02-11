from django.contrib import admin
from .models import (
    FutsalInfo,
    Facility,
    Booking,
    ContactMessage,
    GalleryImage
)

admin.site.register(FutsalInfo)
admin.site.register(Facility)
admin.site.register(Booking)
admin.site.register(ContactMessage)
admin.site.register(GalleryImage)
