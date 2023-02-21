#Simple app which takes the user's height and weight and returns their BMI.
#If requested, will generate a target weight for achieving a healthy BMI.

from tkinter import *

def calc_bmi():
    #calculates bmi based on selected units, and configures the output label to show this information
    weight = int(weight_entry.get())
    height = int(height_entry.get())
    if units.get() == 1:
        bmi = int((weight/height/height) * 10000)
    else:
        bmi = (703*weight)//(height*height)
    return bmi
        
def config_outpul_label():
    #generates a label showing user's BMI and information about a healthy BMI.
    bmi = calc_bmi()
    output_label.configure(text=f'Your BMI is {bmi}')
    advice_label.configure(text = '''A healthy range
is between
18 and 25''')
    more_advice_button = Button(text = 'Advice', font=('Verdana', 16), command = weight_change)
    more_advice_button.grid(row = 4, column = 3)
    
def unit_change():
    #converts labels from metric to imperial or vice-versa
    if units.get() == 1:
        weight_label.configure(text='Enter your weight in KG' )
        height_label.configure(text='Enter your height in CM')       
    else:
        weight_label.configure(text='Enter your weight in LBS' )
        height_label.configure(text='Enter your height in inches')
        
def weight_change():
    #shows the user their target weight in they want a healthy BMI
    weight = int(weight_entry.get())
    height = int(height_entry.get())
    bmi = int(calc_bmi())
    target_weight = 0
    if units.get() ==1:
        if bmi >25:
            for i in range(weight, 0, -1):
                if int((i/height/height) * 10000) <= 25:
                    target_weight = i
                    break              
        else:
            for i in range(weight, weight*10):
                if int((i/height/height) * 10000) >= 18:
                    target_weight = i
                    break
        advice_label.configure(text = f'For a healthy BMI, your\n target weight should be \n{target_weight} KG')
    else:
        if bmi >25:
            for i in range(weight, 0, -1):
                if (703*i)//(height*height) <= 25:
                    target_weight = i
                    break
        else:
            for i in range(weight, weight*10):
                if (703*i)//(height*height) >= 18:
                    target_weight = i
                    break
        advice_label.configure(text = f'For a healthy BMI, your\n target weight should be \n{target_weight} lbs')

#sets up GUI
root = Tk()
root.geometry('800x500')
root.title('BMI Calculator')

#creates and sets an integer variable class, defaulted to the metric option
units = IntVar()
units.set(1)
weight_label = Label(width=25, text='Enter your weight in KG', font=('Verdana', 16))
height_label = Label(text='Enter your height in CM', font = ('Verdana', 16))

metric_units = Radiobutton(text = 'Metric', var = units, value = 1, command = unit_change)
imperial_units = Radiobutton(text = 'Imperial', var = units, value = 2, command = unit_change)

weight_entry = Entry(font=('Verdana', 16), width=4)
height_entry = Entry(font=('Verdana', 16), width=4)
calc_button = Button(text='Calculate BMI', font=('Verdana', 16), command=config_outpul_label)
output_label = Label(font=('Verdana', 16))
advice_label = Label(font=('Verdana', 16))



metric_units.grid(row = 0, column = 0)
imperial_units.grid(row = 0, column = 1)
weight_label.grid(row=1, column=0, columnspan=2)
weight_entry.grid(row=1, column=3)
height_label.grid(row=2, column=0, columnspan = 2)
height_entry.grid(row=2, column=3)
calc_button.grid(row=3, column=3)
output_label.grid(row=3, column=0)
advice_label.grid(row = 4, column = 0)

mainloop()
     