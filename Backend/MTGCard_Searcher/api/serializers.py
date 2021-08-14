from .models import *
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name')

class CardToDeckSerializer(serializers.ModelSerializer):
    card_info = CardSerializer()
    class Meta:
        model = CardToDeck
        fields = ('deck_id', 'card_id', 'card_info')
        depth = 1

# Serializer for Deck that grabs the nested model references
class DeckSerializer(serializers.ModelSerializer):
    # if not intended to use bulk action it's better to keep may fields as read only
    cards = CardToDeckSerializer(many=True)
    class Meta:
        model = Deck
        depth = 0
        fields = ('name', 'cards')
    def create(self, validated_data):
        print("THE DATA RECIEVED WAS: ", validated_data)
        cards_data = validated_data.pop('cards')
        deck = Deck.objects.create(**validated_data)
        for card in cards_data:
            Card.objects.create(id=id, name=name)
        return deck