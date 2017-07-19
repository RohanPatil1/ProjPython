from Tkinter import *

import wikipedia


import tkinter as tk,tkFont
root=Tk()
root.configure(background='#F50A44')
root.geometry('423x423')
root.title('AskMeAnyThing App')
topframe=Frame(root,width=210, height=200,bg='#F50A44')
topframe.pack()

customFont = tkFont.Font(family="Gloria Hallelujah", size=16)
customFont1 = tkFont.Font(family="Oswald", size=14)
customFont2 = tkFont.Font(family="Consolas", size=10)
customFont3 = tkFont.Font(family="Oswald", size=10)
customFontR = tkFont.Font(family="Gloria Hallelujah", size=11)

welcomeLabel=Label(topframe,text="Welcome To Our AskMeAnyThing App",fg='#d8ff4f',font=customFont,bg='#F50A44')

welcomeLabel.pack(side=TOP)

qlabel=Label(topframe,text="Enter Your Question : ",bg='#F50A44',font=customFont1,fg='white')

qlabel.pack(side=LEFT,pady=90)
E1=Entry(topframe,bd=3,bg='#01799e',width=36,fg='white',font=customFont2)

E1.pack(side=LEFT,pady=90)


def getQue():


        question = E1.get()
        ans = StringVar()
        window = Toplevel(topframe)
        window.configure(background='#F50A44')
        l=Message(window,textvariable=ans)
        l.pack()


       


        
        # wikipedia api
        answer1 =wikipedia.summary(question)
        ans.set(answer1)

getButton=Button(topframe,text="Get Answer!",command=getQue,width=20,height=2,relief=RAISED,bg='#65fc5f',font=customFont3)
getButton.place(relx=0.5, rely=1.0, anchor='s')

lr=Label(root,text="- Developed By Rohan",bg='#F50A44',fg='#d8ff4f',font=customFontR)
lr.place(relx=1.0, rely=1.0, anchor='se')
root.mainloop()

root.mainloop()
