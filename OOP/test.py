from consolemenu import *
from consolemenu.items import *

class MyClass:
    def my_method(self):
        print("Hello, world!")

class MyMenuItem(MenuItem):
    def __init__(self, text, my_class):
        super().__init__(text=text, menu=None)
        self.my_class = my_class

    def action(self):
        self.my_class.my_method()

m = ConsoleMenu("Title")

my_class = MyClass()
item = MyMenuItem("My Item", my_class)
m.append_item(item)

m.show()