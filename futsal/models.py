from django.db import models


# 1️⃣ FUTSAL BASIC INFO (Home + Contact)
class FutsalInfo(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    google_map_link = models.URLField(blank=True)

    opening_time = models.CharField(max_length=50)
    closing_time = models.CharField(max_length=50)
    price_per_hour = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# 2️⃣ SERVICES / FACILITIES
class Facility(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='facilities/', blank=True, null=True)

    def __str__(self):
        return self.title


# 3️⃣ BOOKING REQUEST (SIMPLE & REALISTIC)
class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time_slot = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date}"


# 4️⃣ CONTACT FORM
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# 5️⃣ GALLERY (OPTIONAL BONUS)
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "Gallery Image"
