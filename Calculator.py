from tkinter import Button, Text, Tk


"""CALCULATOR WINDOW (ROOT)"""
window = Tk()
window.title("CALCULATOR")
window.geometry("")


"""CALCULATOR INPUT SCREEN"""
screen = Text(window, height = 1, width = 10, font = ("", 32))
screen.grid(row = 0, column = 0, columnspan = 4)


"""ADDS TEXT TO INPUT SCREEN"""
def add_to_screen(number):
    screen_text = screen.get("1.0", "end-1c")
    screen.delete("1.0", "end")
    screen_text += str(number)
    screen.insert("1.0", screen_text)

"""COMPLETELY CLEARS INPUT SCREEN"""
def clear_screen():
    screen.delete("1.0", "end")

"""CLEARS SINGLE CHARACTER FROM END OF THE TEXT"""
def clear():
    screen_text = screen.get("1.0", "end-1c")
    new_text = screen_text[0 : len(screen_text)-1]
    clear_screen()
    add_to_screen(new_text)


number_stack = [] #STACK WITH NUMBERS TO BE OPERATED ON
operation_stack = [] #STACK WITH OPERATIONS

"""PREPARES NUMBERS FOR ADDITION"""
def add():
    global number_stack, operation_stack
    equals()
    number = screen.get("1.0", "end-1c")
    number_stack.append(float(number))
    operation_stack.append("+")
    clear_screen()

"""PREPARES NUMBERS FOR SUBTRACTION"""
def subtract():
    global number_stack, operation_stack
    equals()
    number = screen.get("1.0", "end-1c")
    number_stack.append(float(number))
    operation_stack.append("-")
    clear_screen()

"""PREPARES NUMBERS FOR MULTIPLICATION"""
def multiply():
    global number_stack, operation_stack
    equals()
    number = screen.get("1.0", "end-1c")
    number_stack.append(float(number))
    operation_stack.append("*")
    clear_screen()

"""PREPARES NUMBERS FOR DIVISION"""
def divide():
    global number_stack, operation_stack
    equals()
    number = screen.get("1.0", "end-1c")
    number_stack.append(float(number))
    operation_stack.append("/")
    clear_screen()

"""EVALUATES RESULT OF OPERATION AND DISPLAYS ANSWER ON SCREEN"""
def equals():
    global number_stack, operation_stack
    number = screen.get("1.0", "end-1c")
    number_stack.append(float(number))
    if len(operation_stack) > 0:
        num2 = number_stack.pop()
        num1 = number_stack.pop()
        operation = operation_stack.pop()
        if operation == "+": #ADDITION
            answer = num1 + num2
            clear_screen()
            add_to_screen(answer)
            number_stack.append(answer)
        elif operation == "-": #SUBTRACTION
            answer = num1 - num2
            clear_screen()
            add_to_screen(answer)
            number_stack.append(answer)
        elif operation == "*": #MULTIPLICATTION
            answer = num1 * num2
            clear_screen()
            add_to_screen(answer)
            number_stack.append(answer)
        elif operation == "/": #DIVISION
            answer = num1 / num2
            clear_screen()
            add_to_screen(answer)
            number_stack.append(answer)
    else:
        clear_screen()
        add_to_screen(number)
        

#############################
"""NUMBER BUTTONS"""
#############################

button_1 = Button(window, text = "1", command = lambda: add_to_screen(1), height = 2, width = 5, font = ("", 20))
button_1.grid(row = 1, column = 0)

button_2 = Button(window, text = "2", command = lambda: add_to_screen(2), height = 2, width = 5, font = ("", 20))
button_2.grid(row = 1, column = 1)

button_3 = Button(window, text = "3", command = lambda: add_to_screen(3), height = 2, width = 5, font = ("", 20))
button_3.grid(row = 1, column = 2)

button_4 = Button(window, text = "4", command = lambda: add_to_screen(4), height = 2, width = 5, font = ("", 20))
button_4.grid(row = 2, column = 0)

button_5 = Button(window, text = "5", command = lambda: add_to_screen(5), height = 2, width = 5, font = ("", 20))
button_5.grid(row = 2, column = 1)

button_6 = Button(window, text = "6", command = lambda: add_to_screen(6), height = 2, width = 5, font = ("", 20))
button_6.grid(row = 2, column = 2)

button_7 = Button(window, text = "7", command = lambda: add_to_screen(7), height = 2, width = 5, font = ("", 20))
button_7.grid(row = 3, column = 0)

button_8 = Button(window, text = "8", command = lambda: add_to_screen(8), height = 2, width = 5, font = ("", 20))
button_8.grid(row = 3, column = 1)

button_9 = Button(window, text = "9", command = lambda: add_to_screen(9), height = 2, width = 5, font = ("", 20))
button_9.grid(row = 3, column = 2)

button_0 = Button(window, text = "0", command = lambda: add_to_screen(0), height = 2, width = 5, font = ("", 20))
button_0.grid(row = 4, column = 1)

#############################
"""OPERATION BUTTONS"""
#############################

button_add = Button(window, text = "+", command = add, height = 2, width = 5, font = ("", 20))
button_add.grid(row = 1, column = 3)

button_subtract = Button(window, text = "-", command = subtract, height = 2, width = 5, font = ("", 20))
button_subtract.grid(row = 2, column = 3)

button_multiply = Button(window, text = "×", command = multiply, height = 2, width = 5, font = ("", 20))
button_multiply.grid(row = 3, column = 3)

button_divide = Button(window, text = "÷", command = divide, height = 2, width = 5, font = ("", 20))
button_divide.grid(row = 4, column = 3)

#############################
"""DECIMAL BUTTON"""
#############################

button_divide = Button(window, text = ".", command = lambda: add_to_screen("."), height = 2, width = 5, font = ("", 20))
button_divide.grid(row = 4, column = 2)

#############################
"""CLEAR BUTTONS"""
#############################

button_clear = Button(window, text = "⌦", command = clear, height = 2, width = 5, font = ("", 20))
button_clear.grid(row = 4, column = 0)

button_clear = Button(window, text = "Clear", command = clear_screen, height = 2, width = 10, font = ("", 20))
button_clear.grid(row = 5, column = 0, columnspan = 2)

#############################
"""EQUALS BUTTON"""
#############################

button_equals = Button(window, text = "=", command = equals, height = 2, width = 10, font = ("", 20))
button_equals.grid(row = 5, column = 2, columnspan = 2)


window.mainloop()