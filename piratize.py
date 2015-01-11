from piratize_translate import *

class PartyRepelledError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        
class NoTreasureError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        continue
        
class WhatBeThisError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
            
class Ship:
    def __init__(self, size, treasure):
        self.size = size
        self.treasure = treasure
        
    def board(self, boarding_party):
        if not isinstance(boarding_party, BoardingParty):
            raise Exception("boarding party must be an instance of BoardingParty")
        if boarding_party.size <= self.size:
            raise PartyRepelledError(Exception)
        if self.treasure == 0:
            raise NoTreasureError("Ya! No treasure were found me 'earty!")

class ShipWreck:
    def __init__(self, ship):
        self.ship = ship
        
    def sink(self, ship):
        #sink the ship

