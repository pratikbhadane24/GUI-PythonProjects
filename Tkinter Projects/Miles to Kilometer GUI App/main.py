from tkinter import *


def calculate():
    dist_km = int(input.get()) * 1.60934
    new_text = f"{int(dist_km)} Km"
    km.config(text=new_text)


window = Tk()
window.title("Miles to Kilometer")
window.config(padx=50, pady=50)


input = Entry(width=5)
input.grid(row=0, column=0)
input.get()

miles = Label(text="Miles", font=("Fira Code", 12))
miles.grid(row=0, column=1)

text = Label(text="is equal to", font=("Fira Code", 12))
text.grid(row=1, column=0)

km = Label(text=" ", font=("Fira Code", 12))
km.grid(row=1, column=1)

calc = Button(text="Calculate", command=calculate)
calc.grid(row=2, column=1)


window.mainloop()
