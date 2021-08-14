from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from django.http import HttpResponse

# General views go here.
def sanity_check(req):
    return HttpResponse("<h2>Sanity Check</h2>")

# API views go here
def main(req):
    pass
class DeckView(generics.CreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
class CardView(generics.creatAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer