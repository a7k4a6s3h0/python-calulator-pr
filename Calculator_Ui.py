from tkinter import *
from calculator_code import *


if __name__ == "__main__":
    root = Tk()
    root.geometry("360x350")
    root.title("Calculator")
    root.configure(bg="black")  # Set the background color of the root window

    # Configure grid rows and columns to expand proportionally
    for i in range(10):  # Adjust the range based on your grid
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    equation = StringVar()
    user_input = Entry(root, textvariable=equation, highlightthickness=5, font=('Arial', 20))
    user_input.grid(row=0, column=0, columnspan=10, sticky="nsew")  # Use sticky to expand in all directions

    # Creating Buttons

    button1 = Button(root, text=' 1 ', fg='white', bg='gray',
                     command=lambda: press(1, user_input), height=3, width=10, padx=4)
    button1.grid(row=1, column=0)

    button2 = Button(root, text=' 2 ', fg='white', bg='gray',
                     command=lambda: press(2, user_input), height=3, width=10, padx=4)
    button2.grid(row=1, column=1)

    button3 = Button(root, text=' 3 ', fg='white', bg='gray',
                     command=lambda: press(3, user_input), height=3, width=10, padx=4)
    button3.grid(row=1, column=2)

    button4 = Button(root, text=' 4 ', fg='white', bg='gray',
                     command=lambda: press(4, user_input), height=3, width=10, padx=4)
    button4.grid(row=2, column=0)

    button5 = Button(root, text=' 5 ', fg='white', bg='gray',
                     command=lambda: press(5, user_input), height=3, width=10, padx=4)
    button5.grid(row=2, column=1)

    button6 = Button(root, text=' 6 ', fg='white', bg='gray',
                     command=lambda: press(6, user_input), height=3, width=10, padx=4)
    button6.grid(row=2, column=2)

    button7 = Button(root, text=' 7 ', fg='white', bg='gray',
                     command=lambda: press(7, user_input), height=3, width=10, padx=4)
    button7.grid(row=3, column=0)

    button8 = Button(root, text=' 8 ', fg='white', bg='gray',
                     command=lambda: press(8, user_input), height=3, width=10, padx=4)
    button8.grid(row=3, column=1)

    button9 = Button(root, text=' 9 ', fg='white', bg='gray',
                     command=lambda: press(9, user_input), height=3, width=10, padx=4)
    button9.grid(row=3, column=2)

    button0 = Button(root, text=' 0 ', fg='white', bg='gray',
                     command=lambda: press(0, user_input), height=3, width=10, padx=4)
    button0.grid(row=4, column=0)

    square_root = Button(root, text="√", fg='white', bg='gray',
                  command=lambda: press("√", user_input), height=3, width=10, padx=4)
    square_root.grid(row=5, column=0)

    plus = Button(root, text=' + ', fg='white', bg='gray',
                  command=lambda: press("+", user_input), height=3, width=10, padx=4)
    plus.grid(row=1, column=3)

    minus = Button(root, text=' - ', fg='white', bg='gray',
                   command=lambda: press("-", user_input), height=3, width=10, padx=4)
    minus.grid(row=2, column=3)

    multiply = Button(root, text=' * ', fg='white', bg='gray',
                      command=lambda: press("*", user_input), height=3, width=10, padx=4)
    multiply.grid(row=3, column=3)

    divide = Button(root, text=' / ', fg='white', bg='gray',
                    command=lambda: press("/", user_input), height=3, width=10, padx=4)
    divide.grid(row=4, column=3)

    equal = Button(root, text=' = ', fg='white', bg='gray',
                   command=lambda : equal_press(user_input, equation), height=3, width=10, padx=4)
    equal.grid(row=4, column=2)

    Decimal = Button(root, text='.', fg='white', bg='gray',
                     command=lambda: press('.', user_input), height=3, width=10, padx=4)
    Decimal.grid(row=4, column=1)

    clear = Button(root, text='Clear', fg='white', bg='gray',
                   command=lambda: clear_press(user_input), height=3, width=10, padx=4)
    clear.grid(row=5, column=1)

    go_back = Button(root, text='\u2190', fg='white', bg='gray',
                     command=lambda: press('back', user_input), height=3, width=10, padx=4)
    go_back.grid(row=5, column=2)

    close_but = Button(root, text="Quit", fg='white', bg='red', command=quit, height=3, width=10, padx=4)

    close_but.grid(row=5, column=3)

    root.mainloop()
