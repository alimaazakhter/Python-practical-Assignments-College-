from abc import ABC, abstractmethod

# 1. Interface for Patients

class PatientInterface(ABC):

    @abstractmethod
    def add_record(self, record):
        pass

    @abstractmethod
    def get_records(self):
        pass

    @abstractmethod
    def update_contact(self, new_number):
        pass


# 2. Patient Base Class

class Patient(PatientInterface):

    total_patients = 0   # Static Variable to track patients

    def __init__(self, name, age, mobile, patient_type):
        Patient.total_patients += 1

        self.__patient_id = Patient.total_patients   # Private ID
        self.name = name
        self.age = age
        self.__mobile_number = mobile                # Private Mobile
        self.patient_type = patient_type
        self.__medical_history = []                  # Private Medical Records

    def add_record(self, record):
        self.__medical_history.append(record)
        print("Medical record added!")

    def get_records(self):
        print("Medical History:", self.__medical_history)

    def update_contact(self, new_number):
        self.__mobile_number = new_number
        print("Contact updated!")

    def show_patient_info(self):
        print("\nPatient ID:", self.__patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile:", self.__mobile_number)
        print("Type:", self.patient_type)

    @staticmethod
    def get_total_patients():
        return Patient.total_patients

    @classmethod
    def update_total_patients(cls, value):
        cls.total_patients = value


# 3. Outpatient Class

class Outpatient(Patient):

    def __init__(self, name, age, mobile):
        super().__init__(name, age, mobile, "Outpatient")
        self.appointment_date = None

    def schedule_appointment(self, date):
        self.appointment_date = date
        print("Appointment scheduled on:", date)

# 4. Inpatient Class

class Inpatient(Patient):

    def __init__(self, name, age, mobile, admission_date):
        super().__init__(name, age, mobile, "Inpatient")
        self.room_number = None
        self.admission_date = admission_date
        self.discharge_date = None

    def assign_room(self, room_number):
        self.room_number = room_number
        print("Room assigned:", room_number)

    def discharge(self, date):
        self.discharge_date = date
        print("Patient discharged on:", date)


# 5. Abstract Doctor Class

class Doctor(ABC):

    total_doctors = 0

    def __init__(self):
        Doctor.total_doctors += 1

    @abstractmethod
    def diagnose(self, patient):
        pass

    @abstractmethod
    def prescribe(self, patient, prescription):
        pass

    @staticmethod
    def get_total_doctors():
        return Doctor.total_doctors


# 6. Specialist Doctor Class

class SpecialistDoctor(Doctor):

    def __init__(self, specialization):
        super().__init__()
        self.specialization = specialization

    # Polymorphism
    def diagnose(self, patient):
        diagnosis = "Diagnosed by " + self.specialization
        patient.add_record(diagnosis)
        print("Diagnosis done by", self.specialization)

    def prescribe(self, patient, prescription):
        patient.add_record("Prescription: " + prescription)
        print("Prescription added!")


# MAIN PROGRAM

print("\n--- OUTPATIENT ---")
op = Outpatient("Ali", 22, "9876543210")
op.show_patient_info()
op.schedule_appointment("15 July 2025")
op.add_record("Fever and Cold")
op.get_records()

print("\n--- INPATIENT ---")
ip = Inpatient("Rohan", 30, "9998887777", "10 July 2025")
ip.show_patient_info()
ip.assign_room(205)
ip.add_record("Appendix Surgery")
ip.discharge("14 July 2025")
ip.get_records()

print("\n--- SPECIALIST DOCTOR ---")
doc1 = SpecialistDoctor("Cardiologist")
doc1.diagnose(op)
doc1.prescribe(op, "Heart Medicine")

doc2 = SpecialistDoctor("Neurologist")
doc2.diagnose(ip)
doc2.prescribe(ip, "Neuro Tablets")

print("\n--- FINAL MEDICAL RECORDS ---")
op.get_records()
ip.get_records()

print("\nTotal Patients Registered:", Patient.get_total_patients())
print("Total Doctors Available:", Doctor.get_total_doctors())
