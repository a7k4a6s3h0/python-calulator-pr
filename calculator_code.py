# from Calculator_Ui import equation
import math
global counter
counter = 0


def press(value, user_input):
    global counter
    if value == "back":
        current_text = user_input.get()
        if len(current_text) > 0:
            user_input.delete(len(current_text) - 1)
    else:
        user_input.insert(counter, value)
        counter += 1


def equal_press(user_input, equation):

    try:
        current_text = user_input.get()
        if "√" in current_text:
            number = current_text.split("√")[1]
            result = eval("math.sqrt(" + str(number) + ")")
            equation.set("{:.2f}".format(result))
        else:
            result = str(eval(current_text))
            equation.set(result)

    except Exception as e:
        clear_press(user_input)
        user_input.insert(0, "Error")


def clear_press(user_input):
    if user_input:
        current_text = user_input.get()
        if len(current_text) > 0:
            user_input.delete(0, len(current_text))

