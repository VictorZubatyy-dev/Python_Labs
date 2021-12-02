from vehicle import Vehicle
# import parent class to inherit


class Train(Vehicle):
    """
        Same as bus class, except have train fields
        Inherits from Vehicle parent class and just add attributes train no and number.
        """
    def __init__(self, colour, make, cost, train_no, train_stop):
        super().__init__(colour, make, cost)
        self.train_no = train_no
        self.train_stop = train_stop

