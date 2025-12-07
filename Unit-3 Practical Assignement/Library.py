from abc import ABC, abstractmethod

# 1. Item Interface

class ItemInterface(ABC):

    @abstractmethod
    def borrow_item(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

    @abstractmethod
    def check_availability(self):
        pass


# 2. LibraryItem Base Class

class LibraryItem(ItemInterface):

    total_items = 0   # Static Variable to track total items

    def __init__(self, title, author, category, copies):
        LibraryItem.total_items += 1
        self.__item_id = LibraryItem.total_items   # Private ID
        self.title = title
        self.author = author
        self.category = category
        self.__available_copies = copies           # Private copies

    def borrow_item(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print("Item borrowed successfully!")
            return True
        else:
            print("No copies available!")
            return False

    def return_item(self):
        self.__available_copies += 1
        print("Item returned successfully!")

    def check_availability(self):
        print("Available Copies:", self.__available_copies)

    def show_item_info(self):
        print("\nItem ID:", self.__item_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Category:", self.category)

    @staticmethod
    def get_total_items():
        return LibraryItem.total_items

    @classmethod
    def update_total_items(cls, value):
        cls.total_items = value


# 3. Book Class

class Book(LibraryItem):

    def __init__(self, title, author, copies, isbn):
        super().__init__(title, author, "Book", copies)
        self.isbn = isbn

    def get_book_info(self):
        self.show_item_info()
        print("ISBN:", self.isbn)


# 4. ReferenceBook Class

class ReferenceBook(LibraryItem):

    def __init__(self, title, author, copies):
        super().__init__(title, author, "Reference", copies)
        self.reference_only = True

    # Polymorphism (Borrow not allowed)
    def borrow_item(self):
        print("Reference books cannot be borrowed!")


# 5. Abstract Member Class

class Member(ABC):

    total_members = 0

    def __init__(self, name):
        Member.total_members += 1
        self.name = name
        self.borrowed_items = []

    @abstractmethod
    def borrow(self, item):
        pass

    @abstractmethod
    def return_item(self, item):
        pass

    @abstractmethod
    def get_borrow_limit(self):
        pass

    @staticmethod
    def get_total_members():
        return Member.total_members

# 6. StudentMember Class

class StudentMember(Member):

    def __init__(self, name):
        super().__init__(name)
        self.borrow_limit = 2

    def borrow(self, item):
        if len(self.borrowed_items) < self.borrow_limit:
            if item.borrow_item():
                self.borrowed_items.append(item)
                print(self.name, "borrowed an item!")
        else:
            print("Student borrow limit reached!")

    def return_item(self, item):
        if item in self.borrowed_items:
            item.return_item()
            self.borrowed_items.remove(item)
            print(self.name, "returned the item.")

    def get_borrow_limit(self):
        print("Student Borrow Limit:", self.borrow_limit)


# 7. FacultyMember Class

class FacultyMember(Member):

    def __init__(self, name):
        super().__init__(name)
        self.borrow_limit = 5

    def borrow(self, item):
        if len(self.borrowed_items) < self.borrow_limit:
            if item.borrow_item():
                self.borrowed_items.append(item)
                print(self.name, "borrowed an item!")
        else:
            print("Faculty borrow limit reached!")

    def return_item(self, item):
        if item in self.borrowed_items:
            item.return_item()
            self.borrowed_items.remove(item)
            print(self.name, "returned the item.")

    def get_borrow_limit(self):
        print("Faculty Borrow Limit:", self.borrow_limit)


# MAIN PROGRAM


print("\n--- LIBRARY ITEMS ---")
b1 = Book("Python Programming", "Guido", 3, "ISBN-111")
b2 = Book("Data Science", "Jake", 2, "ISBN-222")
r1 = ReferenceBook("Encyclopedia", "Britannica", 1)

b1.get_book_info()
b2.get_book_info()
r1.show_item_info()

print("\n--- MEMBERS ---")
s1 = StudentMember("Ali")
f1 = FacultyMember("Rohan")

s1.get_borrow_limit()
f1.get_borrow_limit()

print("\n--- BORROW OPERATIONS ---")
s1.borrow(b1)
s1.borrow(b2)
s1.borrow(b1)  

f1.borrow(b1)
f1.borrow(r1)   

print("\n--- RETURN OPERATIONS ---")
s1.return_item(b1)
f1.return_item(b1)

print("\n--- AVAILABILITY CHECK ---")
b1.check_availability()
b2.check_availability()

print("\n--- TOTAL COUNTS ---")
print("Total Library Items:", LibraryItem.get_total_items())
print("Total Members:", Member.get_total_members())
