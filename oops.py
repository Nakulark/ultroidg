class Car: #syntax first:= class (jo same rehga) Second:= Class name (jo Class banani hai uska naam & first charecter capital rehga)
    def __init__(self,brand,model):#isko constructor kehte hai sabse pehle aayga iska name change nhi kar skte| isme self ke aage jo hai usko parameters kehte hai 
        self.brand=brand # attribute
        self.model=model # attribute

    def full_name(self): # isko method kehte hai class ka
        return f"{self.brand} {self.model}"

my_car=Car("Toyota","Corolla")# yeh object hai class ko access aur parameter mai values fill karne mai kaam aata
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car=Car("Tata","Safari")
print(my_new_car.brand)

#inhertiance
#  
# Kya hota hai Inheritance?
#    Inheritance matlab ek class doosri class ki property aur methods ko use kar sakti hai bina dobara likhe.
#    Ye concept kaafi similar hai jaise beta apne papa ki cheeze inherit karta hai.  

'''Types of Classes:
    1) Parent class (Base class / Superclass) → jiske paas original features hain.(jo ki hamare case mai Car class hai)
    2) Child class (Derived class / Subclass) → jo parent class se features inherit karti hai (ElectricCar hai isme)'''

class ElectreicCar(Car):# syntax:--> first:- class (jo ki same rehga) | Second:-class name ()
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

my_tesla=ElectreicCar("Tesla","Model S","85kwh")
print(my_tesla.full_name())

'''#--> conclusion
        ==> Car ek parent class hai jisme brand aur model ka data hai.
        ==> ElectricCar child class hai jo Car se inherit kar rahi hai.
        ==> super().__init__() ka use hota hai parent class ka constructor call karne ke liye.
        ==> ElectricCar class ne apna ek extra function banaya: battery_size

 Inheritance ka matlab hai ek class doosri class ke features reuse kar sakti hai. Ye code ko short, clean aur organized banata hai.'''

# Multilevel Inheritance
# Ek class kisi class se inherit karti hai, aur fir usse ek aur class inherit karti hai. (Grandfather → Father → Child)

class Grandfather:
    def property(self):
        print("Grandfather ki property")

class Father(Grandfather):
    def car(self):
        print("Father ki car")

class Child(Father):
    def bike(self):
        print("Child ki bike")

c = Child()
c.property()  # Grandfather
c.car()       # Father
c.bike()      # Child

# Multiple Inheritance
#    Ek child class, multiple parent classes se inherit karti hai.

class Father:
    def house(self):
        print("Father ka house")

class Mother:
    def jewelry(self):
        print("Mother ki jewelry")

class Child(Father, Mother):
    def bike(self):
        print("Child ki bike")

c = Child()
c.house()
c.jewelry()
c.bike()

#. Hierarchical Inheritance
#    Ek hi parent class ko multiple child classes inherit karte hain.

class Parent:
    def house(self):
        print("Parent ka house")

class Child1(Parent):
    def car(self):
        print("Child1 ki car")

class Child2(Parent):
    def bike(self):
        print("Child2 ki bike")

c1 = Child1()
c2 = Child2()

c1.house()
c1.car()

c2.house()
c2.bike()

# What is Encapsulation?
'''
--> Definition:
    Encapsulation matlab data (variables) aur methods (functions) ko ek single unit (class) me bandh kar dena.
    Saath hi data ko protect karna from direct access (jaise private cheeze hoti hain).

Yani:
    Kisi class ke variables ko direct access na kar sake
    Sirf functions ke through hi access ho'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # private variable

    def get_marks(self):  # Getter
        return self.__marks

    def set_marks(self, new_marks):  # Setter
        if new_marks >= 0 and new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks")

# Create object
s1 = Student("Rahul", 85)

# Accessing private variable directly (not recommended)
# print(s1.__marks)   ❌ Error dega

# Use getter and setter
print(s1.get_marks())    # ✔️ Output: 85

s1.set_marks(95)         # ✔️ Update value
print(s1.get_marks())    # Output: 95

s1.set_marks(150)        # ❌ Invalid

#  Real-Life Example of Encapsulation: ATM Machine

class ATM:
    def __init__(self, balance, pin):
        self.__balance = balance   # private variable
        self.__pin = pin           # private variable

    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            return self.__balance
        else:
            return "Incorrect PIN"

    def withdraw(self, amount, entered_pin):
        if entered_pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrawn: {amount}"
            else:
                return "Insufficient balance"
        else:
            return "Incorrect PIN"

# Use ATM
my_atm = ATM(10000, 1234)

print(my_atm.check_balance(1234))     # ✅ Output: 10000
print(my_atm.withdraw(2000, 1234))    # ✅ Withdraw
print(my_atm.check_balance(1234))     # ✅ Output: 8000

print(my_atm.check_balance(1111))     # ❌ Wrong PIN

'''
--> 
Concept	In ATM Example
    Private Data	__balance, __pin
    Public Methods	check_balance(), withdraw()
    Data Hiding	User can't directly access balance
    Controlled Access	Only through correct PIN'''

# What is Abstraction?
'''
--> Definition:
Abstraction ka matlab hota hai:
Sirf important cheeze dikhana, aur complex cheeze chhupana.'''

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Class
    @abstractmethod
    def make_sound(self):  # Abstract Method
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

# Test
d = Dog()
d.make_sound()   # Output: Bark

c = Cat()
c.make_sound()   # Output: Meow

'''
    --> Animal ek abstract class hai → uska make_sound() method sirf declare kiya gaya hai
    --> Dog aur Cat ne us method ko implement kiya (ye required hota hai)
    --> Abstract class ka object directly nahi ban sakta'''

#  Real-Life Example: ATM Machine


from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class SBI(ATM):
    def withdraw(self, amount):
        print(f"SBI ATM: Withdrawn ₹{amount}")

class HDFC(ATM):
    def withdraw(self, amount):
        print(f"HDFC ATM: Withdrawn ₹{amount}")

# Test
sbi = SBI()
sbi.withdraw(1000)

hdfc = HDFC()
hdfc.withdraw(2000)

'''➡️ Yahan ATM is an abstract class
➡️ Har bank (SBI, HDFC) apna withdraw system implement karta hai
➡️ User ko interface same milta hai'''

# diffrence 
    # Encapsulation:

class ATM:
    def __init__(self):
        self.__balance = 10000  # private
    def get_balance(self, pin):
        if pin == 1234:
            return self.__balance

    # Abstraction:

from abc import ABC, abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

# # conclustion
#    Encapsulation = "Data ke chaaron taraf talaa lagana"
#    Abstraction = "Kaam dikhana, kaise ho raha hai wo chhupana"

# 🔷 What is Polymorphism?
