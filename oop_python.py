# class My_building:
#     floor = '6th'
#     apartment = 12
#     room = '3BSK'
    # def myfun(self, num1,num2):
    #     # print(num1 + num2)
    #     # result = num1 + num2
    #     self.n1 = num1
    #     self.n2 = num2
    #     result = self.n1 + self.n2
    #     return result

    # def __init__(self, num1, num2):
    #     self.n1 = num1
    #     self.n2 = num2



# a = My_building(12,34)

# print(a.n1)

# print(a.myfun(12,12))


# print(a.room)

'''This Topic is about Inheritance'''

# class parents:
#     floor = '6th'
#     apartment = 12
#     room = '3BSK'

# class child(parents):
#     num1 = 12
#     num2 = 23

# a = parents()
# b = child()

# print()

# '''This Topic is about Polymorphism'''

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print('Moving')

# class car(Vehicle):
#     def move(self):
#         print('Moving')

# class boat(Vehicle):
#     def move(self):
#         print('Sail')

# class plane(Vehicle):
#     def move(self):
#         print('Fly')

# a = car('Toyota','Alion A15')
# b = boat('Ship','Titanic')
# c = plane('Air BD','Z16')

# print()
# print(a.move())
# print(b.move())
# print(c.move())

# for i in(a,b,c):
#     # i.move()
#     print(i.brand)