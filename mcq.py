import tkinter as tk
from tkinter import messagebox
win=tk.Tk()
win.geometry("800x800")
win.title("mcq")


c=0
he=tk.Label(win,font="15",text="MCQ TEST:Select one option ",bg="orange")
he.pack()
a1=tk.IntVar()
a2=tk.IntVar()
a3=tk.IntVar()
a4=tk.IntVar()
a5=tk.IntVar()
a6=tk.IntVar()
a7=tk.IntVar()
a8=tk.IntVar()
a9=tk.IntVar()
a10=tk.IntVar()

def don():
    global c
    if(a1.get()==1):
        c=c+1
    if(a2.get()==4):
        c=c+1
    if(a3.get()==8):
        c=c+1
    if(a4.get()==10):
        c=c+1
    if(a5.get()==13):
        c=c+1
    if(a6.get()==18):
        c=c+1
    if(a7.get()==19):
        c=c+1
    if(a8.get()==23):
        c=c+1
    if(a9.get()==25):
        c=c+1
    if(a10.get()==28):
        c=c+1
    messagebox.showinfo("score","Your score is  "+str(c)+"/20") 
    
    
#def sub():
    #messagebox.showinfo("score","Your score is  "+str(c)+"/20")
def cal():
    print("answererd")
    


q1=tk.Label(win,font="15",text="1) What is a scripting language?")
q1.pack()
q11=tk.Radiobutton(win,font="12",text="JavaScript",value=1,variable=a1,command=cal)
q11.place(x=0,y=60)
q12=tk.Radiobutton(win,font="12",text="Oracle",value=2,variable=a1,command=cal)
q12.pack()
q13=tk.Radiobutton(win,font="12",text="SQL",value=3,variable=a1,command=cal)
q13.place(x=600,y=60)

q1=tk.Label(win,font="15",text="2) What created C language?")
q1.pack()
q11=tk.Radiobutton(win,font="12",text="Dennis Ricthe",value=4,variable=a2,command=cal)
q11.place(x=0,y=120)
q12=tk.Radiobutton(win,font="12",text="ken Thompsan",value=5,variable=a2,command=cal)
q12.pack()
q13=tk.Radiobutton(win,font="12",text="rob pike",value=6,variable=a2,command=cal)
q13.place(x=600,y=120)

q1=tk.Label(win,font="15",text="3) What created python language?")
q1.pack()
q11=tk.Radiobutton(win,font="12",text="Dennis Ricthe",value=7,variable=a3,command=cal)
q11.place(x=0,y=180)
q12=tk.Radiobutton(win,font="12",text="Guido van Rossum",value=8,variable=a3,command=cal)
q12.pack()
q13=tk.Radiobutton(win,font="12",text="rob pike",value=9,variable=a3,command=cal)
q13.place(x=600,y=180)

q1=tk.Label(win,font="15",text="4) Which keyword is used to create function in python?")
q1.pack()
q11=tk.Radiobutton(win,font="12",text="def",value=10,variable=a4,command=cal)
q11.place(x=0,y=240)
q12=tk.Radiobutton(win,font="12",text="global",value=11,variable=a4,command=cal)
q12.pack()
q13=tk.Radiobutton(win,font="12",text="func",value=12,variable=a4,command=cal)
q13.place(x=600,y=240)

#hh
q1=tk.Label(win,font="15",text="5) Which keyword is used to convert integer to string in python? ")
q1.pack()
q11=tk.Radiobutton(win,font="12",text="str",value=13,variable=a5,command=cal)
q11.place(x=0,y=315)
q12=tk.Radiobutton(win,font="12",text="tostring",value=14,variable=a5,command=cal)
q12.pack()
q13=tk.Radiobutton(win,font="12",text="stoi",value=15,variable=a5,command=cal)
q13.place(x=600,y=315)

q1=tk.Label(win,font="15",text="6) Which is a tuple?")
q1.pack()
q11=tk.Radiobutton(win,font="12",text="{}",value=16,variable=a6,command=cal)
q11.place(x=0,y=360)
q12=tk.Radiobutton(win,font="12",text="[]",value=17,variable=a6,command=cal)
q12.pack()
q13=tk.Radiobutton(win,font="12",text="()",value=18,variable=a6,command=cal)
q13.place(x=600,y=360)

q1=tk.Label(win,font="15",text="7)what is output of print(math.pow(3,2)) ")
q1.pack()
q11=tk.Radiobutton(win,font="12",text="9",value=19,variable=a7,command=cal)
q11.place(x=0,y=420)
q12=tk.Radiobutton(win,font="12",text="0",value=20,variable=a7,command=cal)
q12.pack()
q13=tk.Radiobutton(win,font="12",text="None",value=21,variable=a7,command=cal)
q13.place(x=600,y=420)

q1=tk.Label(win,font="15",text="8) How is a code block indicated in Python?")
q1.pack()
q11=tk.Radiobutton(win,font="12",text="bracket",value=22,variable=a8,command=cal)
q11.place(x=0,y=480)
q12=tk.Radiobutton(win,font="12",text="indentation",value=23,variable=a8,command=cal )
q12.pack()
q13=tk.Radiobutton(win,font="12",text="None",value=24,variable=a8,command=cal )
q13.place(x=600,y=480)
#jsk

q1=tk.Label(win,font="15",text="9) Which is correct extension of python file?")
q1.pack()
q11=tk.Radiobutton(win,font="12",text=".py",value=25,variable=a9,command=cal)
q11.place(x=0,y=540)
q12=tk.Radiobutton(win,font="12",text=".python",value=26,variable=a9,command=cal)
q12.pack()
q13=tk.Radiobutton(win,font="12",text=".po",value=27,variable=a9,command=cal)
q13.place(x=600,y=550)

q1=tk.Label(win,font="15",text="10) Which symbol is used a single line comment in python?")
q1.pack()
q11=tk.Radiobutton(win,font="12",text="#",value=28,variable=a10,command=cal)
q11.place(x=0,y=630)
q12=tk.Radiobutton(win,font="12",text="/",value=29,variable=a10,command=cal)
q12.pack()
q13=tk.Radiobutton(win,font="12",text="[",value=30,variable=a10,command=cal)
q13.place(x=600,y=630)




b1=tk.Button(win,font="30",text=" Submit and Check Your score",command=don,bg="red")
b1.pack()

