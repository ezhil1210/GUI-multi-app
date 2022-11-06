from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import random

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

def xo():
    for widget in win.winfo_children():
        widget.destroy()
    global x, o
    clicked = True
    x = 0
    o = 0
    r = IntVar()
    r.set("2")

    def reset():
        global b1, b2, b3, b4, b5, b6, b7, b7, b8, b8, b9, score, e, name
        global clicked, count, buttons
        clicked = True
        count = 0
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="XO Game by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=1, column=1, padx=20, pady=20)

        b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                    command=lambda: b_click(b1))
        b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                    command=lambda: b_click(b2))
        b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                    command=lambda: b_click(b3))
        b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                    command=lambda: b_click(b4))
        b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                    command=lambda: b_click(b5))
        b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                    command=lambda: b_click(b6))
        b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                    command=lambda: b_click(b7))
        b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                    command=lambda: b_click(b8))
        b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#373737",
                    command=lambda: b_click(b9))

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

        buttons = [b1, b2, b3, b4, b5 , b6, b7, b8, b9]
        Radiobutton(root, text=("User vs PLAYER"), bg="#373737", fg="red", font=('Helvetica', 10, 'bold'), variable=r,
                    value=1).grid(row=0, column=4)
        Radiobutton(root, text=("User vs COMPUTER"), bg="#373737", fg="red", font=('Helvetica', 10, 'bold'),
                    variable=r,
                    value=2).grid(row=1, column=4)
        resetbtn = Button(root, text="Reset Game", command=reset, bg="#373737", fg="orange").grid(row=4, column=1,
                                                                                                  pady=20)
        score = Label(root, text=(x, "-", o), bg="#373737", fg="light blue", font=('Helvetica', 18, 'bold'))
        score.grid(row=3, column=1, pady=20)
        homebtn = Button(root, font=('Helvetica', 10, 'bold'), fg="#00C0FF", bg="#373737", text="Home",
                         command=hompg)
        homebtn.grid(row=4, column=2)

    def b_click(b):
        global clicked, count, buttons
        type = r.get()
        if b["text"] == " " and clicked == True:
            b.config(text="X", fg="green")
            clicked = False
            buttons.remove(b)
            count += 1
            checkifwon()

        if type == 1 and b["text"] == " " and clicked == False:
            b.config(text="O", fg="orange")
            clicked = True
            buttons.remove(b)
            count += 1
            checkifwon()

        if type == 2 and clicked == False:
            computerchoice = random.choice(buttons)
            computerchoice.config(text="O", fg="orange")
            buttons.remove(computerchoice)
            clicked = True
            count += 1
            checkifwon()

    def checkifwon():
        global winner, x, o, score
        winner = False

        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1.config(bg="red", fg="green")
            b2.config(bg="red", fg="green")
            b3.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "X Won!")
            reset()
            x += 1
            score.config(text=(x, "-", o))
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4.config(bg="red", fg="green")
            b5.config(bg="red", fg="green")
            b6.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "X Won!")
            reset()
            x += 1
            score.config(text=(x, "-", o))
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7.config(bg="red", fg="green")
            b8.config(bg="red", fg="green")
            b9.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "X Won!")
            reset()
            x += 1
            score.config(text=(x, "-", o))
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b7.config(bg="red", fg="green")
            b4.config(bg="red", fg="green")
            b1.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "X Won!")
            reset()
            x += 1
            score.config(text=(x, "-", o))
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2.config(bg="red", fg="green")
            b5.config(bg="red", fg="green")
            b8.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "X Won!")
            reset()
            x += 1
            score.config(text=(x, "-", o))
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3.config(bg="red", fg="green")
            b6.config(bg="red", fg="green")
            b9.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "X Won!")
            reset()
            x += 1
            score.config(text=(x, "-", o))
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.config(bg="red", fg="green")
            b5.config(bg="red", fg="green")
            b9.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "X Won!")
            reset()
            x += 1
            score.config(text=(x, "-", o))
        elif b7["text"] == "X" and b3["text"] == "X" and b5["text"] == "X":
            b7.config(bg="red", fg="green")
            b3.config(bg="red", fg="green")
            b5.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "X Won!")
            reset()
            x += 1
            score.config(text=(x, "-", o))
        if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1.config(bg="red", fg="green")
            b2.config(bg="red", fg="green")
            b3.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "O Won!")
            reset()
            o += 1
            score.config(text=(x, "-", o))
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg="red", fg="green")
            b5.config(bg="red", fg="green")
            b6.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "O Won!")
            reset()
            o += 1
            score.config(text=(x, "-", o))
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg="red", fg="green")
            b8.config(bg="red", fg="green")
            b9.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "O Won!")
            reset()
            o += 1
            score.config(text=(x, "-", o))
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b7.config(bg="red", fg="green")
            b4.config(bg="red", fg="green")
            b1.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "O Won!")
            reset()
            o += 1
            score.config(text=(x, "-", o))
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg="red", fg="green")
            b5.config(bg="red", fg="green")
            b8.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "O Won!")
            reset()
            o += 1
            score.config(text=(x, "-", o))
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.config(bg="red", fg="green")
            b6.config(bg="red", fg="green")
            b9.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "O Won!")
            reset()
            o += 1
            score.config(text=(x, "-", o))
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg="red", fg="green")
            b5.config(bg="red", fg="green")
            b9.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "O Won!")
            reset()
            o += 1
            score.config(text=(x, "-", o))
        elif b7["text"] == "O" and b3["text"] == "O" and b5["text"] == "O":
            b7.config(bg="red", fg="green")
            b3.config(bg="red", fg="green")
            b5.config(bg="red", fg="green")
            winner = True
            messagebox.showinfo("Match Result", "O Won!")
            reset()
            o += 1
            score.config(text=(x, "-", o))
        if count == 9 and winner == False:
            messagebox.showinfo("Match Result", " It's a tie!")
            reset()
            score.config(text=(x, "-", o))
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
    root = LabelFrame(win, text="", bg='#373737', width=540, height=520, fg="orange", padx=34,
                      pady=20)

    root.grid(row=0, column=0, padx=20, pady=20)

    def home():
        global homebtn

        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Converters App By Ezhil")
        alal = Label(root, bg="#373737", fg="light green", font=('Helvetica', 10, 'bold'),
                     text="                                                                                                               \n  Click any button for conversion    ",
                     justify="left").grid(row=0, column=0)
        kmmbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                        text="Kilometer to Meter", command=kmmpage)
        kmmbtn.grid(row=1, column=0, padx=20, pady=15)
        mkmbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                        text="Meter to Kilometer", command=mkmpage)
        mkmbtn.grid(row=2, column=0, padx=20, pady=15)
        ftcbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=22, pady=5, fg="#00C0FF",
                        text="Fahrenheit to Celcius", command=fahcel)
        ftcbtn.grid(row=3, column=0, padx=20, pady=15)
        ctfbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=22, pady=5, fg="#00C0FF",
                        text="Celcius to Fahrenheit", command=celfah)
        ctfbtn.grid(row=4, column=0, padx=20, pady=15)
        milekmbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                           text="Miles to Kilometers", command=milekmpage)
        milekmbtn.grid(row=5, column=0, padx=20, pady=15)
        kmmilebtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                           text="Kilometers to Miles", command=kmmilepage)
        kmmilebtn.grid(row=6, column=0, padx=20, pady=15)
        bmibtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                        text="Calculate your BMI", command=bmipage)
        bmibtn.grid(row=7, column=0, padx=20, pady=15)

        homebtn = Button(root, font=('Helvetica', 10, 'bold'), fg="#00C0FF", bg="#373737", text="Home",
                         command=hompg)
        homebtn.grid(row=7, column=2, pady=20)

    def kmmpage():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Kilometers to Meters")
        alal = Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                     text="                                                                                                               "
                          "\n  Enter KM value    ",
                     justify="left").grid(row=0, column=0)

        Km = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
                   fg="white")

        Km.grid(row=1, column=0)
        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid(row=2, column=0)

        def kmmfun():
            m = float(Km.get()) * 1000
            label.config(text=str(Km.get()) + "KM = " + str(round(m, 2)) + "meters")

        kmmconbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                           text="Convert",
                           command=kmmfun)
        kmmconbtn.grid(row=3, column=0, padx=20, pady=15)
        homebtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Home",
                         command=home).grid()

    def mkmpage():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Meters to Kilometers")
        alal = Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                     text="                                                                                                               "
                          "\n  Enter Meters value    ",
                     justify="left").grid(row=0, column=0)

        meters = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
                       fg="white")

        meters.grid()
        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid()

        def mkmfun():
            kilom = float(meters.get()) / 1000
            label.config(text=str(meters.get()) + " meters = " + str(round(kilom, 2)) + " KM")

        mkmconbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                           text="Convert",
                           command=mkmfun)
        mkmconbtn.grid(padx=20, pady=15)
        homebtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Home",
                         command=home).grid()

    def fahcel():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Fahrenheit to Celsius")
        alal = Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                     text="                                                                                                               "
                          "\n  Enter Fahrenheit value    ",
                     justify="left").grid(row=0, column=0)

        fah = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
                    fg="white")
        fah.grid()
        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid()

        def fahceldef():
            celcius = (float(fah.get()) - 32) * 5 / 9
            label.config(text=str(fah.get()) + " fahrenheit = " + str(round(celcius, 2)) + " celcius")

        ftcconbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                           text="Convert",
                           command=fahceldef)
        ftcconbtn.grid(padx=20, pady=15)
        homebtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Home",
                         command=home).grid()

    def celfah():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Celcius to Fahrenheit")
        alal = Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                     text="                                                                                                               "
                          "\n  Enter Celcius value    ",
                     justify="left").grid(row=0, column=0)

        cel = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
                    fg="white")

        cel.grid()
        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid()

        def celfahdef():
            fahreneit = (float(cel.get()) * 9 // 5) + 32
            label.config(text=str(cel.get()) + " celcius = " + str(round(fahreneit, 2)) + " fahrenheit")

        ctfconbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                           text="Convert",
                           command=celfahdef)
        ctfconbtn.grid(padx=20, pady=15)
        homebtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Home",
                         command=home).grid()

    def milekmpage():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Miles to Kilometers")
        alal = Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                     text="                                                                                                               "
                          "\n  Enter Miles value    ",
                     justify="left").grid(row=0, column=0)

        miles = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
                      fg="white")
        miles.grid()
        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid()

        def milekmfun():
            kilo = float(miles.get()) * 1.6
            label.config(text=str(miles.get()) + " miles = " + str(round(kilo, 2)) + " KM")

        milekmconbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                              text="Convert", command=milekmfun)
        milekmconbtn.grid(padx=20, pady=15)
        homebtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Home",
                         command=home).grid()

    def kmmilepage():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Convert Kilometers to Meters")
        alal = Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                     text="                                                                                                               "
                          "\n  Enter KM value    ",
                     justify="left").grid(row=0, column=0)

        kilometer = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right', bg="#373737",
                          fg="white")

        kilometer.grid()
        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid()

        def kmmilefun():
            mile = float(kilometer.get()) / 1.6
            label.config(text=str(kilometer.get()) + " KM = " + str(mile) + "Miles")

        kmmileconbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                              text="Convert", command=kmmilefun)
        kmmileconbtn.grid(padx=20, pady=15)
        homebtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Home",
                         command=home).grid(row=4, column=0, columnspan=4)

    def bmipage():
        for widget in win.winfo_children():
            widget.destroy()
        root = LabelFrame(win, text="App by Ezhil", bg='#373737', fg="orange", padx=40, pady=40)
        root.grid(row=0, column=0, padx=20, pady=20)
        root.config(text="Calculate your BMI")
        alal = Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                     text="                                                                                                               "
                          "\n  Enter your weight in KGs    ",
                     justify="left").grid()

        weight = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right',
                       bg="#373737",
                       fg="white")
        weight.grid(pady=20)
        aeal = Label(root, bg="#373737", fg="light blue", font=('Helvetica', 10, 'bold'),
                     text="                                                                                                               "
                          "\n  Enter your height in CMs    ",
                     justify="left").grid()

        height = Entry(root, width=15, font=('arial', 18, 'bold'), borderwidth=5, justify='right',
                       bg="#373737",
                       fg="white")
        height.grid(pady=20)
        label = Label(root, text="", bg="#373737", fg="orange", font=('arial', 18, 'bold'))
        label.grid()

        def bmifun():
            m = int(height.get()) / 100
            bmi = int(weight.get()) / (m * m)
            if bmi < 18.5:
                label.config(text="Your BMI is " + str(round(bmi, 2)) + "\nYou are underweight")
            if bmi > 18.5 and bmi < 24.9:
                label.config(text="Your BMI is " + str(round(bmi, 2)) + "\nYou are in normal weight")
            if bmi > 25 and bmi < 29.9:
                label.config(text="Your BMI is " + str(round(bmi, 2)) + "\nYou are overweight")
            if bmi > 30:
                label.config(text="Your BMI is " + str(round(bmi, 2)) + "\nYou are obese")

        bmiconbtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF",
                           text="Convert", command=bmifun)
        bmiconbtn.grid(padx=20, pady=15)
        homebtn = Button(root, font=('Helvetica', 10, 'bold'), bg="#373737", padx=30, pady=5, fg="#00C0FF", text="Home",
                         command=home).grid()

    home()

hompg()
win.mainloop()
