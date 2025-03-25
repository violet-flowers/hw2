#Object oriented programming is a way to structure your code into reusable pieces called object
#Here a class for bicycles.
class bike(object):
    def __init__(self, bike_type, location):
        self.bike_type = bike_type #bike_type is an attribute of the bike that we are defining.
        self.location = location
        self.flat = False
        self.owner = None
    def ride_to(self, destination):
        self.location = destination
    def become_flat(self):
        self.flat = True
    def fix_flat(self):
        self.flat = False
    def __repr__(self): #tells Python how to print out an instance of your bike.
        return f"bike type: {self.bike_type} \nlocation: {self.location} \nflat? {self.flat}"
my_bike = bike("road_bike","uptown")
print(f"Our bike is a {my_bike.bike_type}")
my_bike.ride_to("by_water")
print(f"Our bike is at {my_bike.location}")
my_bike.become_flat()
print(f"Is our bike flat? {my_bike.flat}")
print(f"Current bike type {my_bike.bike_type}")

#Let's define another bike with the same class.
jons_bike = bike("mountain_bike","midcity")
print(jons_bike)