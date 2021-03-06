from tkinter import *
import cmath
import math

class calc():
    def __init__(self):
        self.arithmatic_operator = ""
        self.result = False
        self.check_sum = False
        self.total = 0
        self.dontdeletezero = False
        self.input_value = True
        self.current = "0"
        self.ans = "0"

    def display(self,value):
        textDisplay.delete(0,END)
        textDisplay.insert(0, value)

    def clear_entry(self):
        self.result = False
        self.input_value = True
        self.dontdeletezero = False
        self.current = ""
        self.display(str(self.total) + self.current)

    def ansr(self):
        self.current = self.ans
        if self.total == 0:
            self.display(self.ans)
        elif self.total != 0:
            self.display(str(self.total) + self.ans)


    def nument(self,num):
        self.result = False
        scdnum = str(num)
        if self.current == "0":
            if self.dontdeletezero == False:
                self.current = scdnum
                if self.total != 0:
                    self.display(str(self.total) + self.current)
                else:
                    self.display(self.current)
            else:
                self.current += scdnum
                self.display(str(self.total) + self.current)
                self.dontdeletezero = False
        elif self.total == 0:
            textDisplay.delete(0)
            self.current += scdnum
            self.input_value = False
            self.display(self.current)
        else:
            self.current += scdnum
            self.display(str(self.total) + self.current)


    def clear_all_entry(self):
        self.clear_entry()
        self.total = 0
        self.display("0")

    def pm(self):
        self.result = False
        self.dontdeletezero = False
        self.current = (textDisplay.get())
        try:
            a = float(textDisplay.get()).is_integer()
        except:
            a = textDisplay.get()

        if a == True:
            if textDisplay.get() ==  "0":
                self.current = (textDisplay.get())
            elif str(textDisplay.get())[0] == "-":
                self.current = str(textDisplay.get())[1:]
            else:
                self.current = -(float(textDisplay.get()))
        else:
            if float(eval(textDisplay.get()))< 0:
                self.current = str(eval(textDisplay.get()))[1:]
            else:
                self.current = "-" + str(eval(textDisplay.get()))
        self.display(self.current)
        self.current = ""

    def sqrt(self):
        self.result = False
        self.dontdeletezero = False
        try:
            a = float(eval(textDisplay.get()))
        except:
            self.display("ErrOr")
            return

        if a < 0:
            self.current = cmath.sqrt(a)

        elif a>= 0:
            self.current = round(math.sqrt(a),3)
        self.display(self.current)
        self.current = ""

    def dt(self):
        self.result = False
        self.current += "."
        self.input_value = False
        self.dontdeletezero = True
        if self.total == 0:
            self.current = "0."
            self.display(self.current)
        else:
            self.display(str(self.total) + self.current)

    def zr(self):
        self.result = False
        if textDisplay.get() != "0":
            self.current = textDisplay.get()+"0"
        else:
            self.current = "0"
        self.display(self.current)
        self.current = ""

    def art_op(self,op):
        self.result = False
        self.input_value = False
        self.dontdeletezero = False
        self.current = ""
        i = textDisplay.get()
        o = ["+", "-","*","/"]
        if textDisplay.get()[-1] in o:
            self.arithmatic_operator = str(op)
            textDisplay.delete(len(textDisplay.get())-1)
            self.total = textDisplay.get()+ op
        else:
            self.total = textDisplay.get()+ op
        self.display(self.total)

    def eql(self):
        self.result = True
        self.total = textDisplay.get()
        self.dontdeletezero = False
        try:
            self.current  = eval(self.total)
            self.display(round(self.current, 5))
        except:
            self.current = "ERROR"
            self.display(self.current)
        self.current = ""
        self.input_value = True
        self.arithmatic_operator == ""
        self.total = 0
        self.ans = textDisplay.get()

added_value = calc()
rt = Tk()
rt.title("Calculator")
rt.resizable(width = False, height  = False)
calc1 = Frame(rt)
calc1.grid()
calc = Frame(rt)
calc.grid()
calc2 = Frame(rt)
calc2.grid(column=0, row=2,padx = 1, sticky="nsew", columnspan=1)



textDisplay = Entry(calc1, bg = "#182d4d", fg = "powder blue", font = ("arial" ,21, "bold"),justify = LEFT, bd = 15, width = 23)
textDisplay.grid(row = 0, column = 0, columnspan = 4, pady = 1)
textDisplay.insert(0,"0")


btnC = (Button(calc, height=2, width=5, text="C" , font=("arial", 20, "bold"), bd=4,command = added_value.clear_entry,fg = "powder blue",bg = "#0c3a77"))
btnC.grid(row = 1, column = 0 , pady = 1)
btnCE = (Button(calc, height=2, width=5, text="CE" , font=("arial", 20, "bold"), bd=4, command = added_value.clear_all_entry,fg = "powder blue",bg = "#0c3a77"))
btnCE.grid(row = 1, column = 1 , pady = 1)
btnsqrt = (Button(calc, height=2, width=5, text="√" , font=("arial", 20, "bold"), bd=4, command = added_value.sqrt,fg = "powder blue",bg = "#0c3a77"))
btnsqrt.grid(row = 1, column =2 , pady = 1)

btndiv = (Button(calc, height=2, width=5, text="/" , font=("arial", 20, "bold"), bd=4,fg = "powder blue",bg = "#0c3a77"))
btndiv.grid(row = 1, column = 3 , pady = 1)
btndiv["command"] = lambda x = "/":added_value.art_op(x)
btnmul = (Button(calc, height=2, width=5, text="*" , font=("arial", 20, "bold"), bd=4,fg = "powder blue",bg = "#0c3a77"))
btnmul.grid(row = 2, column = 3 , pady = 1)
btnmul["command"] = lambda x = "*":added_value.art_op(x)
btnadd = (Button(calc, height=2, width=5, text="+" , font=("arial", 20, "bold"), bd=4,fg = "powder blue",bg = "#0c3a77"))
btnadd.grid(row = 3, column = 3 , pady = 1)
btnadd["command"] = lambda x = "+":added_value.art_op(x)
btnsub = (Button(calc, height=2, width=5, text="-" , font=("arial", 20, "bold"), bd=4,fg = "powder blue",bg = "#0c3a77"))
btnsub.grid(row = 4, column = 3 , pady = 1)
btnsub["command"] = lambda x = "-":added_value.art_op(x)

btnzr = (Button(calc, height=2, width=5, text="0" , font=("arial", 20, "bold"), bd=4,fg = "sky blue",bg = "#182d4d"))
btnzr.grid(row = 5, column = 1 , pady = 1)
btnzr["command"] = lambda x = "0":added_value.nument(x)
btndt = (Button(calc, height=2, width=5, text="." , font=("arial", 20, "bold"), bd=4, command = added_value.dt,fg = "powder blue",bg = "#0c3a77"))
btndt.grid(row = 5, column = 2 , pady = 1)
btnas = (Button(calc, height=2, width=5, text="±" , font=("arial", 20, "bold"), bd=4, command = added_value.pm,fg = "powder blue",bg = "#0c3a77"))
btnas.grid(row = 5, column = 0 , pady = 1)
btneq = (Button(calc, height=2, width=5, text="=" , font=("arial", 20, "bold"), bd=4, command = added_value.eql,fg = "white",bg = "#f40e23"))
btneq.grid(row = 5, column = 3 , pady = 1)

btnans = (Button(calc2, height=2, text="Ans" , font=("arial", 21, "bold"), bd=4, command = added_value.ansr,fg = "powder blue",bg = "#0c3a77"))
btnans.pack(expand = True, fill = "x")

numpad = [7,8,9,4,5,6,1,2,3,]
q = 0
for i in range(2,5):
    for j in range(3):
        btn = (Button(calc,height = 2, width = 5,text = str(numpad[q]), font = ("arial" ,20, "bold") ,bd = 4,fg = "sky blue",bg = "#182d4d"))
        btn.grid(row = i, column = j , pady = 1)
        btn["command"] = lambda x = numpad[q]:added_value.nument(x)
        q += 1

rt.mainloop()
