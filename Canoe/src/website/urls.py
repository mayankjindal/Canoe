from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import index, gallery, events, event_detail, register, office_bearers

app_name='website'

urlpatterns = [
                  url(r'^$', index, name='index'),
                  url(r'^gallery/$', gallery, name='gallery'),
                  url(r'^events/$', events, name='events'),
                  url(r'^register/$', register, name='register'),
                  url(r'^event_detail/(?P<event_name_slug>[\w\-]+)/$', event_detail, name='event-detail'),
                  url(r'^office_bearers/$', office_bearers, name='office_bearers'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
