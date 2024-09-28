import tkinter as tk

window = tk.Tk()
window.geometry("300x150")
window.title("CALCULATOR")

tk.Label(window, text="First Number:").grid(row=0, column=0)
num1 = tk.Entry(window, width=17)
num1.grid(row=0, column=1)

tk.Label(window, text="Second Number:").grid(row=1, column=0)
num2 = tk.Entry(window, width=17)
num2.grid(row=1, column=1)

tk.Label(window, text="Result").grid(row=2, column=0)
result = tk.Label(window, bg="grey", width=15)
result.grid(row=2, column=1)

def add():
    n1 = float(num1.get())
    n2 = float(num2.get())
    res = n1 + n2
    result.configure(text=str(res))

def sub():
    n1 = float(num1.get())
    n2 = float(num2.get())
    res = n1 - n2
    result.configure(text=str(res))

def mul():
    n1 = float(num1.get())
    n2 = float(num2.get())
    res = n1 * n2
    result.configure(text=str(res))

def div():
    n1 = float(num1.get())
    n2 = float(num2.get())
    res = n1 / n2
    result.configure(text=str(res))

bt1 = tk.Button(window, text="Add", width=4, command=add)
bt1.grid(row=3, column=0)

bt2 = tk.Button(window, text="Sub", width=4, command=sub)
bt2.grid(row=3, column=1)

bt3 = tk.Button(window, text="Mul", width=4, command=mul)
bt3.grid(row=3, column=2)

bt4 = tk.Button(window, text="Div", width=4, command=div)
bt4.grid(row=3, column=3)

window.mainloop()
