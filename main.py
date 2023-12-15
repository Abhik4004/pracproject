from tkinter import *
km_convert_value =  1.609344

window = Tk()
window.title("Miles to Km Converter")
window.minsize(height=200, width=400)
window.config(padx=20, pady=20)

blankspace = Label(text=" ")
blankspace.grid(column=0, row=0)
blankspace.config(padx=80)

input = Entry()
input.grid(column=1, row=0)

myLabel = Label(text="Miles", font=("Arial"))
myLabel.grid(column=2, row=0)

answer = Label(text=f"is equal to 0 Km", font=("Arial"))
answer.grid(column=0, row=1)

def button_clicked():
    print("I am working")
    miles = input.get()
    print(miles, type(miles))
    miles = int(miles)
    print(type(miles))
    km = miles*km_convert_value
    answer.config(text=f"is equal to    {km}   Km", font=("Arial"))

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)
window.mainloop()