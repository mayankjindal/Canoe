from django import forms
from .models import EventRegister, AthleteRegister


class EventRegisterForm(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()
    athleteid = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    teamname = forms.CharField()


class EventRegistrationCreateForm(forms.ModelForm):
    class Meta:
        model = EventRegister
        fields = [
            'fname',
            'lname',
            'email',
            'phone',
            'athleteid',
            'city',
            'state',
            'teamname'
        ]


class AthleteRegisterForm(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()
    dob = forms.DateField()
    aadhaar = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()


class AthleteRegistrationCreateForm(forms.ModelForm):
    class Meta:
        model = AthleteRegister
        fields = [
            'fname',
            'lname',
            'email',
            'phone',
            'dob',
            'aadhaar',
            'city',
            'state',
        ]


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField()
