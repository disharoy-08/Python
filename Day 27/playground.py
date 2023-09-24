def add(*args):
    print(type(args))
    sum = 0
    for n in args:
        sum+= n
    return sum

print(add(3,5,6))

def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

#calculate(3, add = 5, multiply = 9)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car( model='GT-R')
my_car1 = Car(make="Titu", model='Lambergini')
print(my_car.model)
print(my_car.make)


