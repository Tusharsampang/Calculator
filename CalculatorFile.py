from _ast import Lambda
from tkinter import *
from tkinter.font import Font

root = Tk()

# Defining title of the project
root.title("Simple Calculator")

# To insert an icon
root.iconbitmap('C:/calculator.ico')

# Defining the entry box
e = Entry(root, width=12, borderwidth=15,font=('Cambria',50) )
e.grid(row=0, column=0, columnspan=15, ipadx=20, ipady= 20 )

# Function for click button
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Function to clear the screen
def button_clear():
    e.delete(0, END)

# Function for addition
def button_add():
    first_number = e.get()
    global f_num
    global action
    # global sum
    f_num = int(first_number)
    action = "add"
    e.delete(0, END)


# Function for subtraction
def button_subtraction():
    third_number = e.get()
    global f_num
    global action
    f_num = int(third_number)
    action = "sub"
    e.delete(0, END)

# Function for multiply
def button_multiply():
    fourth_number = e.get()
    global f_num
    global action
    f_num = int(fourth_number)
    action = "multiply"
    e.delete(0, END)


# Function for divide
def button_divide():
    fifth_number = int(e.get())
    global f_num
    global action
    f_num = int(fifth_number)
    action = "divide"
    e.delete(0, END)

# Function for exponent
def button_exp():
    sixth_number = int(e.get())
    global f_num
    global action
    f_num = int(sixth_number)
    action = "exp"
    e.delete(0, END)

# Function for percentage
def button_percentage():
    seventh_number = int(e.get())
    global f_num
    global action
    f_num = int(seventh_number)
    action = "percentage"
    e.delete(0, END)

# Function for equals to
def button_equal():
    second_number = str(e.get())
    e.delete(0, END)
    if action == "add":
        e.insert(0, f_num + int(second_number))
    elif action == "sub":
        e.insert(0, f_num - int(second_number))
    elif action == "multiply":
        e.insert(0, f_num * int(second_number))
    elif action == "divide":
        global total_div
        total_div=(f_num / int(second_number))
        if total_div % 1 == 0:
            e.insert(0, int(total_div))
        else:
            e.insert(0, total_div)
    elif action == "exp":
        e.insert(0,f_num ** int(second_number))
    elif action == "percentage":
        e.insert(0, f_num % int(second_number))






# Defining the buttons
button_1 = Button(root, text="1", padx=40, pady=20, fg="black", bg="white",bd =1, font=('Cambria', 30), command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, fg="black", bg="white",bd=1, font=('Cambria', 30), command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, fg="black", bg="white",bd=1, font=('Cambria', 30), command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, fg="black", bg="white",bd =1, font=('Cambria', 30), command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, fg="black", bg="white",bd=1, font=('Cambria', 30), command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, fg="black", bg="white",bd=1, font=('Cambria', 30),  command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, fg="black", bg="white",bd=1, font=('Cambria', 30), command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, fg="black", bg="white",bd=1, font=('Cambria', 30), command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, fg="black", bg="white",bd=1, font=('Cambria', 30), command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, fg="black", bg="white",bd=1, font=('Cambria', 30), command=lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, fg="black", bg="white",bd=1, font=('Cambria', 30), command=button_add)
button_subtraction = Button(root, text="-", padx=45, fg="black", bg="white",bd=1, pady=20, font=('Cambria', 30), command=button_subtraction)
button_multiply = Button(root, text="*", padx=40, fg="black", bg="white",bd=1, pady=20, font=('Cambria', 30), command=button_multiply)
button_divide = Button(root, text="/", padx=40, fg="black", bg="white",bd=1, pady=20, font=('Cambria', 30), command=button_divide)
button_equal = Button(root, text="=", padx=105,  fg="black", bg="white",bd=1, pady=20, font=('Cambria', 30), command=button_equal)
button_clear = Button(root, text="C", padx=105, fg="black", bg="white", pady=20,bd=1,  font=('Cambria', 30), command=button_clear)
button_exp = Button(root, text="^", padx=40, pady= 20, fg="black", bg="white",bd=1, font=("Cambria", 30), command=button_exp)
button_percentage = Button(root, text="Mod", padx=10, pady=20, fg="black", bg="white", bd=1, font=("Cambria", 30), command=button_percentage)

# Arranging the buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_exp.grid(row=1, column=3)


button_0.grid(row=4, column=0)
button_subtraction.grid(row=4, column=1)
button_add.grid(row=4, column=2)
button_percentage.grid(row=4, column=3 )


button_clear.grid(row=5, column=0,columnspan=2)
button_equal.grid(row=5, column=2,columnspan=4 )

root.mainloop()
