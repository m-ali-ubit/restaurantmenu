from django.urls import path
from rest_framework.routers import DefaultRouter

from restaurantmenu.menu.views import (
    SectionViewSet,
    ItemViewSet,
    ModifierViewSet,
    MenuView,
)

router = DefaultRouter()
router.register(r"section", SectionViewSet, basename="section")
router.register(r"item", ItemViewSet, basename="item")
router.register(r"modifier", ModifierViewSet, basename="modifier")

urlpatterns = [
    path("menu/", MenuView.as_view(), name="menu"),
]

urlpatterns += router.urls
