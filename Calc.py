import tkinter as tk

calculation = ""


def add_to_calcstring(symbol):
    global calculation
    calculation += (str(symbol))
    text_results.delete(1.0, "end")
    text_results.insert(1.0, calculation)
def evaluate():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_results.delete(1.0, "end")
        text_results.insert(1.0, calculation)

    except:
        clear_field()
        text_results.insert(1.0, "Error")
def clear_field():
    global calculation
    calculation = ""
    text_results.delete(1.0, "end")
window = tk.Tk()
window.geometry("300x275")
window.title("Calculator")

button1 = tk.Button(window, text="1", command=lambda: add_to_calcstring(1), width=5, font=("Arial", 14))
button1.grid(row=2, column=1)

button2 = tk.Button(window, text="2", command=lambda: add_to_calcstring(2), width=5, font=("Arial", 14))
button2.grid(row=2, column=2)

button3 = tk.Button(window, text="3", command=lambda: add_to_calcstring(3), width=5, font=("Arial", 14))
button3.grid(row=2, column=3)

button4 = tk.Button(window, text="4", command=lambda: add_to_calcstring(4), width=5, font=("Arial", 14))
button4.grid(row=3, column=1)

button5 = tk.Button(window, text="5", command=lambda: add_to_calcstring(5), width=5, font=("Arial", 14))
button5.grid(row=3, column=2)

button6 = tk.Button(window, text="6", command=lambda: add_to_calcstring(6), width=5, font=("Arial", 14))
button6.grid(row=3, column=3)

button7 = tk.Button(window, text="7", command=lambda: add_to_calcstring(7), width=5, font=("Arial", 14))
button7.grid(row=4, column=1)

button8 = tk.Button(window, text="8", command=lambda: add_to_calcstring(8), width=5, font=("Arial", 14))
button8.grid(row=4, column=2)

button9 = tk.Button(window, text="9", command=lambda: add_to_calcstring(9), width=5, font=("Arial", 14))
button9.grid(row=4, column=3)

button0 = tk.Button(window, text="0", command=lambda: add_to_calcstring(0), width=5, font=("Arial", 14))
button0.grid(row=5, column=1)

buttonplus = tk.Button(window, text="+", command=lambda: add_to_calcstring("+"), width=5, font=("Arial", 14))
buttonplus.grid(row=2, column=4)
buttonminus = tk.Button(window, text="-", command=lambda: add_to_calcstring("-"), width=5, font=("Arial", 14))
buttonminus.grid(row=3, column=4)

buttonmult = tk.Button(window, text="x", command=lambda: add_to_calcstring("*"), width=5, font=("Arial", 14))
buttonmult.grid(row=4, column=4)
buttondiv = tk.Button(window, text="%", command=lambda: add_to_calcstring("/"), width=5, font=("Arial", 14))
buttondiv.grid(row=5, column=4)

button_left_par = tk.Button(window, text="(", command=lambda: add_to_calcstring("("), width=5, font=("Arial", 14))
button_left_par.grid(row=5, column=2)
button_right_par = tk.Button(window, text=")", command=lambda: add_to_calcstring(")"), width=5, font=("Arial", 14))
button_right_par.grid(row=5, column=3)
button_dec = tk.Button(window, text=".", command=lambda: add_to_calcstring("."), width=5, font=("Arial", 14))
button_dec.grid(row=6, column=4)

button_clear = tk.Button(window, text="Clear", command=clear_field, width=5, font=("Arial", 14))
button_clear.grid(row=6, column=3)
button_equal = tk.Button(window, text="=", command=evaluate, width=5, font=("Arial", 14))
button_equal.grid(row=6, column=1, columnspan=2)



text_results = tk.Text(window,height=2, width=16, font=("Arial", 24))
text_results.grid(columnspan=5, row = 1)
window.mainloop()