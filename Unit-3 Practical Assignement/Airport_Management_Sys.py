from abc import ABC, abstractmethod


# 1. Flight Interface

class FlightInterface(ABC):

    @abstractmethod
    def book_seat(self, quantity):
        pass

    @abstractmethod
    def cancel_seat(self, quantity):
        pass

    @abstractmethod
    def check_availability(self):
        pass



# 2. Flight Base Class

class Flight(FlightInterface):

    total_flights = 0

    def __init__(self, airline, source, destination, depart, arrive, seats):
        Flight.total_flights += 1
        self.__flight_id = Flight.total_flights
        self.airline = airline
        self.source = source
        self.destination = destination
        self.departure_time = depart
        self.arrival_time = arrive
        self.__available_seats = seats   # Encapsulated

    def book_seat(self, quantity):
        if quantity <= self.__available_seats:
            self.__available_seats -= quantity
            print("Seats booked:", quantity)
            return True
        else:
            print("Not enough seats available!")
            return False

    def cancel_seat(self, quantity):
        self.__available_seats += quantity
        print("Seats cancelled:", quantity)

    def check_availability(self):
        print("Available Seats:", self.__available_seats)

    def show_flight_info(self):
        print("\nFlight ID:", self.__flight_id)
        print("Airline:", self.airline)
        print("Route:", self.source, "to", self.destination)
        print("Departure:", self.departure_time)
        print("Arrival:", self.arrival_time)

    @staticmethod
    def get_total_flights():
        return Flight.total_flights

    @classmethod
    def update_total_flights(cls, value):
        cls.total_flights = value



# 3. Domestic Flight

class DomesticFlight(Flight):

    def __init__(self, airline, source, destination, depart, arrive, seats, baggage):
        super().__init__(airline, source, destination, depart, arrive, seats)
        self.baggage_allowance = baggage

    def get_baggage_info(self):
        print("Baggage Allowance:", self.baggage_allowance, "kg")



# 4. International Flight

class InternationalFlight(Flight):

    def __init__(self, airline, source, destination, depart, arrive, seats):
        super().__init__(airline, source, destination, depart, arrive, seats)
        self.passport_required = True
        self.visa_required = True

    def verify_documents(self):
        print("Passport & Visa verified successfully!")


# 5. Abstract Passenger Class

class Passenger(ABC):

    total_passengers = 0

    def __init__(self, name):
        Passenger.total_passengers += 1
        self.__passenger_id = Passenger.total_passengers
        self.name = name

    def get_passenger_details(self):
        print("\nPassenger ID:", self.__passenger_id)
        print("Name:", self.name)

    @abstractmethod
    def book_flight(self, flight, seats):
        pass

    @abstractmethod
    def cancel_booking(self, flight, seats):
        pass

    @abstractmethod
    def check_in(self):
        pass

    @staticmethod
    def get_total_passengers():
        return Passenger.total_passengers


# 6. Regular Passenger

class RegularPassenger(Passenger):

    def __init__(self, name):
        super().__init__(name)
        self.frequent_flyer_points = 0

    def book_flight(self, flight, seats):
        if flight.book_seat(seats):
            self.frequent_flyer_points += 10
            print("Flight booked! Points earned.")

    def cancel_booking(self, flight, seats):
        flight.cancel_seat(seats)
        print("Booking cancelled!")

    def check_in(self):
        print("Regular check-in completed!")

    def redeem_points(self):
        print("Redeemed", self.frequent_flyer_points, "points")
        self.frequent_flyer_points = 0


# 7. VIP Passenger

class VIPPassenger(Passenger):

    def __init__(self, name):
        super().__init__(name)
        self.lounge_access = True
        self.priority_boarding = True

    def book_flight(self, flight, seats):
        if flight.book_seat(seats):
            print("VIP booking confirmed with privileges!")

    def cancel_booking(self, flight, seats):
        flight.cancel_seat(seats)
        print("VIP booking cancelled!")

    # Polymorphism (Priority Check-in)
    def check_in(self):
        print("VIP Priority Check-in Completed!")

    def access_lounge(self):
        if self.lounge_access:
            print("Welcome to VIP Lounge!")


# 8. Staff Class

class Staff:

    total_staff = 0

    def __init__(self, name, role):
        Staff.total_staff += 1
        self.__staff_id = Staff.total_staff
        self.name = name
        self.__role = role

    def perform_duty(self):
        print(self.name, "is performing duty as", self.__role)

    def update_role(self, new_role):
        self.__role = new_role
        print("Role updated to:", new_role)

    @staticmethod
    def get_total_staff():
        return Staff.total_staff


# MAIN PROGRAM

print("\n--- FLIGHTS ---")
f1 = DomesticFlight("IndiGo", "Delhi", "Mumbai", "10 AM", "12 PM", 100, 15)
f2 = InternationalFlight("Emirates", "Mumbai", "Dubai", "3 PM", "7 PM", 80)

f1.show_flight_info()
f1.get_baggage_info()
f2.show_flight_info()
f2.verify_documents()

print("\n--- PASSENGERS ---")
p1 = RegularPassenger("Ali")
p2 = VIPPassenger("Rohan")

p1.book_flight(f1, 2)
p2.book_flight(f2, 1)

p1.check_in()
p2.check_in()
p2.access_lounge()

print("\n--- STAFF ---")
s1 = Staff("Amit", "Security")
s2 = Staff("Neha", "Boarding")

s1.perform_duty()
s2.perform_duty()

print("\n--- AVAILABILITY ---")
f1.check_availability()
f2.check_availability()

print("\n--- TOTAL COUNTS ---")
print("Total Flights:", Flight.get_total_flights())
print("Total Passengers:", Passenger.get_total_passengers())
print("Total Staff:", Staff.get_total_staff())
