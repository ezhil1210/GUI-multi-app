from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from random import randint

win = Tk()
win.title("gui app by Ezhil"
          "")
win.config(bg="#373737")
def hompg():
    for widget in win.winfo_children():
        widget.destroy()
    root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
    root.grid(row=1, column=1, padx=20, pady=20)
    calcbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                    text="Calculator", command=calc)
    calcbtn.grid(row=1, column=0, padx=20, pady=15)
    xobtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                   text="XO", command=xo)
    xobtn.grid(row=2, column=0, padx=20, pady=15)
    xobtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                   text="Convert", command=converters)
    xobtn.grid(row=3, column=0, padx=20, pady=15)
    rpsbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                   text="Rock Paper Scissors", command=rpsfn)
    rpsbtn.grid(row=4, column=0, padx=20, pady=15)

def xo():
    for widget in win.winfo_children():
        widget.destroy()

    global x, o, clicked, count, buttons
    clicked = True
    x = 0
    o = 0
    r = IntVar()
    r.set(2)  # Default to "User vs COMPUTER"

    def reset():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9, score
        global clicked, count, buttons

        clicked = True
        count = 0
        for widget in win.winfo_children():
            widget.destroy()

        root = LabelFrame(win, text="XO Game by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=1, column=1, padx=20, pady=20)

        b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737", command=lambda: b_click(b1))
        b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737", command=lambda: b_click(b2))
        b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737", command=lambda: b_click(b3))
        b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737", command=lambda: b_click(b4))
        b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737", command=lambda: b_click(b5))
        b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737", command=lambda: b_click(b6))
        b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737", command=lambda: b_click(b7))
        b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737", command=lambda: b_click(b8))
        b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737", command=lambda: b_click(b9))

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)
        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)
        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

        buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

        Radiobutton(root, text="User vs PLAYER", bg="#373737", fg="red", font=('Helvetica', 10, 'bold'), variable=r, value=1).grid(row=0, column=4)
        Radiobutton(root, text="User vs COMPUTER", bg="#373737", fg="red", font=('Helvetica', 10, 'bold'), variable=r, value=2).grid(row=1, column=4)

        resetbtn = Button(root, text="Reset Game", command=reset, bg="#373737", fg="orange")
        resetbtn.grid(row=4, column=1, pady=20)

        score = Label(root, text=f"{x} - {o}", bg="#373737", fg="light blue", font=('Helvetica', 18, 'bold'))
        score.grid(row=3, column=1, pady=20)

        homebtn = Button(root, font=('Helvetica', 10, 'bold'), fg="#00C0FF", bg="#373737", text="Home", command=hompg)
        homebtn.grid(row=4, column=2)

    def b_click(b):
        global clicked, count, buttons
        type = r.get()
        if b["text"] == " " and clicked:
            b.config(text="X", fg="green")
            clicked = False
            buttons.remove(b)
            count += 1
            checkifwon()

        if type == 1 and b["text"] == " " and not clicked:
            b.config(text="O", fg="orange")
            clicked = True
            buttons.remove(b)
            count += 1
            checkifwon()

        if type == 2 and not clicked:
            computerchoice = random.choice(buttons)
            computerchoice.config(text="O", fg="orange")
            buttons.remove(computerchoice)
            clicked = True
            count += 1
            checkifwon()

    def checkifwon():
        global x, o, score
        winner = False

        win_conditions = [
            (b1, b2, b3), (b4, b5, b6), (b7, b8, b9),  # Rows
            (b1, b4, b7), (b2, b5, b8), (b3, b6, b9),  # Columns
            (b1, b5, b9), (b7, b5, b3)  # Diagonals
        ]

        for a, b, c in win_conditions:
            if a["text"] == b["text"] == c["text"] and a["text"] != " ":
                winner = a["text"]
                break

        if winner:
            if winner == "X":
                messagebox.showinfo("Match Result", "X Won!")
                x += 1
            else:
                messagebox.showinfo("Match Result", "O Won!")
                o += 1

            a.config(bg="red", fg="green")
            b.config(bg="red", fg="green")
            c.config(bg="red", fg="green")
            reset()
            score.config(text=f"{x} - {o}")
        elif count == 9:
            messagebox.showinfo("Match Result", "It's a tie!")
            reset()
            score.config(text=f"{x} - {o}")

    reset()
    
def calc():
    for widget in win.winfo_children():
        widget.destroy()
    root = LabelFrame(win, text="Calculator By Ezhil", bg='#373737', fg="white", padx=20, pady=20)
    root.grid(row=0,column=0,padx=20, pady=20)
    e = Entry(root, width=25, font=('arial', 18, 'bold'), borderwidth=5, text="0", justify='right', bg="#373737",
              fg="white")
    e.insert(0, 0)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def button_click(number):

        current = e.get()

        e.delete(0, END)
        e.insert(0, str(current) + str(number))


    def Button_Clear():
        e.delete(0, END)
        e.insert(0, 0)


    def Button_add():
        first_number = e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        e.delete(0, END)


    def Button_sub():
        first_number = e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        e.delete(0, END)


    def Button_mul():
        first_number = e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        e.delete(0, END)


    def Button_div():
        first_number = e.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        e.delete(0, END)

    def Button_equal():
        second_number = e.get()
        e.delete(0, END)
        if math == "addition":
            e.insert(0, f_num + int(second_number))
        if math == "subtraction":
            e.insert(0, f_num - int(second_number))
        if math == "multiplication":
            e.insert(0, f_num * int(second_number))
        if math == "division":
            e.insert(0, f_num / int(second_number))


    button_1 = Button(root, text=1, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(1))
    button_2 = Button(root, text=2, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(2))
    button_3 = Button(root, text=3, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(3))
    button_4 = Button(root, text=4, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(4))
    button_5 = Button(root, text=5, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(5))
    button_6 = Button(root, text=6, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(6))
    button_7 = Button(root, text=7, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(7))
    button_8 = Button(root, text=8, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(8))
    button_9 = Button(root, text=9, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(9))
    button_0 = Button(root, text=0, font="bold", padx=40, pady=20, bg="#373737", fg="white", command=lambda: button_click(0))
    button_add = Button(root, text="+", font="bold", padx=40, pady=20, bg="#373737", fg="orange", command=Button_add)
    button_equal = Button(root, text="=", font="bold", padx=100, pady=20, bg="#373737", fg="green", command=Button_equal)
    button_clear = Button(root, text="C", font="bold", padx=99, pady=20, bg="#373737", fg="orange", command=Button_Clear)
    button_sub = Button(root, text="-", font="bold", padx=42, pady=20, bg="#373737", fg="orange", command=Button_sub)
    button_mul = Button(root, text="×", font="bold", padx=40, pady=20, bg="#373737", fg="orange", command=Button_mul)
    button_div = Button(root, text="÷", font="bold", padx=40, pady=20, bg="#373737", fg="orange", command=Button_div)

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_add.grid(row=4, column=1)
    button_clear.grid(row=6, column=1, columnspan=2)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_sub.grid(row=4, column=2)
    button_mul.grid(row=5, column=0)
    button_div.grid(row=6, column=0)
    homebtn = Button(root, font=('Helvetica', 10, 'bold'), fg="#00C0FF", bg="#373737", text="Home",
                     command=hompg)
    homebtn.grid(row=7, column=2,pady=20)

def converters():
    for widget in win.winfo_children():
        widget.destroy()


    def home():
        global homebtn
        for widget in win.winfo_children():
            widget.destroy()

        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Converters App By Ezhil")
        
        Label(root, bg="#373737", fg="light green", font=('Helvetica', 10, 'bold'),
              text="\n  Click any button for conversion", justify="left").grid(row=0, column=0)

        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Kilometer to Meter", command=kmmpage).grid(row=1, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Meter to Kilometer", command=mkmpage).grid(row=2, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=22, pady=5, fg="#00C0FF",
               text="Fahrenheit to Celsius", command=fahcel).grid(row=3, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=22, pady=5, fg="#00C0FF",
               text="Celsius to Fahrenheit", command=celfah).grid(row=4, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Miles to Kilometers", command=milekmpage).grid(row=5, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Kilometers to Miles", command=kmmilepage).grid(row=6, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Calculate your BMI", command=bmipage).grid(row=7, column=0, padx=20, pady=15)

        homebtn = Button(root, font=('Helvetica', 10, 'bold'), fg="#00C0FF", bg="#373737", text="Home",
                         command=hompg)
        homebtn.grid(row=9, column=2, pady=20)

    def kmmpage():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Kilometers to Meters")

        Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
              text="\n  Enter KM value", justify="left").grid(row=0, column=0)

        Km = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737", fg="white")
        Km.grid(row=1, column=0)

        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid(row=2, column=0)

        def kmmfun():
            try:
                m = float(Km.get()) * 1000
                label.config(text=f"{Km.get()} KM = {round(m, 2)} meters")
            except ValueError:
                label.config(text="Please enter a valid number")

        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Convert", command=kmmfun).grid(row=3, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Back",
               command=home).grid(row=4, column=0, pady=15)

    def mkmpage():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Meters to Kilometers")

        Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
              text="\n  Enter Meters value", justify="left").grid(row=0, column=0)

        meters = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737", fg="white")
        meters.grid(row=1, column=0)

        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid(row=2, column=0)

        def mkmfun():
            try:
                kilom = float(meters.get()) / 1000
                label.config(text=f"{meters.get()} meters = {round(kilom, 2)} KM")
            except ValueError:
                label.config(text="Please enter a valid number")

        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Convert", command=mkmfun).grid(row=3, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Back",
               command=home).grid(row=4, column=0, pady=15)

    def fahcel():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Fahrenheit to Celsius")

        Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
              text="\n  Enter Fahrenheit value", justify="left").grid(row=0, column=0)

        fah = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737", fg="white")
        fah.grid(row=1, column=0)

        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid(row=2, column=0)

        def fahceldef():
            try:
                celcius = (float(fah.get()) - 32) * 5 / 9
                label.config(text=f"{fah.get()} Fahrenheit = {round(celcius, 2)} Celsius")
            except ValueError:
                label.config(text="Please enter a valid number")

        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Convert", command=fahceldef).grid(row=3, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Back",
               command=home).grid(row=4, column=0, pady=15)

    def celfah():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Celsius to Fahrenheit")

        Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
              text="\n  Enter Celsius value", justify="left").grid(row=0, column=0)

        cel = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737", fg="white")
        cel.grid(row=1, column=0)

        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid(row=2, column=0)

        def celfahdef():
            try:
                fahrenheit = (float(cel.get()) * 9 / 5) + 32
                label.config(text=f"{cel.get()} Celsius = {round(fahrenheit, 2)} Fahrenheit")
            except ValueError:
                label.config(text="Please enter a valid number")

        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Convert", command=celfahdef).grid(row=3, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Back",
               command=home).grid(row=4, column=0, pady=15)

    def milekmpage():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Miles to Kilometers")

        Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
              text="\n  Enter Miles value", justify="left").grid(row=0, column=0)

        miles = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737", fg="white")
        miles.grid(row=1, column=0)

        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid(row=2, column=0)

        def milekmfun():
            try:
                kilo = float(miles.get()) * 1.60934
                label.config(text=f"{miles.get()} miles = {round(kilo, 2)} KM")
            except ValueError:
                label.config(text="Please enter a valid number")

        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Convert", command=milekmfun).grid(row=3, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Back",
               command=home).grid(row=4, column=0, pady=15)

    def kmmilepage():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Kilometers to Miles")

        Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
              text="\n  Enter KM value", justify="left").grid(row=0, column=0)

        kilometer = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737", fg="white")
        kilometer.grid(row=1, column=0)

        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid(row=2, column=0)

        def kmmilefun():
            try:
                mile = float(kilometer.get()) / 1.60934
                label.config(text=f"{kilometer.get()} KM = {round(mile, 2)} miles")
            except ValueError:
                label.config(text="Please enter a valid number")

        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Convert", command=kmmilefun).grid(row=3, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Back",
               command=home).grid(row=4, column=0, pady=15)

    def bmipage():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Calculate your BMI")

        Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
              text="\n  Enter your weight in KGs", justify="left").grid(row=0, column=0)

        weight = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737", fg="white")
        weight.grid(row=1, column=0, pady=10)

        Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
              text="\n  Enter your height in CMS", justify="left").grid(row=2, column=0)

        height = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737", fg="white")
        height.grid(row=3, column=0, pady=10)

        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid(row=4, column=0)

        def bmifun():
            try:
                m = float(height.get()) / 100
                bmi = float(weight.get()) / (m * m)
                if bmi < 18.5:
                    label.config(text=f"Your BMI is {round(bmi, 2)}\nYou are underweight")
                elif 18.5 <= bmi < 24.9:
                    label.config(text=f"Your BMI is {round(bmi, 2)}\nYou are in normal weight")
                elif 25 <= bmi < 29.9:
                    label.config(text=f"Your BMI is {round(bmi, 2)}\nYou are overweight")
                else:
                    label.config(text=f"Your BMI is {round(bmi, 2)}\nYou are obese")
            except ValueError:
                label.config(text="Please enter valid numbers")
            except ZeroDivisionError:
                label.config(text="Please enter correct height")

        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
               text="Calculate", command=bmifun).grid(row=5, column=0, padx=20, pady=15)
        Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Back",
               command=home).grid(row=6, column=0, pady=15)

    home()

def rpsfn():
    for widget in win.winfo_children():
        widget.destroy()

    root = LabelFrame(win, text="ROCK PAPER SCISSORS by Ezhil", bg='#373737', fg="orange", padx=20, pady=20)
    root.grid(row=0, column=0, padx=20, pady=20)

    homebtn = Button(root, font=('Helvetica', 10, 'bold'), fg="#00C0FF", bg="#373737", text="Home", command=hompg)
    homebtn.grid(row=10, column=2, pady=20)

    rock = PhotoImage(file="rpspics/pcrock.png")
    paper = PhotoImage(file='rpspics/pcpaper.png')
    scissors = PhotoImage(file='rpspics/pcscissors.png')

    you = Label(root, text="YOU", font=('Helvetica', 18, 'bold'), bg="#373737", fg="green")
    you.grid(row=1, column=0)
    computerlabel = Label(root, text="COMPUTER", font=('Helvetica', 18, 'bold'), bg="#373737", fg="green")
    computerlabel.grid(row=1, column=2)

    image_list = [rock, paper, scissors]
    computer = randint(0, 2)
    computerimage = Label(root, image=image_list[computer], height=350, width=300, padx=60)
    computerimage.grid(row=2, column=2)

    global userscore, computerscore
    userscore = 0
    computerscore = 0

    result = Label(root, text="", font=('Helvetica', 18, 'bold'), bg="#373737", fg="orange", justify="center")
    result.grid(row=7, column=0, columnspan=3)
    score = Label(root, text=f"{userscore} - {computerscore}", font=('Helvetica', 18, 'bold'), bg="#373737", fg="#00C0FF")
    score.grid(column=1, row=9)

    userrock = PhotoImage(file='rpspics/userrock.png')
    userpaper = PhotoImage(file='rpspics/userpaper.png')
    userscissors = PhotoImage(file='rpspics/userscissors.png')
    userpicture = Label(root, image=userrock, height=350, width=300, padx=60, pady=60, bd=0)
    userpicture.grid(row=2, column=0)

    def update_score():
        score.config(text=f"{userscore} - {computerscore}")

    def clickrock():
        global userscore, computerscore
        computer = randint(0, 2)
        computerimage.config(image=image_list[computer])
        userpicture.config(image=userrock)
        if computer == 0:
            result.config(text="It's a tie!", fg="orange")
        elif computer == 1:
            result.config(text="Paper covers rock! You Lose!", fg="orange")
            computerscore += 1
        elif computer == 2:
            result.config(text="Rock smashes scissors! You win!", fg="orange")
            userscore += 1
        update_score()

    Rock = Button(root, text="Rock", font=('Helvetica', 18, 'bold'), command=clickrock, bg="#373737", fg="purple")
    Rock.grid(row=6, column=0)

    def clickpaper():
        global userscore, computerscore
        computer = randint(0, 2)
        computerimage.config(image=image_list[computer])
        userpicture.config(image=userpaper)
        if computer == 1:
            result.config(text="It's a tie!", fg="orange")
        elif computer == 0:
            result.config(text="Paper covers rock! You win!", fg="orange")
            userscore += 1
        elif computer == 2:
            result.config(text="Scissors cuts paper! You lose!", fg="orange")
            computerscore += 1
        update_score()

    Paper = Button(root, text="Paper", font=('Helvetica', 18, 'bold'), command=clickpaper, bg="#373737", fg="green")
    Paper.grid(row=6, column=1)

    def clickscissor():
        global userscore, computerscore
        computer = randint(0, 2)
        computerimage.config(image=image_list[computer])
        userpicture.config(image=userscissors)
        if computer == 0:
            result.config(text="Rock smashes scissors! You lose!", fg="orange")
            computerscore += 1
        elif computer == 1:
            result.config(text="Scissors cuts paper! You win!", fg="orange")
            userscore += 1
        elif computer == 2:
            result.config(text="It's a tie!", fg="orange")
        update_score()

    Scissors = Button(root, text="Scissors", font=('Helvetica', 18, 'bold'), command=clickscissor, bg="#373737", fg="orange")
    Scissors.grid(row=6, column=2)

hompg()
win.mainloop()
