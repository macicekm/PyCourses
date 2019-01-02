# https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/

class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance


custMartin = Customer("Martin Macíček",1000.53)

custMartin.withdraw(500)
custMartin.deposit(1000)

custOlga = Customer("Olga Macíčková",100000)

custOlga.deposit(200000)

print(custOlga.balance)
print(custOlga.name)


#Static methods

class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod # To make it clear that this method should not receive the instance as the first parameter (i.e. self on "normal" methods), the @staticmethod decorator is used, turning our definition into:
    def make_car_sound():
        print('VRooooommmm!')

mustang = Car('Ford', 'Mustang')
print(mustang.wheels)
# 4
print(Car.wheels)
# 4

print(mustang.make_car_sound())

class Car(object):
    ...

class Vehicle(object):
    ...
    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2



class Pass():
    def __init__(self):
        pass

pok = Pass()

# INHERITANCE


class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    base_sale_price = 0

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Vehicle object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on


    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

"""
Now we can make the Car and Truck class inherit from the Vehicle class by replacing object in the line class Car(object). 
The class in parenthesis is the class that is inherited from (object essentially means "no inheritance". 

We can now define Car and Truck in a very straightforward way:
"""

class Car(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Car object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 8000


class Truck(Vehicle):

    def __init__(self, wheels, miles, make, model, year, sold_on):
        """Return a new Truck object."""
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.base_sale_price = 10000


# Creating abstract class - this can't be used to create any instance, only to be inherited from to another class

from abc import ABCMeta, abstractmethod
class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.


    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    @abstractmethod
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass

"""
Now, since vehicle_type is an abstractmethod, we can't directly create an instance of Vehicle. As long as Car and Truck inherit from Vehicle and define vehicle_type, we can instantiate those classes just fine.

Returning to the repetition in our Car and Truck classes, let see if we can't remove that by hoisting up common functionality to the base class, Vehicle:
"""


# Now the Car and Truck classes become:

class Car(Vehicle):
    """A car for sale by Jeffco Car Dealership."""

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'

class Truck(Vehicle):
    """A truck for sale by Jeffco Car Dealership."""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'


volvo = Car(100, 'a', 'XC40', 2005, 2013)



# Pokus o vytvoreni nejake class s nactenim dat jako v Jezevciku

import pandas as pd

cisloKTK = 'KTK00000297'






class KTK_Class(object):
    def __init__(self,codeOverdraftNumber):

        df = pd.read_excel('chybneKOPktk.xlsx')
        dfRow = df.loc[df['CODE_LOAN_NUMBER'] == codeOverdraftNumber]


        self.cisloKTK = codeOverdraftNumber
        self.dpd = dfRow.iloc[0]['DPD_FIN']
        self.kop = dfRow.iloc[0]['KOP']
        self.sumbalance = dfRow.iloc[0]['SUMBALANCE']
        self.op_fin = dfRow.iloc[0]['OP_FIN']

        print("Overdraft " + self.cisloKTK + " initialized.")


ktk = KTK_Class(cisloKTK)

ktk.dpd

ktk.kop

ktk.cisloKTK

ktk.sumbalance

ktk2 =


del dpdHodnota


import this # ZEN of Python



# Abstract class

from abc import ABC, abstractmethod

class Employee(object):

    @abstractmethod

    def calculate_salary(self,sal):

        return 5


class Developer(Employee):

    def calculate_salary(self,sal):
        finalsalary = sal*1.10

        return finalsalary


emp1 = Developer()

print(emp1.calculate_salary(100))



class A:
    def _single_method(self):
        pass
    def __double_method(self): # for mangling
        pass
class B(A):
    def __double_method(self): # for mangling
        pass



