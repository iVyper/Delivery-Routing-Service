import csv
import datetime

from hashtable import HashTable
from package import Package
from truck import Truck
from functions import (distance_between_stops, address_to_id, delivery_status_update,
                       update_info, reset_packageAddress, update_address)

'''
Counts the number of packages listed in the package data CSV file.
Returns the total count which is used to dynamically size the hash table.
'''
def count_packages(package_manifest):
    with open(package_manifest) as file:
        reader = csv.reader(file)
        line_count = sum(1 for row in reader)
    return line_count

'''
Loads package data from a CSV file into the hash table.
Each row from the CSV is parsed into a Package object and inserted using the package ID.
'''
def load_package_data(package_manifest, hash_name):
    with open(package_manifest) as pd:
        package_data = csv.reader(pd)
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_zipcode = package[3]
            package_state = package[4]
            package_deadline = package[5]
            package_weight = package[6]
            package_notes = package[7]
            package_status = 'Hub'
            package_time_delivered = ''
            package_start_time = ''
            # Create a Package object with the parsed information.
            package = Package(package_id, package_address, package_city, package_zipcode,
                              package_state, package_deadline, package_weight,
                              package_notes, package_status, package_time_delivered, package_start_time)
            # Insert the package into the hash table.
            hash_name.insert(package_id, package)

# Get the number of packages from the CSV file.
package_count = count_packages('programdata/package_data.csv')
# Create a hash table sized based on the number of packages.
package_hashTable = HashTable(size=package_count)
# Load package data into the hash table.
load_package_data('programdata/package_data.csv', package_hashTable)

'''
Initialize Truck objects with their respective package lists, starting location, and departure times.
Each truck is represented with its capacity, distance traveled, speed, list of package IDs, location,
and time details.
'''
truck1 = Truck(16, 0, 18, [12, 13, 14, 15, 16, 19, 20, 25, 29, 30, 31, 34, 37, 40],
               '4001 South 700 East', '', datetime.timedelta(hours=8, minutes=00))
truck2 = Truck(16, 0, 18, [9, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 18, 36, 38],
               '4001 South 700 East', '', datetime.timedelta(hours=9, minutes=10))
truck3 = Truck(16, 0, 18, [17, 21, 22, 23, 24, 26, 27, 28, 32, 33, 35, 39],
               '4001 South 700 East', '', datetime.timedelta(hours=10, minutes=30))

'''
Delivers all packages assigned to a given truck.
For each truck, the function:
 - Marks packages as "En Route"
 - Finds the nearest package delivery location
 - Updates the truck and package information accordingly
'''
def deliver(truck, truck_number):
    undelivered_queue = []
    # Load all packages assigned to the truck into a working queue.
    for pid in truck.packages:
        package = package_hashTable.lookup(pid)
        package.status = 'Package is En Route'
        package.truck_number = truck_number  # Assign truck number to the package.
        undelivered_queue.append(package)

    # Continue delivering until all packages on the truck have been delivered.
    while len(undelivered_queue) > 0:
        nearest_distance = float('inf')
        for package in undelivered_queue:
            truck_location = truck.location
            package_delivery_location = package.address
            # Calculate the distance between the truck's current location and the package delivery address.
            distance_conv = distance_between_stops(address_to_id(truck_location),
                                                   address_to_id(package_delivery_location))
            # Identify the package with the nearest delivery location.
            if distance_conv <= nearest_distance:
                nearest_distance = distance_conv
                next_package = package
        # Update truck and package details based on the nearest package.
        update_info(truck, next_package, nearest_distance)
        # Remove the delivered package from the queue.
        undelivered_queue.remove(next_package)

# Deliver packages for each truck.
deliver(truck1, 1)
deliver(truck2, 2)
deliver(truck3, 3)

'''
The main program loop acts as a simple command-line GUI.
Users can:
 1. Retrieve complete trip information for all trucks.
 2. Check the status of a specific package at a given time.
 3. Check the status of all packages at a given time.
 4. Quit the application.
'''
class Main:
    runProgram = True
    while runProgram:
        print('\nWelcome to the WGUPS Routing Program')
        print('\n====================================')
        print('Main Menu:')
        print('\n(1) Retrieve Complete Trip Information')
        print('(2) Check a Package\'s Status at a Given Time')
        print('(3) Check the Status of All Packages at a Given Time')
        print('(4) Quit the Application')
        print('\n====================================')
        option = input('\nPlease Select an Option: ')
        
        if option == '1':
            # Print detailed trip information for each truck.
            print('\n====================================')
            print('Complete Trip Information')
            print('====================================')
            print('Truck 1 Info: ')
            print('Total Distance Traveled: ' + str(truck1.distance))
            print('Total Run Time: ' + str(truck1.delivery_time - truck1.departure_time))
            print('\nTruck 2 Info: ')
            print('Total Distance Traveled: ' + str(truck2.distance))
            print('Total Run Time: ' + str(truck2.delivery_time - truck2.departure_time))
            print('\nTruck 3 Info: ')
            print('Total Distance Traveled: ' + str(truck3.distance))
            print('Total Run Time: ' + str(truck3.delivery_time - truck3.departure_time))
            print('\nCombined Trucks Distance: ' + str(round(truck1.distance + truck2.distance + truck3.distance, 2)))
            print('Combined Delivery Time: ' + str((truck1.delivery_time - truck1.departure_time)
                                                  + (truck2.delivery_time - truck2.departure_time)
                                                  + (truck3.delivery_time - truck3.departure_time)))
        
        elif option == '2':
            # Check the status of a single package at a given time.
            try:
                print('\n')
                user_package = int(input(f'Please enter a valid Package ID (0 to {package_count - 1}): '))
                user_time = input('Please enter a time in HH:MM:SS format: ')
                if user_package < 0 or user_package >= package_count:
                    print(f'Invalid Package ID. Please try again.')
                else:
                    user_time_datetime = datetime.datetime.strptime(user_time, '%H:%M:%S')
                    user_time_delta = datetime.timedelta(hours=user_time_datetime.hour,
                                                         minutes=user_time_datetime.minute,
                                                         seconds=user_time_datetime.second)
                    print(f'\nPackage ID: {user_package} at Time: {user_time_delta}')
                    package_gui = package_hashTable.lookup(user_package)
                    
                    # Correct the package address if needed.
                    reset_packageAddress(package_gui, 9)
                    update_address(user_time_delta, package_gui)
                    
                    # Convert time strings to time deltas for comparison.
                    t = datetime.datetime.strptime(package_gui.time_delivered, '%H:%M:%S') if package_gui.time_delivered else datetime.datetime.min
                    time_delivered_delta = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
                    start_time_minutes = int(package_gui.start_time / datetime.timedelta(minutes=1)) if package_gui.start_time else 0
                    user_time_minutes = int(user_time_delta / datetime.timedelta(minutes=1))
                    time_delivered_minutes = int(time_delivered_delta / datetime.timedelta(minutes=1))
                    
                    # Update the package's delivery status based on the times.
                    delivery_status_update(start_time_minutes, user_time_minutes, time_delivered_minutes, package_gui)
                    # Print package information.
                    print('\n')
                    print(f'Package ID: {package_gui.package_id}')
                    print(f'Truck Number: {package_gui.truck_number}')
                    print(f'Weight: {package_gui.weight} | Deadline: {package_gui.deadline} | Expected Delivery: {package_gui.time_delivered}')
                    print(f'Current Status: {package_gui.status} | Time Loaded: {package_gui.start_time}')
                    print(f'Delivery Address: {package_gui.address}, {package_gui.city}, {package_gui.zipcode}, {package_gui.state}')
            except ValueError:
                print('Invalid input. Please enter a valid Package ID and time in HH:MM:SS format.')

        elif option == '3':
            # Check the status of all packages at a given time.
            try:
                user_time = input('Please enter the time in HH:MM:SS format: ')
                user_time_datetime = datetime.datetime.strptime(user_time, '%H:%M:%S')
                user_time_delta = datetime.timedelta(hours=user_time_datetime.hour,
                                                     minutes=user_time_datetime.minute,
                                                     seconds=user_time_datetime.second)
                print(f'\nStatus of all packages at {user_time}:')
                # Iterate over all possible package IDs.
                for i in range(1, len(package_hashTable.table) + 1):
                    package_gui = package_hashTable.lookup(i)
                    if package_gui is not None:
                        reset_packageAddress(package_gui, 9)
                        update_address(user_time_delta, package_gui)
                        
                        t = datetime.datetime.strptime(package_gui.time_delivered, '%H:%M:%S') if package_gui.time_delivered else datetime.datetime.min
                        time_delivered_delta = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
                        start_time_minutes = int(package_gui.start_time / datetime.timedelta(minutes=1)) if package_gui.start_time else 0
                        user_time_minutes = int(user_time_delta / datetime.timedelta(minutes=1))
                        time_delivered_minutes = int(time_delivered_delta / datetime.timedelta(minutes=1))
                        
                        delivery_status_update(start_time_minutes, user_time_minutes, time_delivered_minutes, package_gui)
                        # Print package details.
                        print('\n')
                        print(f'Package ID: {package_gui.package_id}')
                        print(f'Truck Number: {package_gui.truck_number}')
                        print(f'Weight: {package_gui.weight} | Deadline: {package_gui.deadline} | Expected Delivery: {package_gui.time_delivered}')
                        print(f'Current Status: {package_gui.status} | Time Loaded: {package_gui.start_time}')
                        print(f'Delivery Address: {package_gui.address}, {package_gui.city}, {package_gui.zipcode}, {package_gui.state}')
            except ValueError:
                print('Invalid input. Please enter a time in HH:MM:SS format.')
        
        elif option == '4':
            # Exit the application.
            print('The Application is now terminating. Goodbye!')
            runProgram = False
        
        else:
            print('Invalid option. Please try again.')
