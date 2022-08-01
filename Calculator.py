from tkinter import Button, Text, Tk

window = Tk()
window.title("CALCULATOR")
window.geometry("270x150")

screen_font = "Helevetica"
screen = Text(window, height = 1, width = 20, font = (screen_font, 20))
screen.grid(row = 0, column = 0, columnspan = 4)

screen_text = ""
def add_to_screen(number):
    screen.delete("1.0", "end")
    global screen_text
    screen_text += str(number)
    screen.insert("1.0", screen_text)

def clear_screen():
    global screen_text
    screen_text = ""
    add_to_screen("")

def clear():
    global screen_text
    l = len(screen_text)
    new_text = screen_text[0 : l-1]
    clear_screen()
    add_to_screen(new_text)

number_stack = []
operation_stack = []
def add():
    equals()
    number = screen.get("1.0", "end-1c")
    number_stack.append(float(number))
    operation_stack.append("+")
    clear_screen()

def subtract():
    equals()
    number = screen.get("1.0", "end-1c")
    number_stack.append(float(number))
    operation_stack.append("-")
    clear_screen()

def multiply():
    equals()
    number = screen.get("1.0", "end-1c")
    number_stack.append(float(number))
    operation_stack.append("*")
    clear_screen()

def divide():
    equals()
    number = screen.get("1.0", "end-1c")
    number_stack.append(float(number))
    operation_stack.append("/")
    clear_screen()

def equals():
    number = screen.get("1.0", "end-1c")
    number_stack.append(float(number))
    if len(operation_stack) > 0:
        num2 = number_stack.pop()
        num1 = number_stack.pop()
        operation = operation_stack.pop()
        if operation == "+":
            answer = num1 + num2
            clear_screen()
            add_to_screen(answer)
            number_stack.append(answer)
            print(answer)
        elif operation == "-":
            answer = num1 - num2
            clear_screen()
            add_to_screen(answer)
            number_stack.append(answer)
        elif operation == "*":
            answer = num1 * num2
            clear_screen()
            add_to_screen(answer)
            number_stack.append(answer)
        elif operation == "/":
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

button_1 = Button(window, text = "1", command = lambda: add_to_screen(1), width = 5, font = (screen_font, 14))
button_1.grid(row = 1, column = 0)

button_2 = Button(window, text = "2", command = lambda: add_to_screen(2), width = 5, font = (screen_font, 14))
button_2.grid(row = 1, column = 1)

button_3 = Button(window, text = "3", command = lambda: add_to_screen(3), width = 5, font = (screen_font, 14))
button_3.grid(row = 1, column = 2)

button_4 = Button(window, text = "4", command = lambda: add_to_screen(4), width = 5, font = (screen_font, 14))
button_4.grid(row = 2, column = 0)

button_5 = Button(window, text = "5", command = lambda: add_to_screen(5), width = 5, font = (screen_font, 14))
button_5.grid(row = 2, column = 1)

button_6 = Button(window, text = "6", command = lambda: add_to_screen(6), width = 5, font = (screen_font, 14))
button_6.grid(row = 2, column = 2)

button_7 = Button(window, text = "7", command = lambda: add_to_screen(7), width = 5, font = (screen_font, 14))
button_7.grid(row = 3, column = 0)

button_8 = Button(window, text = "8", command = lambda: add_to_screen(8), width = 5, font = (screen_font, 14))
button_8.grid(row = 3, column = 1)

button_9 = Button(window, text = "9", command = lambda: add_to_screen(9), width = 5, font = (screen_font, 14))
button_9.grid(row = 3, column = 2)

button_0 = Button(window, text = "0", command = lambda: add_to_screen(0), width = 5, font = (screen_font, 14))
button_0.grid(row = 4, column = 1)

#############################
"""OPERATION BUTTONS"""
#############################

button_add = Button(window, text = "+", command = add, width = 5, font = (screen_font, 14))
button_add.grid(row = 1, column = 3)

button_subtract = Button(window, text = "-", command = subtract, width = 5, font = (screen_font, 14))
button_subtract.grid(row = 2, column = 3)

button_multiply = Button(window, text = "×", command = multiply, width = 5, font = (screen_font, 14))
button_multiply.grid(row = 3, column = 3)

button_divide = Button(window, text = "÷", command = divide, width = 5, font = (screen_font, 14))
button_divide.grid(row = 4, column = 3)

#############################
"""DECIMAL BUTTON"""
#############################

button_divide = Button(window, text = ".", command = lambda: add_to_screen("."), width = 5, font = (screen_font, 14))
button_divide.grid(row = 4, column = 2)

#############################
"""CLEAR BUTTONS"""
#############################

button_clear = Button(window, text = "⌦", command = clear, width = 5, font = (screen_font, 14))
button_clear.grid(row = 4, column = 0)

button_clear = Button(window, text = "Clear", command = clear_screen, width = 10, font = (screen_font, 14))
button_clear.grid(row = 5, column = 0, columnspan = 2)

#############################
"""EQUALS BUTTON"""
#############################

button_equals = Button(window, text = "=", command = equals, width = 10, font = (screen_font, 14))
button_equals.grid(row = 5, column = 2, columnspan = 2)


window.mainloop()

