from rest_framework import routers
from tutorial.tutorial.quickstart.views import *
from django.views.decorators.cache import cache_page

router = routers.DefaultRouter()
cache_page(80)(router.register(r'person', PersonView))