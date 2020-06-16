try:
    from tkinter import *
except ImportError:
    print('tkinter is not imported')

root = Tk()

root.geometry('345x480+450+100')
root.title('Calculator')
root.resizable(False,False)
intVar = IntVar()
entry = Entry(root,width=30,text=intVar,exportselection=0,borderwidth=10,font=('Helvetica',14))

cancel_image = PhotoImage(file="cancel.png")
plus_image = PhotoImage(file="plus.png")
minus_image = PhotoImage(file="minus.png")
multiply_image = PhotoImage(file="multiply.png")
divide_image = PhotoImage(file="divide.png")
percentage_image = PhotoImage(file="percent.png")
equal_image = PhotoImage(file="equal.png")

value = ""
first_value = ""
second_value = ""
final_value = first_value + second_value
sign_value = ""

try:
    def func_1(event=""):
        global first_value
        global second_value
        global value
        if entry.get() == 0:
            intVar.set(1)
        else:
            value += '1'
            first_value += '1'
            intVar.set(value)


    def func_2(event=""):
        global value
        global first_value
        if entry.get() == 0:
            intVar.set(2)
        else:
            value += '2'
            first_value += '2'
            intVar.set(value)


    def func_3(event=""):
        global value
        global first_value
        if entry.get() == 0:
            intVar.set(3)
        else:
            value += '3'
            first_value += '3'
            intVar.set(value)


    def func_4(event=""):
        global value
        global first_value
        if entry.get() == 0:
            intVar.set(4)
        else:
            value += '4'
            first_value += '4'
            intVar.set(value)


    def func_5(event=""):
        global value
        global first_value
        if entry.get() == 0:
            intVar.set(5)
        else:
            value += '5'
            first_value += '5'
            intVar.set(value)


    def func_6(event=""):
        global value
        global first_value
        if entry.get() == 0:
            intVar.set(6)
        else:
            value += '6'
            first_value += '6'
            intVar.set(value)


    def func_7(event=""):
        global value
        global first_value
        if entry.get() == 0:
            intVar.set(7)
        else:
            value += '7'
            first_value += '7'
            intVar.set(value)


    def func_8(event=""):
        global value
        global first_value
        if entry.get() == 0:
            intVar.set(8)
        else:
            value += '8'
            first_value += '8'
            intVar.set(value)


    def func_9(event=""):
        global value
        global first_value
        if entry.get() == 0:
            intVar.set(9)
        else:
            value += '9'
            first_value += '9'
            intVar.set(value)


    def func_0(event=""):
        global value
        global first_value
        if entry.get() == 0:
            intVar.set(0)
        else:
            value += '0'
            first_value += '0'
            intVar.set(value)


    def func_point(event=""):
        global value
        global first_value
        if entry.get() == 0:
            intVar.set(0)
        else:
            value += '.'
            first_value += '.'
            intVar.set(value)


    def func_plus(event=""):
        global value
        global first_value
        global second_value
        global final_value
        global sign_value
        if entry.get() == 0:
            intVar.set(0)
        else:
            second_value = float(first_value)
            first_value = ""

            value += '+'
            sign_value = '+'
            intVar.set(value)


    def func_minus(event=""):
        global value
        global first_value
        global second_value
        global final_value
        global sign_value
        if entry.get() == 0:
            intVar.set(0)
        else:
            second_value = float(first_value)
            first_value = ""

            value += '-'
            sign_value = "-"
            intVar.set(value)


    def func_multiply(event=""):
        global value
        global first_value
        global second_value
        global final_value
        global sign_value
        if entry.get() == 0:
            intVar.set(0)
        else:
            second_value = float(first_value)
            first_value = ""

            value += '*'
            sign_value = "*"
            intVar.set(value)


    def func_divide(event=""):
        global value
        global first_value
        global second_value
        global final_value
        global sign_value
        if entry.get() == 0:
            intVar.set(0)
        else:
            second_value = float(first_value)
            first_value = ""
            value += '/'
            sign_value = "/"
            intVar.set(value)


    def func_percentage(event=""):
        global value
        global first_value
        global second_value
        global final_value
        global sign_value
        if entry.get() == 0:
            intVar.set(0)
        else:
            second_value = float(first_value)
            # first_value = ""

            intVar.set(second_value / 100)


    def func_AC(event=""):

        global value
        global final_value
        global first_value
        global second_value
        if entry.get() == 0:
            intVar.set(0)
        else:
            value = ""
            final_value = 0
            first_value = ""
            second_value = ""
            intVar.set(0)


    def func_cancel(event=""):
        global value
        global new_value
        global first_value
        new_value = ""
        first_new_value = ""
        if entry.get() == 0:
            intVar.set(0)
        else:
            value_len = len(value)
            for i in range(len(value)):
                if i == (len(value)) - 1:
                    break
                new_value += value[i]
            for j in range(len(first_value)):
                if j == (len(first_value) - 1):
                    break
                first_new_value += first_value[j]

            value = new_value
            first_value = first_new_value
            intVar.set(value)


    def func_equal(event=""):
        global first_value
        global second_value
        global final_value
        if sign_value == '+':
            final_value = float(second_value) + float(first_value)
            intVar.set(final_value)
            second_value = ""
            first_value = final_value
        elif sign_value == '-':
            final_value = float(second_value) - float(first_value)
            intVar.set(final_value)
            second_value = ""
            first_value = final_value
        elif sign_value == '*':
            final_value = float(second_value) * float(first_value)
            intVar.set(final_value)
            second_value = ""
            first_value = final_value
        elif sign_value == '/':
            final_value = float(second_value) / float(first_value)
            intVar.set(final_value)
            second_value = ""
            first_value = final_value

        else:
            return


    entry.place(x=0, y=0)

    root.bind("0", func_0)
    root.bind("1", func_1)
    root.bind("2", func_2)
    root.bind("3", func_3)
    root.bind("4", func_4)
    root.bind("5", func_5)
    root.bind("6", func_6)
    root.bind("7", func_7)
    root.bind("8", func_8)
    root.bind("9", func_9)
    root.bind(".", func_point)

    root.bind("+", func_plus)
    root.bind("-", func_minus)
    root.bind("*", func_multiply)
    root.bind("/", func_divide)
    root.bind("%", func_percentage)
    root.bind("=", func_equal)
    root.bind("<BackSpace>", func_cancel)
    root.bind('<Escape>', func_AC)
    # first Layer
    button_AC = Button(root, text="AC", font=('Helvetica', 15, 'bold'), fg="red", width=6, height=3, command=func_AC,
                       borderwidth=3, relief=RAISED)
    button_cancel = Button(root, image=cancel_image, width=77, height=84, relief=RAISED, font=15, borderwidth=3,
                           command=func_cancel)
    button_divide = Button(root, image=divide_image, width=77, height=84, borderwidth=3, command=func_divide,
                           relief=RAISED)
    button_multiply = Button(root, image=multiply_image, width=77, height=84, borderwidth=3, command=func_multiply,
                             relief=RAISED)

    # Second Layer
    button_7 = Button(root, text='7', font=('Helvetica', 15, 'bold'), width=6, height=3, borderwidth=3, command=func_7,
                      relief=RAISED)
    button_8 = Button(root, text='8', font=('Helvetica', 15, 'bold'), width=6, height=3, borderwidth=3, command=func_8,
                      relief=RAISED)
    button_9 = Button(root, text='9', font=('Helvetica', 15, 'bold'), width=6, height=3, borderwidth=3, command=func_9,
                      relief=RAISED)
    button_minus = Button(root, image=minus_image, width=77, height=84, borderwidth=3, command=func_minus,
                          relief=RAISED)

    # Third Layer
    button_4 = Button(root, text='4', font=('Helvetica', 15, 'bold'), width=6, height=3, borderwidth=3, command=func_4,
                      relief=RAISED)
    button_5 = Button(root, text='5', font=('Helvetica', 15, 'bold'), width=6, height=3, borderwidth=3, command=func_5,
                      relief=RAISED)
    button_6 = Button(root, text='6', font=('Helvetica', 15, 'bold'), width=6, height=3, borderwidth=3, command=func_6,
                      relief=RAISED)
    button_plus = Button(root, image=plus_image, width=77, height=84, borderwidth=3, command=func_plus, relief=RAISED)

    # Fourth Layer
    button_1 = Button(root, text='1', font=('Helvetica', 15, 'bold'), width=6, height=3, borderwidth=3, command=func_1,
                      relief=RAISED)
    button_2 = Button(root, text='2', font=('Helvetica', 15, 'bold'), width=6, height=3, borderwidth=3, command=func_2,
                      relief=RAISED)
    button_3 = Button(root, text='3', font=('Helvetica', 15, 'bold'), width=6, height=3, borderwidth=3, command=func_3,
                      relief=RAISED)
    button_equal = Button(root, image=equal_image, bg="orange", width=77, height=152, borderwidth=3, command=func_equal,
                          relief=RAISED)

    # Fifth Layer
    button_percentage = Button(root, image=percentage_image, width=76, height=60, borderwidth=3,
                               command=func_percentage, relief=RAISED)
    button_0 = Button(root, text='0', font=('Helvetica', 15, 'bold'), width=6, height=2, borderwidth=3, command=func_0,
                      relief=RAISED)
    button_point = Button(root, text='.', font=('Helvetica', 15, 'bold'), width=6, height=2, borderwidth=3,
                          command=func_point, relief=RAISED)

    button_AC.place(x=3, y=40)
    button_cancel.place(x=88, y=40)
    button_divide.place(x=173, y=40)
    button_multiply.place(x=258, y=40)

    button_7.place(x=3, y=132)
    button_8.place(x=88, y=132)
    button_9.place(x=173, y=132)
    button_minus.place(x=258, y=132)

    button_4.place(x=3, y=224)
    button_5.place(x=88, y=224)
    button_6.place(x=173, y=224)
    button_plus.place(x=258, y=224)

    button_1.place(x=3, y=316)
    button_2.place(x=88, y=316)
    button_3.place(x=173, y=316)
    button_equal.place(x=258, y=316)

    button_percentage.place(x=3, y=408)
    button_0.place(x=88, y=408)
    button_point.place(x=173, y=408)

    mainloop()

except:
    print("--------------Something is wrong---------------")
    print("Debug Your Code")