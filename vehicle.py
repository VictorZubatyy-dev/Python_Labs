"""
Main class, parent class.
Set the basic attributes for a vehicle.
"""
class Vehicle:
    def __init__(self, colour, make, cost):
        self._colour = colour
        self._make = make
        self.cost = cost

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, colour):
        self._colour = colour











