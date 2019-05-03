'''
Represents a package with detailed delivery information.
Each package has a unique ID, address information, delivery deadline, weight, notes,
and status information (including delivery time, time loaded, and associated truck number).
'''
class Package:
    def __init__(self, package_id, address, city, zipcode, state, deadline, weight, notes, status, time_delivered, start_time, truck_number=None):
        self.package_id = package_id      # Unique package identifier
        self.address = address            # Delivery address
        self.city = city                  # Delivery city
        self.zipcode = zipcode            # Delivery zip code
        self.state = state                # Delivery state
        self.deadline = deadline          # Delivery deadline
        self.weight = weight              # Package weight
        self.notes = notes                # Special instructions or notes
        self.status = status              # Current status (e.g., 'Hub', 'En Route', 'Delivered')
        self.time_delivered = time_delivered  # Time when the package was delivered
        self.start_time = start_time      # Time when the package left the hub
        self.truck_number = truck_number  # Assigned truck number (if any)

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.package_id, self.address, self.city, self.zipcode, self.state,
            self.deadline, self.weight, self.notes, self.status, self.time_delivered,
            self.start_time, self.truck_number)
