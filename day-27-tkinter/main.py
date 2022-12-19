from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "My new Label Text"
my_label.config(text="My new Label Text")


# Button
def button_clicker() -> None:
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicker)
button.pack()

# Entry - input
input = Entry(width=10)
input.pack()
print(input.get())


window.mainloop()
