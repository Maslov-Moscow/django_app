from main_page.models.main_page import MainPage
from rest_framework.serializers import ModelSerializer


class MainPageSerializer(ModelSerializer):
    class Meta:
        model = MainPage
        exclude = ("id",)
