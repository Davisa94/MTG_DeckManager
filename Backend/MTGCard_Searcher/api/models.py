from django.db import models

# Create your models here.

##################################################
# A relational Model for storing card to deck relations
# Author: Austin Benitez
##################################################
class CardToDeck(models.Model):
    deck_id = models.ForeignKey("Deck", related_name="card_to_deck", on_delete=models.CASCADE)
    card_id = models.ForeignKey("Card", related_name="card_to_deck", on_delete=models.CASCADE)
    quantity = models.IntegerField

##################################################
# An info table containing everything about the
# Card given from the API used as a cache
# Author: Austin Benitez
##################################################
class Card(models.Model):
    id = models.AutoField(primary_key=True)
    multiverseid = models.IntegerField(unique=True) # Used to fetch the card from the API
    name = models.CharField(max_length=145)

##################################################
# Holds all information needed to display a users 
# curated list of cards and related information
# Author: Austin Benitez
##################################################
class Deck(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=145)

