
# back to the Salary and Employee example from last
# week
# how done with "private" variables
# and how represent an object not with a memory address
# if your method only gets or sets a variable: it
# should
# absolutely be a @property!
# the line starting with the @ is a so called decorator in
# Python. It's a Python way of getting
class Salary:

   def __init__(self, pay, bonus):
       self.__pay = pay
       self.__bonus = bonus

# if you want to control the string representation
# of an object
# rather than returning something like
# <__main__.Salary object at 0x7fe97e906100>
# similar but slightly different is __repr__
# the example here uses f-strings (stands for formatted string literals)
# available since Python 3.6
   def __str__(self):
       return f"I earn {self.__pay} and my bonus is: {self.__bonus}"

   @property
   def pay_prop(self):
       # include appropriate logic here for allowing or disallowing
       # reading access to this variable
       return self.__pay

   @pay_prop.setter
   def pay_prop(self, value):
       # include appropriate logic here for checking that value is
       # an allowed entry
       self.__pay = value

   @property
   def bonus_prop(self):
       return self.__bonus

   @bonus_prop.setter
   def bonus_prop(self, value):
       self.__bonus = value

   # returns a calculation
   def annual_salary(self):
       return (self.__pay * 12) + self.__bonus


# composition:

class Employee:
   def __init__(self, name, age, pay, bonus):
       self.__name = name
       self.__age = age
       self.__salary_object = Salary(pay, bonus)


   @property
   def age_prop(self):
       return self.__age

   @age_prop.setter
   def age_prop(self, value):
       self.__age = value

   @property
   def name_prop(self):
       return self.__name

   # if you don't provide a setter property, then this
   # variable cannot be set from outside the definition of the class!
   # this is neither good nor bad, just a design choice

   @property
   def salary_obj_prop(self):
       return self.__salary_object

   def total_salary(self):
       return self.__salary_object.annual_salary()


anna = Employee("Anna", 25, 2500, 10000)
print(anna.total_salary())
print(anna.name_prop)
print(anna.salary_obj_prop)     # gives the object memory without __str__
bob = Employee("Bob", 25, 3500, 10000)
print(bob.total_salary())
print(bob.name_prop)
print(bob.salary_obj_prop)
