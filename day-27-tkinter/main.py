from tkinter import *
from typing import Any


def button_clicker() -> None:
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Create a new window and configurations
window = Tk()
window.title("My First GUI Program")
# window['background'] = 'blue'
window.minsize(width=500, height=300)
window.config(background='blue')
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a Label", font=("Arial", 25, "bold"))
my_label["text"] = "My new Text"
my_label.config(text="My new Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button
button = Button(text="Click Me", command=button_clicker)
button.grid(column=1, row=1)

new_botton = Button(text="New Botton")
new_botton.grid(column=2, row=0)

# Entries - input
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


window.mainloop()
