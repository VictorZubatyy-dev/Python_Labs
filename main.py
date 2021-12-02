from vehicle import Vehicle
from bus import Bus
from train import Train
# run here to test inheritance functionality
# import all classes to access specific attributes created from those specific classes

# car inherits the vehicle attributes, it does not need any more attributes added, bus and train do
car1 = Vehicle("Blue", "Car", 20000)
print(car1.colour)
car1.colour = "Red"
print(car1.colour)






# bus1 = Bus("Red", "Bus", 100000, 101, "76a")
# print(bus1.bus_no)
# train1 = Train("Red", "Train", 20000, 200, "2001")
# print(train1.train_stop)













