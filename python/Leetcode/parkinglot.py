from enum import Enum
from abc import ABC, abstractmethod
import threading

# Enums and Constants: Here are the required enums, data types, and constants:
class VehicleType(Enum):
  CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5

class ParkingSpotType(Enum):
  HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5

class AccountStatus(Enum):
  ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6

class ParkingTicketStatus(Enum):
  ACTIVE, PAID, LOST = 1, 2, 3

class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country

class Person():
  def __init__(self, name, address, email, phone):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
# ------------------------------------------------------------------------------------
# ParkingSpot: Here is the definition of ParkingSpot and all of its children classes:
class ParkingSpot(ABC):
  def __init__(self, number, parking_spot_type):
    self.__number = number
    self.__free = True
    self.__vehicle = None
    self.__parking_spot_type = parking_spot_type

  def is_free(self):
    return self.__free

  def assign_vehicle(self, vehicle):
    self.__vehicle = vehicle
    free = False

  def remove_vehicle(self):
    self.__vehicle = None
    free = True

class CompactSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.COMPACT)


class LargeSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.LARGE)


class MotorbikeSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.MOTORBIKE)


class ElectricSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.ELECTRIC)

class HandicappedSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.HANDICAPPED)

# ------------------------------------------------------------------------------------
# Vehicle: Here is the definition for Vehicle and all of its child classes:

class Vehicle(ABC):
  def __init__(self, license_number, vehicle_type, ticket=None):
    self.__license_number = license_number
    self.__type = vehicle_type
    self.__ticket = ticket

  def assign_ticket(self, ticket):
    self.__ticket = ticket


class Car(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.CAR, ticket)


class Van(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.VAN, ticket)

class Truck(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.TRUCK, ticket)

class Montorcylce(Vehicle):
  def __init__(self, lincense_number, ticket=None):
    super().__init__(lincense_number, VehicleType.MOTORBIKE, ticket)

# Similarly we can define classes for Motorcycle and Electric vehicles
# ------------------------------------------------------------------------------------
# Account, Admin, and ParkingAttendant: These classes represent various people that interact with our system:
class Account:
  def __init__(self, user_name, password, person, status=AccountStatus.Active):
    self.__user_name = user_name
    self.__password = password
    self.__person = person
    self.__status = status

  def reset_password(self):
    None

class Admin(Account):
  def __init__(self, user_name, password, person, status=AccountStatus.Active):
    super().__init__(user_name, password, person, status)

  def add_parking_floor(self, floor):
    None

  def add_parking_spot(self, floor_name, spot):
    None

  def add_parking_display_board(self, floor_name, display_board):
    None

  def add_customer_info_panel(self, floor_name, info_panel):
    None

  def add_entrance_panel(self, entrance_panel):
    None

  def add_exit_panel(self, exit_panel):
    None

class ParkingAttendant(Account):
  def __init__(self, user_name, password, person, status=AccountStatus.Active):
    super().__init__(user_name, password, person, status)

  def process_ticket(self, ticket_number):
    None

# ------------------------------------------------------------------------------------
# ParkingLot: Our system will have only one object of this class. This can be enforced by using the Singleton pattern. In software engineering, 
# the singleton pattern is a software design pattern that restricts the instantiation of a class to only one object.

class ParkingLot:
  # singleton ParkingLot to ensure only one object of ParkingLot in the system,
  # all entrance panels will use this object to create new parking ticket: get_new_parking_ticket(),
  # similarly exit panels will also use this object to close parking tickets
  instance = None

  class __OnlyOne:
    def __init__(self, name, address):
      # 1. initialize variables: read name, address and parking_rate from database
      # 2. initialize parking floors: read the parking floor map from database,
      #    this map should tell how many parking spots are there on each floor. This
      #    should also initialize max spot counts too.
      # 3. initialize parking spot counts by reading all active tickets from database
      # 4. initialize entrance and exit panels: read from database

      self.__name = name
      self.__address = address
      self.__parking_rate = ParkingRate()

      self.__compact_spot_count = 0
      self.__large_spot_count = 0
      self.__motorbike_spot_count = 0
      self.__electric_spot_count = 0
      self.__max_compact_count = 0
      self.__max_large_count = 0
      self.__max_motorbike_count = 0
      self.__max_electric_count = 0

      self.__entrance_panels = {}
      self.__exit_panels = {}
      self.__parking_floors = {}

      # all active parking tickets, identified by their ticket_number
      self.__active_tickets = {}

      self.__lock = threading.Lock()

  def __init__(self, name, address):
    if not ParkingLot.instance:
      ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
    else:
      ParkingLot.instance.__name = name
      ParkingLot.instance.__address = address

  def __getattr__(self, name):
    return getattr(self.instance, name)

  def get_new_parking_ticket(self, vehicle):
    if self.is_full(vehicle.get_type()):
      raise Exception('Parking full!')
    # synchronizing to allow multiple entrances panels to issue a new
    # parking ticket without interfering with each other
    self.__lock.acquire()
    ticket = ParkingTicketStatus()
    vehicle.assign_ticket(ticket)
    ### DB가 있을 경우...
    ticket.save_in_DB()
    # if the ticket is successfully saved in the database, we can increment the parking spot count
    self.__increment_spot_count(vehicle.get_type())
    self.__active_tickets.put(ticket.get_ticket_number(), ticket)
    self.__lock.release()
    ###
    return ticket

  def is_full(self, type):
    # trucks and vans can only be parked in LargeSpot
    if type == VehicleType.Truck or type == VehicleType.Van:
      return self.__large_spot_count >= self.__max_large_count

    # motorbikes can only be parked at motorbike spots
    if type == VehicleType.Motorbike:
      return self.__motorbike_spot_count >= self.__max_motorbike_count

    # cars can be parked at compact or large spots
    if type == VehicleType.Car:
      return (self.__compact_spot_count + self.__large_spot_count) >= (self.__max_compact_count + self.__max_large_count)

    # electric car can be parked at compact, large or electric spots
    return (self.__compact_spot_count + self.__large_spot_count + self.__electric_spot_count) >= (self.__max_compact_count + self.__max_large_count
                                                                                                  + self.__max_electric_count)

  # increment the parking spot count based on the vehicle type
  def increment_spot_count(self, type):
    if type == VehicleType.Truck or type == VehicleType.Van:
      large_spot_count += 1
    elif type == VehicleType.Motorbike:
      motorbike_spot_count += 1
    elif type == VehicleType.Car:
      if self.__compact_spot_count < self.__max_compact_count:
        compact_spot_count += 1
      else:
        large_spot_count += 1
    else:  # electric car
      if self.__electric_spot_count < self.__max_electric_count:
        electric_spot_count += 1
      elif self.__compact_spot_count < self.__max_compact_count:
        compact_spot_count += 1
      else:
        large_spot_count += 1

  def is_full(self):
    for key in self.__parking_floors:
      if not self.__parking_floors.get(key).is_full():
        return False
    return True

  def add_parking_floor(self, floor):
    # store in database
    None

  def add_entrance_panel(self, entrance_panel):
    # store in database
    None

  def add_exit_panel(self,  exit_panel):
    # store in database
    None
    
# ------------------------------------------------------------------------------------
# ParkingDisplayBoard: This class encapsulates a parking display board:
class ParkingDisplayBoard:
  def __init__(self, id):
    self.__id = id
    self.__handicapped_free_spot = None
    self.__compact_free_spot = None
    self.__large_free_spot = None
    self.__motorbike_free_spot = None
    self.__electric_free_spot = None

  def show_empty_spot_number(self):
    message = ""
    if self.__handicapped_free_spot.is_free():
      message += "Free Handicapped: " + self.__handicapped_free_spot.get_number()
    else:
      message += "Handicapped is full"
    message += "\n"

    if self.__compact_free_spot.is_free():
      message += "Free Compact: " + self.__compact_free_spot.get_number()
    else:
      message += "Compact is full"
    message += "\n"

    if self.__large_free_spot.is_free():
      message += "Free Large: " + self.__large_free_spot.get_number()
    else:
      message += "Large is full"
    message += "\n"

    if self.__motorbike_free_spot.is_free():
      message += "Free Motorbike: " + self.__motorbike_free_spot.get_number()
    else:
      message += "Motorbike is full"
    message += "\n"

    if self.__electric_free_spot.is_free():
      message += "Free Electric: " + self.__electric_free_spot.get_number()
    else:
      message += "Electric is full"

    print(message)