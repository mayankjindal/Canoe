from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify

User = settings.AUTH_USER_MODEL


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    prize = models.CharField(max_length=15)
    date = models.DateField()
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.event_name)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.event_name


class EventRegister(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.BigIntegerField(default=60)
    email = models.EmailField(max_length=50)
    athleteid = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    teamname = models.CharField(max_length=50)

    def __str__(self):
        return self.fname


class AthleteRegister(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.BigIntegerField(default=60)
    email = models.EmailField(max_length=50)
    dob = models.DateField()
    athleteid = models.CharField(max_length=30)
    aadhaar = models.BigIntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.fname


class OfficeBearers(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    phone = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='static/img')
    social_media = models.CharField(max_length=200, default="https://www.fb.com")

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/img')
    desc = models.TextField()

    def __str__(self):
        return self.name
