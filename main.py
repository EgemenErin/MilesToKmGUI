from tkinter import *

def convert_to_km():
    # Function to convert miles to kilometers
    miles = float(input_entry.get())
    kilometers = miles * 1.60934
    result_label.config(text=f"{kilometers:.2f}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=150)

# Entry for miles input
input_entry = Entry(width=10)
input_entry.grid(column=1, row=0, padx=(10,10), pady=(20,10))

# Label next to entry for "Miles"
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label for "is equal to"
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1, padx=(10,2), pady=(0,10))

# Label for result
result_label = Label(text="0")
result_label.grid(column=1, row=1, padx=(2,2))

# Label for "Kilometers"
km_label = Label(text="Kilometers")
km_label.grid(column=2, row=1)

convert_button = Button(text="Convert", command=convert_to_km)
convert_button.grid(column=1,row=2)

window.mainloop()
