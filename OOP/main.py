from sqlite import book

# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

book = book()

# Create the menu
menu = ConsoleMenu("Book Store")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

show = book.show_book()

# A SelectionMenu constructs a menu from a list of strings


# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
menu.append_item(function_item)
menu.show(show)
menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()

