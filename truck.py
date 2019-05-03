'''
Represents a delivery truck used to deliver packages.
The Truck object tracks capacity, current distance traveled, speed,
a list of package IDs assigned for delivery, current location, delivery time, and departure time.
'''
class Truck:
    def __init__(self, capacity, distance, speed, packages, location, delivery_time, departure_time):
        self.capacity = capacity              # Maximum number of packages the truck can carry
        self.distance = distance              # Total distance traveled so far
        self.speed = speed                    # Average speed of the truck (used for time calculation)
        self.packages = packages              # List of package IDs assigned to the truck
        self.location = location              # Current location of the truck
        self.delivery_time = departure_time   # Current delivery time (initially set to departure time)
        self.departure_time = departure_time  # Time the truck left the hub

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (
            self.capacity, self.distance, self.speed, self.packages, self.location,
            self.delivery_time, self.departure_time)
