
#(Jul 2017)GUI BUILD IN PYTHON BY Rohan Patil
#
#----------------------------------------------Python_Imports-------------------------------------------------------------------#

import smtplib
import tkinter as tk,tkFont
from tkinter import Text, Tk
from Tkinter import *
import tkMessageBox
#----------------------------------------Function_To_Run_On_Button_Pressed------------------------------------------------------#

def mainProccess():

    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()  # ehlo for the esmtp server (extended)
    mail.starttls()  # tls mode stands transport layer security which encrypts the next command
    mail.login(eEntry.get(), le.get())
    mail.sendmail(eEntry.get(), rme.get(), yme.get())
    mail.close()






# ------------------------------------------------Roots_&_Frames----------------------------------------------------------------#

root=Tk()
root.title("Rmailer")
root.geometry('453x453')
root.configure(background='#00f4bb')
topframe=Frame(root,width=210, height=200,bg='#00f4bb')
topframe.pack()

bottomFrame=Frame()
bottomFrame.pack(side=BOTTOM)
# --------------------------------------------------Custom_Fonts----------------------------------------------------------------#
customFont = tkFont.Font(family="Magneto", size=18)
customFont1 = tkFont.Font(family="Oswald", size=14)
customFont2 = tkFont.Font(family="Raleway", size=10)

customFontR = tkFont.Font(family="Gloria Hallelujah", size=11)
customFontB=tkFont.Font(family="Century Gothic",size=17)

# ------------------------------------------------TKINTER_BUILDS----------------------------------------------------------------#

welcomeLabel=Label(topframe,text="Welcome To Our Rmailer App",fg='#01256d',bg='#00f4bb',font=customFont)
welcomeLabel.pack(side=TOP)

getButton=Button(root,text="Send Mail !",width=20,height=4,command=mainProccess,relief=RAISED,bg='#65fc5f',font=customFontB,fg='#1a164f')
getButton.place(relx=0.45, rely=0.4, anchor='s')



elabel=Label(root,text="Enter Your Mail :   ",bg='#00f4bb',fg='white',font=customFont1)
elabel.pack(side=LEFT)

eEntry=Entry(root,bd=4,width=30,font=customFont2,bg="#ffff6b",fg="#0f0f01")
eEntry.pack(side=LEFT)

print "\n"

lr=Label(root,text="Your Password :",bg='#00f4bb',fg='white',font=customFont1)
lr.place(relx=0.26, rely=0.7, anchor='se')

le=Entry(root,bd=4,width=30,font=customFont2,show="*",bg="#ffff6b")
le.place(relx=0.835, rely=0.7, anchor='se')

rm=Label(root,text="Receiver's Mail  :",bg='#00f4bb',fg='white',font=customFont1)
rm.place(relx=0.28, rely=0.79, anchor='e')

rme=Entry(root,bd=4,width=30,font=customFont2,bg="#ffff6b")
rme.place(relx=0.84, rely=0.8, anchor='e')

ym=Label(root,text="Your Message  :",bg='#00f4bb',fg='white',font=customFont1)
ym.place(relx=0.25, rely=0.93, anchor='e')

yme=Entry(root,bd=4,width=30,font=customFont2,bg="#ffff6b")
yme.place(relx=0.84, rely=0.93, anchor='e')

root.mainloop()

#--------------------------------------------------Email:prorohan8@gmail.com--------------------------------------------------#

