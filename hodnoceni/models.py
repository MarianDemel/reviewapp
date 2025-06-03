from django.db import models
from django.conf import settings

class Place(models.Model):
    id = models.AutoField(primary_key=True)  # Implicitní chování
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    popis = models.TextField()
    rating = models.PositiveSmallIntegerField()
    datum_vytvoreni = models.DateTimeField(auto_now_add=True)  # Přidáno
    datum_upraveni = models.DateTimeField(auto_now=True)      # Přidáno

    def __str__(self):
        return f"Review by {self.user.username} for {self.place.name} (Rating: {self.rating})"
