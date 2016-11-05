from django.contrib import admin
from .models import Post   # models.py deki nesneyi import ediyoruz

admin.site.register(Post) # models.py de tanımlı olan post nesnesinin admin panelinde görunur olması
# Register your models here.
