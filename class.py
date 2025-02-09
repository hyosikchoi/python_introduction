class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
  
  def printname(self):
    print(self.name, self.age)




p1 = Person("John", 36)
p1.myfunc()

# 상속
class Student(Person):
  pass

x = Student("Mike", 30)
x.printname()
