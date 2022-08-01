"""
Convert Miles to its equivalence in kilometers.
"""
from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Entries
entry_miles = Entry(width=10)
entry_miles.insert(END, string="0")
entry_miles.grid(column=1, row=0)

# Labels
label_miles = Label(text="Miles", font=('Arial', 12,))
label_miles.grid(column=2, row=0)

label_is_equal_to = Label(text="is equal to", font=('Arial', 12,))
label_is_equal_to.grid(column=0, row=1)

label_answer = Label(text="0", font=('Arial', 12,))
label_answer.grid(column=1, row=1)

label_km = Label(text="Km", font=('Arial', 12,))
label_km.grid(column=2, row=1)


# Buttons
def action():
    miles = float(entry_miles.get())
    label_answer.config(text=f"{miles * 1.609}")


# calls action() when
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

window.mainloop()
