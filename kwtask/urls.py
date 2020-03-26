# add custom url config to register our custom page

from django.conf.urls import url
from otree.urls import urlpatterns
from .pages import process_payments, payments_link

urlpatterns.append(url(r'^process_payments/(?P<session_code>[a-zA-Z0-9]*)/$', process_payments, name="process_payments"))
urlpatterns.append(url(r'^payments_link/', payments_link, name="payments_link"))