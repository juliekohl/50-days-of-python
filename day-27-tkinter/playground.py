# *args
# def add(*args: int) -> int:
#     # print(type(args)) # class 'tuple'
#     # print(args[0]) # 3
#     # print(args[1]) # 5
#     sum: int = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(3, 5, 6, 2, 1, 7, 4, 3)) # 31

from typing import Dict, Any


# **kwargs
# def calculate(n: int, **kwargs: Dict[str, Any]) -> None:
#     # print(type(kwargs)) # class 'dict'
#     print(kwargs) # {'add': 3, 'multiply': 5}
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n) # 25
#
#
# calculate(2, add=3, multiply=5)

# How to use a **kwargs dictionary safely
# class Car:
#     def __init__(self, **kw: Dict[str, str]) -> None:
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.colour = kw.get("color")
#         self.seats = kw.get("seats")
#
#
# my_car = Car(make="Nissan", model="Skyline")
# print(my_car.model)
# print(my_car.make)
# print(my_car.color)


from tkinter import *
from typing import Any

# Background color
# gui = Tk(className='Python Examples - Window Color')
# # set window size
# gui.geometry("400x300")
#
# # set window color
# gui['background']='yellow'
# # gui.configure(background='yellow')
# gui.mainloop()

# Create a new window and configurations
window = Tk(className="Background color")
window.title("Widget Examples")
# window['background'] = 'blue'
window.config(background='white')
window.minsize(width=500, height=500)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "My new Label Text"
my_label.config(text="My new Label Text")
my_label.pack()


# Button
def button_clicker() -> None:
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicker)
button.pack()

# Entries - input
input = Entry(width=30)
print(input.get())
input.pack()

entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used() -> None:
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value: Any) -> None:
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used() -> None:
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used() -> None:
    print(radio_state.get())
# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event: Any) -> None:
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
#
#
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
