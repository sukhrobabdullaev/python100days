# OOP paradigm
# 4 concepts of OOP
# procedural, function, object-oriented
# classes, objects and methods
# class => attributes => behavior
# object is an instance of class
# class => variables => methods
# Inheritance, Polymorphism, Encapsulation and Abstraction
# Method overriding ....

class House:
    # data members or attributes
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self,rate):
        cost=rate*self.num_rooms
        return cost

# house_instance=House()
#
# house_instance.num_rooms = 7
# print(house_instance.num_rooms)
# print(House.num_rooms)
#
# print(house_instance.num_rooms)
# print(house_instance.bathrooms)
# print(house_instance.cost_evaluation()) # None that means it is returning anything else


house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

print(house.cost_evaluation(30))


# example of code

value = 7
class A:
    value = 5
a = A()
a.value = 3
print(value)

# bravo = 3
# b = B()
# class B:
#     bravo = 5
#     print("Inside class B")
# c = B()
# print(b.bravo)


