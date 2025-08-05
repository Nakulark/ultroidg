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