#Julissa Franco
#04/30/2019
#LabActivity4 Problem 3-5


class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def myfunc(self):
        print("Hello" + self.name)

s1 = Student("Julissa", "Computer Science")

print(s1.name)
print(s1.major)

s1.myfunc()

s1.major = ("Crimminal Justice") 

print (s1.major)
