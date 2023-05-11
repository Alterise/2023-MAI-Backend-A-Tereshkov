from rest_framework import serializers
from .models import Item, Character, Profile


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'rarity', 'price')


class CharacterSerializer(serializers.ModelSerializer):
    inventory = ItemSerializer(read_only=True)

    class Meta:
        model = Character
        fields = ('id', 'name', 'class_name', 'lvl', 'inventory')


class ProfileSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('id', 'username', 'hours_played', 'characters_count', 'characters')
