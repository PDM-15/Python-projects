from tkinter import *

#function for calculator operations
def get_digit(digit):
    current = result_label['text']
    new = current +str(digit)
    result_label.config(text=new)

def clear_result():
    result_label.config(text='')

def get_operator(op):
    global first_num, operator
    first_num = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_num, second_num, operator
    second_num = int(result_label['text'])

    if operator =='+':
        result_label.config(text = str(first_num + second_num))
    elif operator == '-':
        result_label.config(text = str(first_num - second_num))
    elif operator == '*':
        result_label.config(text = str(first_num * second_num))
    elif operator == '/':
        if second_num == 0:
            result_label.config(text = 'Error')
        else:
            result_label.config(text = str(first_num / second_num))

root = Tk()
root.title("Calculator")
root.geometry('280x380')
root.resizable(0, 0)
root.configure(bg='black')

#displaying the result part of the calculator
result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, column=0, columnspan=10, pady=(50,25), sticky='w')
result_label.config(font=('verdana', 30, 'bold'))

#Buttons of the calculator
btn7 = Button(root, text='7', bg='light gray', fg = 'black', width = 5, height = 2, command=lambda: get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana', 14, 'bold'))

btn8 = Button(root, text='8', bg='light gray', fg = 'black', width = 5, height = 2, command=lambda: get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana', 14, 'bold'))

btn9 = Button(root, text='9', bg='light gray', fg = 'black', width = 5, height = 2, command=lambda: get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana', 14, 'bold'))

btn_add = Button(root, text='+', bg='light gray', fg = 'black', width = 4, height = 2, command=lambda: get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana', 14, 'bold'))

btn4 = Button(root, text='4', bg='light gray', fg = 'black', width = 5, height = 2, command=lambda: get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana', 14, 'bold'))

btn5 = Button(root, text='5', bg='light gray', fg = 'black', width = 5, height = 2, command=lambda: get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana', 14, 'bold'))

btn6 = Button(root, text='6', bg='light gray', fg = 'black', width = 5, height = 2, command=lambda: get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana', 14, 'bold'))

btn_sub = Button(root, text='-', bg='light gray', fg = 'black', width = 4, height = 2, command=lambda: get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana', 14, 'bold'))

btn1 = Button(root, text='1', bg='light gray', fg = 'black', width = 5, height = 2, command=lambda: get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana', 14, 'bold'))

btn2 = Button(root, text='2', bg='light gray', fg = 'black', width = 5, height = 2, command=lambda: get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana', 14, 'bold'))

btn3 = Button(root, text='3', bg='light gray', fg = 'black', width = 5, height = 2, command=lambda: get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana', 14, 'bold'))

btn_mult = Button(root, text='*', bg='light gray', fg = 'black', width = 4, height = 2, command=lambda: get_operator('*'))
btn_mult.grid(row=3,column=3)
btn_mult.config(font=('verdana', 14, 'bold'))

btn0 = Button(root, text='0', bg='light gray', fg = 'black', width = 5, height = 2, command=lambda: get_digit(0))
btn0.grid(row=4,column=0)
btn0.config(font=('verdana', 14, 'bold'))

btneq = Button(root, text='=', bg='light gray', fg = 'black', width = 5, height = 2, command=get_result)
btneq.grid(row=4,column=1)
btneq.config(font=('verdana', 14, 'bold'))

btnclr = Button(root, text='C', bg='light gray', fg = 'black', width = 5, height = 2, command=lambda: clear_result())
btnclr.grid(row=4,column=2)
btnclr.config(font=('verdana', 14, 'bold'))

btndiv = Button(root, text='/', bg='light gray', fg = 'black', width = 4, height = 2, command=lambda: get_operator('/'))
btndiv.grid(row=4,column=3)
btndiv.config(font=('verdana', 14, 'bold'))

root.mainloop()