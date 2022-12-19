from tkinter import *
from typing import Any

# Create a new window and configurations
window = Tk()
window.title("My First GUI Program")
# window['background'] = 'blue'
window.config(background='blue')
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 25, "bold"))
my_label["text"] = "My new Text"
my_label.config(text="My new Text")
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



window.mainloop()
