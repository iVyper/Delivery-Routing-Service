# WGUPS Routing Program

This project is a Python-based simulation of a package delivery routing system for WGUPS. The program uses several modules to simulate package management, truck routing, and delivery status updates based on real-world data files (CSV). It also includes a simple command-line interface (GUI) for interacting with the system.

## Project Structure

- **functions.py**  
  Contains helper functions that perform key operations such as:
  - Calculating the distance between stops using a CSV distance table.
  - Converting addresses to unique IDs.
  - Updating package delivery status.
  - Updating truck and package information during delivery.
  - Resetting and updating package addresses based on time.

- **hashtable.py**  
  Implements a simple hash table for storing and retrieving `Package` objects.
  The hash table is dynamically sized based on the number of packages and uses basic chaining to handle collisions.

- **package.py**  
  Defines the `Package` class that holds detailed package information including address, deadline, weight, notes, and delivery status.

- **truck.py**  
  Defines the `Truck` class representing delivery trucks. Each truck has attributes such as capacity, speed, package list, current location, delivery time, and departure time.

- **main.py**  
  The main entry point of the application. This file:
  - Loads package data from CSV files into a hash table.
  - Initializes Truck objects with assigned package IDs.
  - Simulates the delivery process by finding the nearest package delivery locations and updating truck and package information.
  - Provides a command-line interface for:
    - Viewing complete trip information.
    - Checking the status of individual packages at a given time.
    - Checking the status of all packages at a given time.

- **CSV Data Files (not shown):**
  - `distance_table.csv`: Contains a matrix of distances between stops.
  - `package_data.csv`: Contains package details (ID, address, deadline, etc.).
  - `stops.csv`: Contains stop information used to map addresses to IDs.

## How to Run

1. **Clone the Repository or Download the Files:**

   ```bash
   git clone https://github.com/ivyper/Delivery-Routing-Service.git
   cd Delivery-Routing-Service

2. **Ensure the CSV Data Files are in the programdata Directory:**

    The project expects the following files to be present in a folder named `programdata`:
    - `distance_table.csv`
    - `package_data.csv`
    - `stops.csv`

3. **Run the Program:**

    Use Python 3 to run the main file:
    ```bash
    python main.py

4. **Follow the On-Screen Prompts:**

    The program provides a simple menu to:
    - Retrieve complete trip information.
    - Check a package's status at a given time.
    - Check the status of all packages at a given time.
    - Quit the application.

## Dependencies

- Python 3.x
- Standard Python libraries: `csv`, `datetime`

## License

This project is open-source and available under the MIT License.