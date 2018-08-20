from django.shortcuts import render
from .models import EventRegister, Event, AthleteRegister, OfficeBearers, Gallery
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EventRegisterForm, AthleteRegisterForm, ContactForm
from django.core.mail import send_mail, EmailMessage


def index(request):
    form = ContactForm()
    if request.method == "POST":
        print("POST")
        form = ContactForm(request.POST)
        print(form.errors)

        if form.is_valid():
            print("IS VALID")
            subject = form.cleaned_data.get('subject')
            plain_message = form.cleaned_data.get('message')
            from_email = form.cleaned_data.get('email')
            print(from_email)
            to = 'jindalmayank78@gmail.com'
            email = EmailMessage(subject, plain_message, to=[to])
            print(email)
            email.send()

            return HttpResponseRedirect('/')

        else:
            form = ContactForm()

    return render(request, 'index.html', {'form': form})


def gallery(request):
    context = {'img': []}
    gal = Gallery.objects.all()
    for g in gal:
        context['img'].append(g)

    return render(request, 'gallery.html', context)


def events(request):
    event_list = {}
    context = {}
    events = Event.objects.all()
    for e in events:
        event_list[e.event_name] = {'prize': e.prize, 'date': e.date, 'place': e.location, 'slug': e.slug, 'done': e.done}

    context['event_list'] = event_list
    return render(request, 'events.html', context)


def event_detail(request, event_name_slug):
    form = EventRegisterForm()
    context = {}
    event = list(Event.objects.filter(slug=event_name_slug))
    #print(event)
    context['e_name'] = event[0].event_name
    context['e_location'] = event[0].location
    context['e_prize'] = event[0].prize
    context['e_description'] = event[0].description
    context['e_date'] = event[0].date
    context['slug'] = event_name_slug

    errors = None
    if request.method == "POST":
        print("POST")
        form = EventRegisterForm(request.POST)
        print(form.errors)

        if form.is_valid():
            print("IS VALID")
            obj = EventRegister.objects.create(
                fname=form.cleaned_data.get('fname'),
                lname=form.cleaned_data.get('lname'),
                email=form.cleaned_data.get('email'),
                phone=form.cleaned_data.get('phone'),
                athleteid=form.cleaned_data.get('athleteid'),
                city=form.cleaned_data.get('city'),
                state=form.cleaned_data.get('state'),
                teamname=form.cleaned_data.get('teamname'),
                event=event[0],
            )
            return HttpResponseRedirect('/events/')

        else:
            form = EventRegisterForm()

    if form.errors:
        print("ERRORS")
        errors = form.errors
    context['form'] = form
    return render(request, "event-detail.html", context)


def register(request):
    form = AthleteRegisterForm()
    errors = None
    l = len(list(AthleteRegister.objects.all()))
    athleteid = 'CF'
    n_zeros = 5 - len(str(l))
    athleteid = athleteid + ('0'*n_zeros) + str((l+1))

    if request.method == "POST":
        print("POST")
        form = AthleteRegisterForm(request.POST)

        print(form.errors)
        if form.is_valid():
            print("IS VALID")
            obj = AthleteRegister.objects.create(
                fname=form.cleaned_data.get('fname'),
                lname=form.cleaned_data.get('lname'),
                email=form.cleaned_data.get('email'),
                phone=form.cleaned_data.get('phone'),
                dob=form.cleaned_data.get('dob'),
                aadhaar=form.cleaned_data.get('aadhaar'),
                city=form.cleaned_data.get('city'),
                state=form.cleaned_data.get('state'),
                athleteid=athleteid,
            )
            subject = 'Registration Successful'
            plain_message = "Dear Athlete, \n\n" + "You have successfully registered with the Canoe Federation of India. Following is your Athlete ID : \n\n" + str(athleteid) + "\n\n Use this ID to participate in our future events.\n\n" + "Thank You\nCanoe Federation of India"

            email = EmailMessage(subject, plain_message, to=[form.cleaned_data.get('email')])
            email.send()
            return HttpResponseRedirect('/events/')
        else:
            form = AthleteRegisterForm()
    if form.errors:
        print("ERRORS")
        errors = form.errors

    context = {'form':form}
    return render(request, 'register.html', context)


def office_bearers(request):
    office = OfficeBearers.objects.all()
    official_list = {}
    context = {}
    for o in office:
        official_list[o.name] = {'role': o.role, 'phone': o.phone, 'email': o.email, 'image': o.image.url, 'link': o.social_media}

    context['official_list'] = official_list
    return render(request, 'office_bearers.html', context)
