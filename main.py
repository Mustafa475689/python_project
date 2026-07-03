from abc import ABC, abstractmethod
# pillars of OOPs ///////////
# Inheritance..
# Parent Class
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start(self):
#         print(f"{self.brand} {self.model} is starting...")

#     def stop(self):
#         print(f"{self.brand} {self.model} has stopped.")

#     def info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")


# # Child Class - Toyota
# class Toyota(Car):
#     def __init__(self, model):
#         super().__init__("Toyota", model)

#     def feature(self):
#         print("Toyota Feature: Excellent reliability.")


# # Child Class - Suzuki
# class Suzuki(Car):
#     def __init__(self, model):
#         super().__init__("Suzuki", model)

#     def feature(self):
#         print("Suzuki Feature: Great fuel efficiency.")


# # Child Class - Hyundai
# class Hyundai(Car):
#     def __init__(self, model):
#         super().__init__("Hyundai", model)

#     def feature(self):
#         print("Hyundai Feature: Modern technology.")


# # Creating Objects
# car1 = Toyota("Corolla")
# car2 = Suzuki("Alto")
# car3 = Hyundai("Elantra")

# # Testing
# car1.info()
# car1.start()
# car1.feature()
# print()

# car2.info()
# car2.start()
# car2.feature()
# print()

# car3.info()
# car3.start()
# car3.feature()
# ...

# 2 Polymorphism..
# class Animal:
#     def show(self):
#         print("WE are animals")

# # Method over writing
# class Human(Animal):
#     def show(self): # this show show function over writes the Animal class show function because they have same name 
#         print("Hello how are you doing")

# obj = Human()
# obj.show()

# Duck typing..
# class Animal:
#     def make_sound(self):
#         print("Animal makes a sound")


# # Child Class - Dog
# class Dog(Animal):
#     def make_sound(self):
#         print("Dog barks: Woof Woof!")


# # Child Class - Cat
# class Cat(Animal):
#     def make_sound(self):
#         print("Cat meows: Meow!")


# # Child Class - Cow
# class Cow(Animal):
#     def make_sound(self):
#         print("Cow moos: Moo!")

# # Creating Objects
# animal = Animal()
# dog = Dog()
# cat = Cat()
# cow = Cow()

# # Calling Methods
# animal.make_sound()
# dog.make_sound()
# cat.make_sound()
# cow.make_sound()     
# ...

# 3 Encapsulation...
# class Factory:
#     k = "Karachi" # public 
#     _h = "Hyderabad" # Protected 
#     __n = "Nazimabad"  # Private
#     def show(self):
#         print("Welcome to Karachi")
#         print(Factory.__n) # you can access private attribute by printing this in its own class and then call outside


# class Shop(Factory):
#     def show(self):
#         print(super()._h)
#         print(super().k)
#         # print(super().__n) this line will give you error beacuse it is a private attribute so you can not use it outsideclass

# obj = Shop()
# fac = Factory()
# fac.show()
# obj.show()
# ...

# Abstraction..

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass 

    @abstractmethod
    def area(self):
        pass


class Square(abstract):
    def __init__(self, side):
        self.side = side
    
    def perimeter(self):
        print("I have created")

    def area(self):
        print("this is an area")


class Circle(abstract):
    def __init__(self, radius):
        self.radius =radius

    def perimeter(self):
        print("I have created")

    def area(self):
        print("this is an area")

circle = Circle(7)
sqr = Square(5)

# ...