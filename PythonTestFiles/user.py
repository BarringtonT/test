
import sys


class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print("Hello my name is " + self.name)

    def sayBye(self):
        print("Goodbye!!!!")


james = User("MANGA")
david = User("David")
eric = User("Eric")


james.sayHello()
david.sayHello()
eric.sayHello()

print("Type exit to close program")
leave = input()
if leave == "exit":
    sys.exit()
else:
    print("Program cannot close")
