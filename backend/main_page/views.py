from tools.viewsets import SoloModelViewSet

from main_page.models.main_page import MainPage
from main_page.serializers.main_page_serializer import MainPageSerializer


class MainPageViewSet(SoloModelViewSet):
    queryset = MainPage
    serializer_class = MainPageSerializer
