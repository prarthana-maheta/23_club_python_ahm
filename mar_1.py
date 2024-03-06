# magic methods
# dunder methods

# class Sky:
#     name="Techno"
#     def __init__(self):
#         self.name="Royal"
#         print("in init")

#     def __call__(self):
#         print("in call")
    
#     def __str__(self):
#         return ("at object")

#     def display(self):
#         # self.list1.append()
#         return self.name
# # sky = Sky()
# print(sky)
# sky()

# print(sky())
# print(sky.display())
# list()



# def __royal__()


# instance methods
# static method
# class method
# def display(self)
    


class Vehicle:

    name="techno"

    def __init__(self):
        self.name='royal'

    def dispaly(self):
        print(self.name)
    def ini(self):
        self.dispaly()
        pass
    @staticmethod
    def example(a,b):
        print("example",a,b)

    @classmethod
    def class_vehicle(cls):
        print(cls.name)  

        # print(self.name)  

v = Vehicle()
print(v.name)
# Vehicle.dispaly()
Vehicle.class_vehicle()
print(Vehicle.name)