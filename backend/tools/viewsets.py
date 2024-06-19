from http import HTTPStatus

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class SoloModelViewSet(GenericViewSet):
    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset.get_solo())
        data = serializer.data
        return Response(data=data, status=HTTPStatus.OK)
