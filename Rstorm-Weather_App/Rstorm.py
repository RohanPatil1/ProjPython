#(Jul 2017)
#To Preview The Application, Go To :https://youtu.be/QXRNJpqMO2A
#---------------------------------------------------Tkinter--------------------------------------------------------------#

from Tkinter import *
import requests
import tkinter as tk,tkFont
from tkinter import Text, Tk


#-------------------------------------------------Root_config-------------------------------------------------------------#

root=Tk()
root.configure(background='#13366d')
root.geometry('425x425')
root.title('Rstorm - Weather App')

#-------------------------------------------------Fonts--------------------------------------------------------------------#
customFont = tkFont.Font(family="Product Sans", size=23)
customFontRe = tkFont.Font(family="Product Sans", size=23)
customFont1 = tkFont.Font(family="Product Sans", size=9)
customFont2 = tkFont.Font(family="Consolas", size=10)
customFont3 = tkFont.Font(family="Oswald", size=13)
customFontD = tkFont.Font(family="Pristina", size=11)
customFontR = tkFont.Font(family="Product Sans", size=11)
customFonttopL = tkFont.Font(family="Tempus Sans ITC", size=15)
customFont4 = tkFont.Font(family="Square721 BT", size=14)
customFont5 = tkFont.Font(family="Product Sans", size=27)

welcomeLabel=Label(root,text="Welcome To Our Weather App",font=customFont,bg="#13366d",fg="white")
welcomeLabel.place(relx=0.99, rely=0.14, anchor='se')




EnterNameL=Label(root,text="Enter City Name :  ",font=customFont3,bg="#13366d",fg="#f9e2ca")
EnterNameL.pack(side=LEFT)
EnterNameL.place(relx=0.4, rely=0.44, anchor='se')

citynameE=Entry(root,bd=3,width=24,bg="#fca549",fg="#161613",font=customFont1)
citynameE.place(relx=0.87, rely=0.44, anchor='se')



#----------------------------------------------Main_Process_on_Button_Press---------------------------------------------------#
def getWeather():
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + citynameE.get() + "&appid=57147502247fabc972b29ef5ce0c8a7a"

    data = requests.get(url)
    read = data.json()
#-----------------------------------------------STRINGVAR_CONFIGS------------------------------------------------------------#

    country=(format(read['sys']['country']))
    cityname=StringVar()
    cityname.set(format(read['name'])+","+country)
    wdescrip=StringVar()
    wdescrip.set(format(read['weather'][0]['description']).title())

    humidity=StringVar()
    humidity.set(format(read['main']['humidity'])+ " F")
    pressure=StringVar()
    pressure.set(format(read['main']['pressure'])+" atm")

    temp = float(format(read['main']['temp']))
    tempInC = float(temp - 273.14)
    temperature=StringVar()
    temperature.set(str(tempInC)+" C")
    windSpeed=StringVar()
    windSpeed.set(format(read['wind']['speed'])+" mph")
    clouds=StringVar()
    clouds.set(format(read['clouds']['all'])+ " %")
#-----------------------------------------DISPLAY_IT_TO_TOPLEVEL-------------------------------------------------------#
    top = Toplevel(root)
    top.geometry('430x430')
    top.configure(background='#13366d')


    tiltL=Label(top,text="--Weather Reports--",fg="White",font=customFontRe,bg="#13366d")
    tiltL.place(relx=0.84, rely=0.16, anchor='se')

    citynameL = Label(top,  textvariable=cityname,bg="#13366d", fg="#ce1a1a",font=customFont5)
    citynameL.place(relx=0.65, rely=0.3, anchor='se')

    Labeldescrip= Label(top, text="Weather Type : ", bg="#13366d",fg="#E4FEFF",font=customFonttopL)
    Labeldescrip.place(relx=0.38, rely=0.4, anchor='se')

    Labelhumidity = Label(top, text="Humidity : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)
    Labelhumidity.place(relx=0.38, rely=0.48, anchor='se')

    Labelpressure = Label(top, text="Pressure : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)
    Labelpressure.place(relx=0.38, rely=0.56, anchor='se')

    LabelWind = Label(top, text="Wind Speed : ", bg="#13366d",fg="#E4FEFF",font=customFonttopL)
    LabelWind.place(relx=0.38, rely=0.64, anchor='se')

    LabelClouds = Label(top, text="Clouds : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)
    LabelClouds.place(relx=0.38, rely=0.72, anchor='se')

    LabelTemp = Label(top, text="Temp : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)
    LabelTemp.place(relx=0.38, rely=0.8, anchor='se')

    wdescripL = Label(top, textvariable=wdescrip, bg="#13366d", fg="white",font=customFont4)
    wdescripL.place(relx=0.73, rely=0.398, anchor='se')

    humidityL = Label(top,  textvariable=humidity, bg="#13366d", fg="white")
    humidityL.place(relx=0.60, rely=0.47, anchor='se')
    
    pressureL = Label(top,textvariable=pressure, bg="#13366d", fg="white")
    pressureL.place(relx=0.62, rely=0.54, anchor='se')


    windSpeedL = Label(top,textvariable=windSpeed, bg="#13366d", fg="white")
    
    windSpeedL.place(relx=0.62, rely=0.62, anchor='se')
    cloudsL = Label(top, textvariable=clouds, bg="#13366d",fg="white")
    cloudsL.place(relx=0.59, rely=0.70, anchor='se')
    
    TempL = Label(top, textvariable=temperature, bg="#13366d", fg="white")
    TempL.place(relx=0.60, rely=0.79, anchor='se')





#-------------------------------------------------Root_config---------------------------------------------------------------#
b = Button(root, text="Get Weather !", command=getWeather,font=customFontR,bg="#ce1a1a",width=33,height=3,fg="white")
b.place(relx=0.83, rely=0.68, anchor='se')

deveL=Label(root,text="-Developed By Rohan",bg="#13366d",fg="white",font=customFontD)
deveL.place(relx=0.99, rely=0.99, anchor='se')

root.mainloop()

#-------------------------------------------Email:prorohan8@gmail.com------------------------------------------------------#
