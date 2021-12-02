from vehicle import Vehicle
# import parent class to inherit


class Bus(Vehicle):
    """
    Added bus stop and bus number attributes to this class.
    The parent class handles the colour, make and cost.
    """
    def __init__(self, colour, make, cost, bus_no, bus_stop):
        super().__init__(colour, make, cost)
        self.bus_no = bus_no
        self.bus_stop = bus_stop






