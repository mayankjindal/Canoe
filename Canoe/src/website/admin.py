from django.contrib import admin

# Register your models here.
from .models import EventRegister, Event, AthleteRegister, OfficeBearers, Gallery

admin.site.register(EventRegister)
admin.site.register(Event)
admin.site.register(AthleteRegister)
admin.site.register(OfficeBearers)
admin.site.register(Gallery)