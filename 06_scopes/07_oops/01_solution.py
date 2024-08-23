# Basic Class and Object
# Problem: Create a car class with attributes or variable like brand and model . then create an instance of this class

#CLASS
class Car:                    #self.brand is class ke ander ke variables
   total_car = 0

   def __init__(self , brand , model):
       self.__brand = brand
       self.model = model
       Car.total_car += 1
    

    # making getter method using get_
   def get_brand(self):
        return self.__brand + " !"

   def full_name(self):
        return f"{self.__brand} {self.model}"

   def fuel_type(self):
       return "Petrol or Diesel"


   def general_description(self):
       return "Cars are means of transport"



class ElectricCar(Car):
   def __init__(self, brand , model , battery_size):
       super().__init__(brand, model)
       self.battery_size = battery_size

   def fuel_type(self):
       return "Electric Charge"


# my_tesla = ElectricCar("Tesla" , "Model S" , "85kWh")

#print(my_tesla._brand)
#print(my_tesla.fuel_type())


my_car = Car("Tata" , "Safari")
Car("Tata" ,"Nexon")


print(my_car.general_description())

# init is also known as contructor

#OBJECT

# my_car = Car("Toyota" , "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


# my_new_car = Car("Tata" , "Safari")
# print(my_new_car.model)
# print(my_new_car.full_name())




