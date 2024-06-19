from main_page.views import MainPageViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"main_page", MainPageViewSet, basename="main_page")
