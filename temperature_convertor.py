from tkinter import *

#creating the instance of tkinter
window = Tk()

#defining the function to convert form celsius
def from_celsius():
    fahrenheit = (float(e2_value.get())*(9/5))+32 #celsius to fahrenheit
    kelvin = float(e2_value.get())+273.15         #celsius to kelvin

    t1.insert(END, fahrenheit)
    t2.insert(END, kelvin)

#displays the instruction  
e1 = Label(window, text="Input the temperature in celsius")
e1.grid(row=0, column=0)

#entering the temperature in celsius
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

e3 = Label(window, text="Fahrenheit")
e3.grid(row=1, column=0)

e4 = Label(window, text="Kelvin")
e4.grid(row=1, column=1)

#displays temperature in fahrenheit
t1 = Text(window, height=5, width=30)
t1.grid(row=2, column=0)

#displays temperature in kelvin
t2 = Text(window, height=5, width=30)
t2.grid(row=2, column=1)

b1 = Button(window, text="Convert", command=from_celsius) #button with command to convert temperature
b1.grid(row=0, column=2)

window.mainloop()