class Mammal:
    def walk(self):
        print("walk")

# use pass when you're not defining
# other methods in the class


class Dog(Mammal):
    pass


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()


cat1 = Cat()
cat1.be_annoying()

