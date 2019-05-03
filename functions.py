import csv
import datetime

'''
Calculates the distance between two stops using data from a CSV file.
The CSV file (distance_table.csv) is assumed to contain a symmetric distance matrix.
Time Complexity: O(1) per call (file read overhead aside).
'''
def distance_between_stops(x, y):
    # Open and read the distance table from the CSV file.
    with open('programdata/distance_table.csv') as db:
        distance_between = list(csv.reader(db, delimiter=","))
    # Retrieve the distance from the table using indices.
    distance = distance_between[y][x]
    # If the entry is blank (data missing), try the opposite order.
    if distance == '':
        distance = distance_between[x][y]
    # Return the distance as a float.
    return float(distance)

'''
Converts an address to a unique ID by looking it up in a CSV file containing stop information.
The CSV file (stops.csv) is assumed to have an ID in column 0 and address details in column 2.
Time Complexity: O(N), where N is the number of stops.
'''
def address_to_id(address):
    # Open and read the stops data from CSV.
    with open('programdata/stops.csv') as stop:
        stop_data = list(csv.reader(stop, delimiter=","))
    # Loop through each stop and check if the address is contained in the address field.
    for stops in stop_data:
        if address in stops[2]:
            return int(stops[0])
    # If no matching address is found, return None (or consider raising an error).
    return None

'''
Updates the delivery status of a package based on the provided times.
Compares the package's start time, delivered time, and the user input time to set the status.
Time & Space Complexity: O(1)
'''
def delivery_status_update(start_time, user_time, time_delivered, package):
    # If the package has already left the hub.
    if start_time <= user_time:
        # If delivery time has passed, mark as delivered.
        if time_delivered <= user_time:
            package.status = 'Package Delivered'
        # If package is still on the way.
        elif time_delivered >= start_time:
            package.status = 'Package is En Route'
    else:
        # If the package hasn't left yet, it is at the hub.
        package.status = 'Package is at the Hub'

'''
Updates the truck's and package's information after a delivery move.
- Moves the truck's location to the package's delivery address.
- Increases the truck's total distance traveled.
- Updates the truck's delivery time based on the distance covered.
- Sets the package delivery time and marks it as delivered.
Time & Space Complexity: O(1)
'''
def update_info(truck, package, distance):
    # Update truck's location to the current package's address.
    truck.location = package.address
    # Add the traveled distance.
    truck.distance += distance
    # Calculate the time change based on truck speed.
    time_change = datetime.timedelta(hours=distance / truck.speed)
    truck.delivery_time += time_change
    # Update package delivery details.
    package.time_delivered = str(truck.delivery_time)
    package.status = 'DELIVERED AT:'
    package.start_time = truck.departure_time

'''
Resets a package's address to an incorrect (default) address if needed.
Typically used when a package's address is not yet corrected (e.g., before a certain time).
Time & Space Complexity: O(1)
'''
def reset_packageAddress(package, package_id):
    if package.package_id == package_id:
        package.address = '300 State St'
        package.city = 'Salt Lake City'
        package.state = 'UT'
        package.zipcode = '84103'

'''
Updates a package's address to the correct address if the current time is past a specified threshold.
Time & Space Complexity: O(1)
'''
def update_address(user_time, package):
    # Check if the current time is on or after 10:20 AM.
    if user_time >= datetime.timedelta(hours=10, minutes=20, seconds=00):
        package.address = '410 S State St.'
        package.city = 'Salt Lake City'
        package.state = 'UT'
        package.zipcode = '84111'
