from abc import ABC, abstractmethod

# ----------------------------------
# 1. Train Interface
# ----------------------------------
class TrainInterface(ABC):

    @abstractmethod
    def book_seat(self, class_type, count):
        pass

    @abstractmethod
    def cancel_seat(self, class_type, count):
        pass

    @abstractmethod
    def check_availability(self, class_type):
        pass


# ----------------------------------
# 2. Train Base Class
# ----------------------------------
class Train(TrainInterface):

    total_trains = 0

    def __init__(self, train_number, train_name, source, destination, depart, arrive, seats_dict):
        Train.total_trains += 1
        self.train_number = train_number
        self.train_name = train_name
        self.source_station = source
        self.destination_station = destination
        self.departure_time = depart
        self.arrival_time = arrive
        self.__available_seats = seats_dict   # Encapsulated seat data

    def book_seat(self, class_type, count):
        if self.__available_seats.get(class_type, 0) >= count:
            self.__available_seats[class_type] -= count
            print(count, "seats booked in", class_type)
            return "Confirmed"
        else:
            print("Seats not available! Ticket moved to Waitlist.")
            return "Waitlisted"

    def cancel_seat(self, class_type, count):
        self.__available_seats[class_type] += count
        print(count, "seats cancelled in", class_type)

    def check_availability(self, class_type):
        print("Available seats in", class_type, ":", self.__available_seats.get(class_type, 0))

    def show_train_info(self):
        print("\nTrain No:", self.train_number)
        print("Train Name:", self.train_name)
        print("Route:", self.source_station, "to", self.destination_station)
        print("Departure:", self.departure_time)
        print("Arrival:", self.arrival_time)

    @staticmethod
    def get_total_trains():
        return Train.total_trains

    @classmethod
    def update_total_trains(cls, value):
        cls.total_trains = value


# ----------------------------------
# 3. Express Train
# ----------------------------------
class ExpressTrain(Train):

    def __init__(self, *args, extra_charges):
        super().__init__(*args)
        self.extra_charges = extra_charges

    def get_extra_charges(self):
        print("Express Extra Charges:", self.extra_charges)


# ----------------------------------
# 4. SuperFast Train
# ----------------------------------
class SuperFastTrain(Train):

    def __init__(self, *args, superfast_charge):
        super().__init__(*args)
        self.superfast_charge = superfast_charge

    def calculate_superfast_charge(self):
        return self.superfast_charge


# ----------------------------------
# 5. Abstract Passenger
# ----------------------------------
class Passenger(ABC):

    total_passengers = 0

    def __init__(self, name, age, mobile):
        Passenger.total_passengers += 1
        self.__passenger_id = Passenger.total_passengers
        self.name = name
        self.age = age
        self.mobile_number = mobile

    def get_passenger_details(self):
        print("\nPassenger ID:", self.__passenger_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile:", self.mobile_number)

    @abstractmethod
    def book_ticket(self, train, class_type, seats):
        pass

    @abstractmethod
    def cancel_ticket(self, train, class_type, seats):
        pass

    @staticmethod
    def get_total_passengers():
        return Passenger.total_passengers


# ----------------------------------
# 6. General Passenger
# ----------------------------------
class GeneralPassenger(Passenger):

    def book_ticket(self, train, class_type, seats):
        status = train.book_seat(class_type, seats)
        ticket = Ticket(self, train, class_type, seats, status)
        ticket.calculate_fare()
        return ticket

    def cancel_ticket(self, train, class_type, seats):
        train.cancel_seat(class_type, seats)
        print("Ticket cancelled successfully!")


# ----------------------------------
# 7. Senior Citizen Passenger
# ----------------------------------
class SeniorCitizenPassenger(Passenger):

    def __init__(self, name, age, mobile):
        super().__init__(name, age, mobile)
        self.discount_rate = 30

    def book_ticket(self, train, class_type, seats):
        status = train.book_seat(class_type, seats)
        ticket = Ticket(self, train, class_type, seats, status, self.discount_rate)
        ticket.calculate_fare()
        return ticket

    def cancel_ticket(self, train, class_type, seats):
        train.cancel_seat(class_type, seats)
        print("Senior Citizen ticket cancelled.")

    def get_discount_info(self):
        print("Senior Citizen Discount:", self.discount_rate, "%")


# ----------------------------------
# 8. Ticket Class
# ----------------------------------
class Ticket:

    total_tickets = 0

    def __init__(self, passenger, train, class_type, seats, status, discount=0):
        Ticket.total_tickets += 1
        self.ticket_id = Ticket.total_tickets
        self.passenger = passenger
        self.train = train
        self.class_type = class_type
        self.seat_count = seats
        self.booking_status = status
        self.__total_fare = 0
        self.discount = discount

    def calculate_fare(self):
        base_fare = {
            "General": 200,
            "Sleeper": 500,
            "AC3": 900,
            "AC2": 1400
        }

        fare = base_fare.get(self.class_type, 300) * self.seat_count

        if isinstance(self.train, ExpressTrain):
            fare += self.train.extra_charges

        if isinstance(self.train, SuperFastTrain):
            fare += self.train.calculate_superfast_charge()

        discount_amount = fare * self.discount / 100
        self.__total_fare = fare - discount_amount

        print("\nTicket ID:", self.ticket_id)
        print("Passenger:", self.passenger.name)
        print("Train:", self.train.train_name)
        print("Class:", self.class_type)
        print("Seats:", self.seat_count)
        print("Status:", self.booking_status)
        print("Total Fare:", self.__total_fare)

    def update_status(self, status):
        self.booking_status = status
        print("Ticket status updated to:", status)

    @staticmethod
    def get_total_tickets():
        return Ticket.total_tickets


# ----------------------------------
# ✅ MAIN PROGRAM (DEMO)
# ----------------------------------

seats = {"General": 5, "Sleeper": 5, "AC3": 3, "AC2": 2}

t1 = ExpressTrain(10101, "Rajdhani Express", "Delhi", "Mumbai", "10 AM", "6 PM", seats, extra_charges=150)
t2 = SuperFastTrain(20202, "Duronto Express", "Delhi", "Kolkata", "8 AM", "5 PM", seats, superfast_charge=200)

t1.show_train_info()
t2.show_train_info()

p1 = GeneralPassenger("Ali", 22, "9998887777")
p2 = SeniorCitizenPassenger("Rohan", 65, "8887776666")

ticket1 = p1.book_ticket(t1, "Sleeper", 2)
ticket2 = p2.book_ticket(t2, "AC3", 2)

p2.get_discount_info()

print("\n--- Seat Availability ---")
t1.check_availability("Sleeper")
t2.check_availability("AC3")

print("\n--- TOTAL COUNTS ---")
print("Total Trains:", Train.get_total_trains())
print("Total Passengers:", Passenger.get_total_passengers())
print("Total Tickets:", Ticket.get_total_tickets())
