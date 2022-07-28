from rest_framework import serializers

from restaurantmenu.menu.models import Section, Item, Modifier


class SectionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class ItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ModifierModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = "__all__"


class ModifierMenuSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="name")

    class Meta:
        model = Modifier
        fields = ("id", "title")


class ItemMenuSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="name")
    modifiers = ModifierMenuSerializer(many=True)

    class Meta:
        model = Item
        fields = ("id", "title", "modifiers")


class MenuSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="name")
    items = ItemMenuSerializer(many=True)

    class Meta:
        model = Section
        fields = ("id", "title", "items")
