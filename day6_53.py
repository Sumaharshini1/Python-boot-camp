class Animal:
    def Speak():
            return "Speaking......"
class Dog(Animal):
      def Speak():
            return "Dog is speaking......"
class puppy(Dog):
      def Speak():
            return "puppy is speaking......."
obj1=Animal
obj2=Dog
obj3=puppy
print(obj3.Speak())
print(obj3.Speak())
print(obj3.Speak())