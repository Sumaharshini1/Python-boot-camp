#single,multiple,multilevel#multiple inheritance
class Animal:
    def speak():
        return "Animal is speaking"
class Dog(Animal):
    def Bark():
         return "Bow.."
class puppy(Dog):
    def puppy_speak():
        return "is puppy"
obj1=Animal
obj2=Dog
obj3=puppy
print(obj3.speak())
print(obj3.Bark())
print(obj3.puppy_speak())

#Multilevel inheritance
class Father:
    def father_speak():
        return "Father class"
class Mother:
    def mother_speak():
        return "Mother class"
class kid(Father,Mother):
    def kid_speak():
        return "I'm kid.I'm having properties of mother class and father class"
obj1=kid
obj2=Father
obj3=Mother
print(obj2.father_speak())
print(obj3.mother_speak())
print(obj1.kid_speak())