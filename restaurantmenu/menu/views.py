from rest_framework import viewsets, views
from rest_framework.response import Response

from restaurantmenu.menu.models import Section, Item, Modifier
from restaurantmenu.menu.serializer import (
    SectionModelSerializer,
    ItemModelSerializer,
    ModifierModelSerializer,
    MenuSerializer,
)


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionModelSerializer
    queryset = Section.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemModelSerializer
    queryset = Item.objects.all()


class ModifierViewSet(viewsets.ModelViewSet):
    serializer_class = ModifierModelSerializer
    queryset = Modifier.objects.all()


class MenuView(views.APIView):

    def get(self, request):
        sections = Section.objects.all()
        data = MenuSerializer(sections, many=True).data
        return Response(data)
