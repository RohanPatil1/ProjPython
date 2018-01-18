#(Jul 2017)
#To Preview How It Works, Visit : https://www.youtube.com/watch?v=wA6plE3ukfk
#---------------------------------------------IMPORTS-----------------------------------------------------------------------#
import trunofficial
from Tkinter import *
import tkinter as tk,tkFont
from PIL import ImageTk,Image
from PIL import Image, ImageTk

# open a SPIDER image and convert to byte format

#----------------------------------------------CustomFonts-----------------------------------------------------------------------#

customFontRe = tkFont.Font(family="Vermin Vibes", size=31)
customFont3 = tkFont.Font(family="Oswald", size=13)
customFontD = tkFont.Font(family="Pristina", size=11)
customFontR = tkFont.Font(family="Product Sans", size=11)
customFonttopL = tkFont.Font(family="Tempus Sans ITC", size=15)
customFont4 = tkFont.Font(family="Sugarcubes", size=14)
customFont5 = tkFont.Font(family="Sugarcubes", size=27)

#---------------------------------------------TKINTER-ROOT CONFIG-------------------------------------------------------------#


root = Tk()  # A root window for displaying objects
root.geometry("420x322")
root.title('TrapCall')


tk_img = ImageTk.PhotoImage(file = 'image1.jpg')
canvas1 = Canvas(root, relief = FLAT,width = 410, height = 280)
canvas1.create_image(40, 80, image=tk_img)
canvas1.pack(fill=BOTH,expand=TRUE)
#---------------------------------------------CANVAS_WIDTGETS-------------------------------------------------------------#

labelT=Label(canvas1,text="TrapCall",fg="#05116d",bg='#DBDBDB',font=customFontRe)
label_windowT = canvas1.create_window(173, 18, anchor=N, window=labelT)


label=Label(canvas1,text="Enter Your Phone Number : ",fg="black",bg='#DBDBDB',font=customFont3)
label_window = canvas1.create_window(102, 100, anchor=N, window=label)

entry=Entry(canvas1,bd=4,width=26)
canvas1.create_window(282,118,window = entry)
#---------------------------------------------MAIN_FUNCTION -------------------------------------------------------------#

def getDetails():
    owner = trunofficial.search(entry.get())
    mobile = owner.phone

#----------------------------------------------STRINGVAR()---------------------------------------------------------------#
    mobile_numberI = StringVar()
    mobile_numberI.set(str(mobile.number))
    mobile_country_codeI = StringVar()
    mobile_carrierI = StringVar()
    mobile_cityI = StringVar()
    mobile_timeZoneI = StringVar()
    mobile_spamSC=StringVar()
#---------------------------------------------SETTING_TEXTVARIABLES-------------------------------------------------------------#
    mobile_country_codeI.set(str(mobile.countrycode))
    mobile_carrierI.set(str(mobile.carrier))
    house = owner.address
    mobile_cityI.set(house.city)
    mobile_timeZoneI.set(str(house.timezone))
    mobile_spamSC.set(str(mobile.spamscore))

#---------------------------------------------TKINTER-TOPLEVEL CONFIG-------------------------------------------------------------#
    top = Toplevel(root)
    top.geometry('460x430')
    top.configure(background='#DBDBDB')

#---------------------------------------------TOP-LABELS-------------------------------------------------------------#
    tiltL = Label(top, text="--Mobile Info--", fg="#05116d", font=customFontRe, bg="#DBDBDB")
    tiltL.place(relx=0.84, rely=0.16, anchor='se')

    mobile_numberL = Label(top, textvariable=mobile_numberI, bg="#DBDBDB", fg="#ce1a1a", font=customFont5)
    mobile_numberL.place(relx=0.70, rely=0.3, anchor='se')

    country_codeL = Label(top, text="Country Code : ",bg="#DBDBDB", fg="#894de2", font=customFonttopL)
    country_codeL.place(relx=0.38, rely=0.4, anchor='se')

    carrierL = Label(top, text="Carrier : ", bg="#DBDBDB", fg="#894de2", font=customFonttopL)
    carrierL.place(relx=0.38, rely=0.48, anchor='se')

    cityL = Label(top, text="City : ", bg="#DBDBDB", fg="#894de2", font=customFonttopL)
    cityL.place(relx=0.38, rely=0.56, anchor='se')

    timezoneL = Label(top, text="TimeZone : ", bg="#DBDBDB", fg="#894de2", font=customFonttopL)
    timezoneL.place(relx=0.38, rely=0.64, anchor='se')

    SCL = Label(top, text="Spam Votes : ", bg="#DBDBDB", fg="#894de2", font=customFonttopL)
    SCL.place(relx=0.38, rely=0.74, anchor='se')
#---------------------------------------------TOP-INFO-LABELS-------------------------------------------------------------#
    country_code_top = Label(top, textvariable=mobile_country_codeI, bg="#DBDBDB", fg="black", font=customFont4)
    country_code_top.place(relx=0.53, rely=0.398, anchor='se')

    country_carrier_top = Label(top, textvariable=mobile_carrierI, bg="#DBDBDB", fg="black", font=customFont4)
    country_carrier_top.place(relx=0.57, rely=0.483, anchor='se')
    country_city_top = Label(top, textvariable=mobile_cityI, bg="#DBDBDB", fg="black" ,font=customFont4)
    country_city_top.place(relx=0.58, rely=0.553, anchor='se')

    country_timeZone_top = Label(top, textvariable=mobile_timeZoneI, bg="#DBDBDB", fg="black", font=customFont4)
    country_timeZone_top.place(relx=0.62, rely=0.63, anchor='se')

    spamScore_top = Label(top, textvariable=mobile_spamSC, bg="#DBDBDB", fg="black", font=customFont4)
    spamScore_top.place(relx=0.58, rely=0.72, anchor='se')


#---------------------------------------------TKINTER-ROOT CONFIG-------------------------------------------------------------#

button1 = Button(root, text = "GET INFO",font=customFontR)
button1.configure(width=15,height=1, activebackground = "#33B5E5",bg="#894de2", relief = RAISED,command=getDetails)
button1_window = canvas1.create_window(192, 185, window=button1)

root.mainloop()

#----------------------------------EMAIL: prorohan8@gmail.com-------------------------------------------------------------------#
