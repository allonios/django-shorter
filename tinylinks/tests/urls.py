"""
This ``urls.py`` is only used when running the tests via ``runtests.py``.
As you know, every app must be hooked into yout main ``urls.py`` so that
you can actually reach the app's views (provided it has any views, of course).

"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

from tinylinks.tests.views import TestFailedRedirectView, TestRedirectView


admin.autodiscover()


urlpatterns = [
    re_path(r'^redirect-test/', TestRedirectView.as_view()),
    re_path(r'^redirect-fail/', TestFailedRedirectView.as_view()),
    re_path(r'^administration/', admin.site.urls),
    re_path(r'^s/', include('tinylinks.urls')),
]
