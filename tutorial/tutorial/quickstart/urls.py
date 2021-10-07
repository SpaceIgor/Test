from rest_framework import routers

from tutorial.tutorial.quickstart.views import *

router = routers.DefaultRouter()
router.register(r'person', PersonView)