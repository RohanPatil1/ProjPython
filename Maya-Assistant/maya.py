

import wx
import os
import subprocess
# os.environ["HTTPS_PROXY"] = "http://user:pass@192.168.1.107:3128"
import wikipedia
import wolframalpha
import time
import webbrowser
import json
import requests
import random
import speech_recognition as sr
import Tkinter
import wx
import pyttsx3
import wikipedia
import wolframalpha
import os
import webbrowser
import json
try:
    from urllib.request  import urlopen
except ImportError:
    from urllib2 import urlopen

import codecs
import ctypes
import winshell
import re
import json
from urllib2 import urlopen
import trunofficial
import Tkinter
import Tkinter as tk,tkFont
#import tkinter as tk, tkFont
import ssl
from Tkinter import tkinter
import Tkinter as tk, tkFont
from Tkinter import Text, Tk

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# os.environ["HTTPS_PROXY"] = "http://user:pass@192.168.1.107:3128"


def tellIt(value):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 80)
    engine.say(value)
    engine.runAndWait()


# GUI creation
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          pos=wx.DefaultPosition, size=wx.Size(580, 285),
                          style=wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.RESIZE_BORDER |
                                wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                          title="MAYA")
        panel = wx.Panel(self)
        self.SetBackgroundColour('#ED1C24')
        ico = wx.Icon('funal.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

        my_sizer = wx.BoxSizer(wx.VERTICAL)

        lbl = wx.StaticText(self,
                            label="MAYA", pos=(155, 46))
        dlbl=wx.StaticText(self,label="-Developed By Rohan",pos=(405,213))
        dlbl.SetForegroundColour(('#FFFFFF'))
        fontd = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.BOLD, False, "Product Sans")
        dlbl.SetFont(fontd)
        font = wx.Font(36, wx.DECORATIVE, wx.NORMAL, wx.BOLD, False, "Jaapokki subtract")
        lbl.SetForegroundColour(('#FFFFFF'))
        lbl.SetFont(font)
        my_sizer.Add(lbl, 1, wx.ALL, 5)
        font1 = wx.Font(10, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, False, "Product Sans")
        self.txt = wx.TextCtrl(self, size=(400, 30), pos=(55, 120), style=wx.TE_PROCESS_ENTER)
        self.txt.SetFont(font1)
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        tellIt("Welcome, I am Maya ,   What can i do  for you  ?   ")

    def OnEnter(self, event):
        put = self.txt.GetValue()
        put = put.lower()
        link = put.split()
        if put == '':
            r = sr.Recognizer()
            with sr.Microphone() as src:
                audio = r.listen(src)
            try:
                put = r.recognize_google(audio)
                put = put.lower()
                link = put.split()
                self.txt.SetValue(put)

            except sr.UnknownValueError:
                tellIt("Our Voice Recognition could not understand audio")
                print("Our Voice Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google STT; {0}"
                      .format(e))
            except:
                print("Unknown exception occurred!")


                # ---------------------------------------SAY GO TO ' ___ ' TO OPEN WEBPAGE-------------------------->
        elif ('go to ') in put:
            try:
                # speak.Speak("opening " + link[2])
                tellIt("One Moment ")
                webbrowser.open('https://www.' + link[2] + '.com')
            except Exception as e:
                print(str(e))

        elif ('google') in put:
            try :
                name=str(put[7:])
                tellIt("On it")
                url="http://www.google.com/search?q="+name
                webbrowser.open_new_tab(url)
            except:
                print("Unknown exception occurred!")
                # -------------------------------------SAY OPEN ' ___ '  TO OPEN MS APPS-------------------->
        elif ('open') in put:
            if ('notepad') in put:
                try:
                    tellIt("On it")
                    os.system("notepad")
                except:
                    print("Unknown exception occurred!")

            elif ('paint') in put:
                try:
                    tellIt("One Moment")
                    subprocess.call('C:\Windows\System32\mspaint.exe')
                except:
                    print("Unknown exception occurred!")
            elif ('calculator') in put:
                try:
                    tellIt("On It")
                    subprocess.call('C:\Windows\System32\calc.exe')

                except:
                    print("Unknown exception occurred!")

            elif ('sound recorder') in put:
                try:
                    tellIt("One Moment ")
                    subprocess.call('C:\Windows\System32\SoundRecorder.exe')

                except:
                    print("Unknown exception occurred!")
            elif ('onscreen keyboard') in put:
                try:
                    tellIt("One Moment ")
                    subprocess.call('C:\Windows\System32\osk.exe')
                except:
                    print("Unknown exception occurred!")
            elif ('media player'):
                try:
                    tellIt("On It")
                    subprocess.call('C:\Program Files\Windows Media Player\wmplayer.exe')
                except:
                    print "ERROR"

        elif ('windows') in put:
            if ('shutdown') in put:
                try:
                    tellIt("doing")
                    subprocess.call(["shutdown", "/s"])
                except:
                    print("Unknown exception occurred!")
            elif ('restart') in put:
                try:
                    tellIt("One Moment ")
                    subprocess.call(["shutdown", "/r"])
                except:
                    print("Unknown exception occurred!")
            elif ('log out') in put:
                try:
                    tellIt("On it")
                    subprocess.call(["shutdown", "/l "])
                except:
                    print("Unknown exception occurred!")
            elif ('abort') in put:
                try:
                    tellIt("aborting")
                    subprocess.call(["shutdown", "/a "])
                except:
                    print("Unknown exception occurred!")
                    # -------------------------------------SAY OPEN ' ___ '  TO OPEN MS APPS-------------------->

        elif ('play the song') in put:
            name=(str(put[14:]).replace(' ','%20'))
            final=name
            
            url = ("http://gaana.com/song/" + final)
            
            webbrowser.open_new_tab(url )

        elif ('play the video') in put:
            
            #https://www.youtube.com/results?search_query=shape+of+you
            name=str(put[14:]).replace(' ','+')
           
            url = 'https://www.youtube.com/results?search_query=' + name
            webbrowser.open_new_tab(url)

        elif ('buy') in put:
            #https://www.flipkart.com/search?q=laptops
            name=str(put[4:])
            tellIt("On it")
            url=('https://www.flipkart.com/search?q=' + name)
            webbrowser.open_new_tab(url)

        elif ('empty recycle bin') in put:
            try:
                tellIt("Done")
                winshell.recycle_bin().empty(confirm=False,
                                             show_progress=False, sound=True)
            except:
                print("Unknown exception occurred!")

        elif ('thank you') in put:
            
            tellIt("Welcome!")

       

        
            
            

        elif("tell me the news for today") in put:
            jsonObj = urlopen(
                '''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=b75363e37d1d438596e3ab9d1966bef4''')

            i = 1
            reader = codecs.getreader("utf-8")
            data = json.load(reader(jsonObj))
            tellIt("Here are some of the headlines of today's news")
            for item in data['articles']:
                title=(str(i) + '. ' + item['title'] + '\n')
                decrip=(item['description'] + '\n')
                print title
                print decrip
                tellIt(title)
                tellIt(decrip)
                
                i += 1

        elif ('lock my computer') in put:
            try:
                tellIt("locking your device")
                ctypes.windll.user32.LockWorkStation()
            except:
                raise ('Error')

        elif ('get my location') in put:
            url = 'http://ipinfo.io/json'
            response = urlopen(url)
            data = json.load(response)
            IP = data['ip']
            org = data['org']
            city = str(data['city'])
            country = data['country']
            region = str(data['region'])
            print 'Your region is ,'+region+' ,' + country
            print 'and your current location is ' +city 
            tellIt('Your region is  ,'+ region +', country)
            tellIt('and your current location is ' +city )
        elif ('tell my detail location') in put:
            url = 'http://ipinfo.io/json'
            response = urlopen(url)
            data = json.load(response)
            IP = str(data['ip'])
            org = str(data['org'])
            city = str(data['city'])
            country = data['country']
            region = str(data['region'])
            print 'You are currently in  '+city +',' +region +' ,' + country
            print 'Your IP Adress is   ' + IP +'  from  a brodbrand connection company named as ' + org
            tellIt('You are currently in  '+city +',' +region + 'India')
            tellIt('Your IP Adress is '+IP+'from  a brodbrand connection company named as ' + org)

        elif ('send a mail') in put :
            
           
            tellIt("Initiating R  mailer the email application")
            import smtplib
            import Tkinter as tk, tkFont
            from Tkinter import Text, Tk
            
            import tkMessageBox
            # ----------------------------------------Function_To_Run_On_Button_Pressed------------------------------------------------------#

            def mainProccess():

                mail = smtplib.SMTP("smtp.gmail.com", 587)
                mail.ehlo()  # ehlo for the esmtp server (extended)
                mail.starttls()  # tls mode stands transport layer security which encrypts the next command
                mail.login(eEntry.get(), le.get())
                mail.sendmail(eEntry.get(), rme.get(), yme.get())
                tellIt("Message Sent")
                mail.close()

            # ------------------------------------------------Roots_&_Frames----------------------------------------------------------------#

            root = Tk()
            root.title("Rmailer")
            root.geometry('483x483')
            root.configure(background='#00f4bb')
            topframe = tk.Frame(root, width=230, height=200, bg='#00f4bb')
            topframe.pack()

            bottomFrame = tk.Frame()
            bottomFrame.pack(side=tk.BOTTOM)
            # --------------------------------------------------Custom_Fonts----------------------------------------------------------------#
            customFont = tkFont.Font(family="Magneto", size=18)
            customFont1 = tkFont.Font(family="Oswald", size=14)
            customFont2 = tkFont.Font(family="Raleway", size=10)

            customFontR = tkFont.Font(family="Gloria Hallelujah", size=11)
            customFontB = tkFont.Font(family="Century Gothic", size=17)

            # ------------------------------------------------TKINTER_BUILDS----------------------------------------------------------------#

            welcomeLabel = tk.Label(topframe, text="Welcome To Our Rmailer App", fg='#01256d', bg='#00f4bb',
                                 font=customFont)
            welcomeLabel.pack(side=tk.TOP)

            getButton = tk.Button(root, text="Send Mail !", width=20, height=4, command=mainProccess, relief=tk.RAISED,
                               bg='#65fc5f', font=customFontB, fg='#1a164f')
            getButton.place(relx=0.45, rely=0.4, anchor='s')

            elabel = tk.Label(root, text="Enter Your Mail :   ", bg='#00f4bb', fg='white', font=customFont1)
            elabel.place(relx=0.322, rely=0.600, anchor='se')

            eEntry = tk.Entry(root, bd=4, width=30, font=customFont2, bg="#ffff6b", fg="#0f0f01")
            eEntry.place(relx=0.83, rely=0.600, anchor='se')

            

            lr = tk.Label(root, text="Your Password :", bg='#00f4bb', fg='white', font=customFont1)
            lr.place(relx=0.299, rely=0.7, anchor='se')

            le = tk.Entry(root, bd=4, width=30, font=customFont2, show="*", bg="#ffff6b")
            le.place(relx=0.835, rely=0.7, anchor='se')

            rm = tk.Label(root, text="Receiver's Mail  :", bg='#00f4bb', fg='white', font=customFont1)
            rm.place(relx=0.308, rely=0.79, anchor='e')

            rme = tk.Entry(root, bd=4, width=30, font=customFont2, bg="#ffff6b")
            rme.place(relx=0.84, rely=0.8, anchor='e')

            ym = tk.Label(root, text="Your Message  :", bg='#00f4bb', fg='white', font=customFont1)
            ym.place(relx=0.298, rely=0.93, anchor='e')

            yme = tk.Entry(root, bd=4, width=30, font=customFont2, bg="#ffff6b")
            yme.place(relx=0.84, rely=0.93, anchor='e')

            root.mainloop()

            

        elif ('get weather details') in put:
           

            tellIt("Initiating Rstorn the weather app ")
            import requests
            import Tkinter as tk, tkFont
            from Tkinter import Text, Tk

            # -------------------------------------------------Root_config-------------------------------------------------------------#

            root = tk.Tk()
            root.configure(background='#13366d')
            root.geometry('425x425')
            root.title('Rstorm - Weather App')

            # -------------------------------------------------Fonts--------------------------------------------------------------------#
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

            welcomeLabel = tk.Label(root, text="Welcome To Our Weather App", font=customFont, bg="#13366d", fg="white")
            welcomeLabel.place(relx=0.99, rely=0.14, anchor='se')

            EnterNameL = tk.Label(root, text="Enter City Name :  ", font=customFont3, bg="#13366d", fg="#f9e2ca")
            EnterNameL.pack(side= tk.LEFT)
            EnterNameL.place(relx=0.4, rely=0.44, anchor='se')

            citynameE =  tk.Entry(root, bd=3, width=24, bg="#fca549", fg="#161613", font=customFont1)
            citynameE.place(relx=0.87, rely=0.44, anchor='se')

            # ----------------------------------------------Main_Process_on_Button_Press---------------------------------------------------#
            def getWeather():
                url = "http://api.openweathermap.org/data/2.5/weather?q=" + citynameE.get() + "&appid=57147502247fabc972b29ef5ce0c8a7a"

                data = requests.get(url)
                read = data.json()
                # -----------------------------------------------tk.StringVar_CONFIGS------------------------------------------------------------#

                country = (format(read['sys']['country']))
                cityname = tk.StringVar()
                cityname.set(format(read['name']) + "," + country)
                wdescrip = tk.StringVar()
                wdescrip.set(format(read['weather'][0]['description']).title())

                humidity = tk.StringVar()
                humidity.set(format(read['main']['humidity']) + " F")
                pressure = tk.StringVar()
                pressure.set(format(read['main']['pressure']) + " atm")

                temp = float(format(read['main']['temp']))
                tempInC = float(temp - 273.14)
                temperature = tk.StringVar()
                temperature.set(str(tempInC) + " C")
                windSpeed = tk.StringVar()
                windSpeed.set(format(read['wind']['speed']) + " mph")
                clouds = tk.StringVar()
                clouds.set(format(read['clouds']['all']) + " %")
                # -----------------------------------------DISPLAY_IT_TO_TOPLEVEL-------------------------------------------------------#
                top =  tk.Toplevel(root)
                top.geometry('430x430')
                top.configure(background='#13366d')

                tiltL =  tk.Label(top, text="--Weather Reports--", fg="White", font=customFontRe, bg="#13366d")
                tiltL.place(relx=0.84, rely=0.16, anchor='se')

                citynameL =  tk.Label(top, textvariable=cityname, bg="#13366d", fg="#ce1a1a", font=customFont5)
                citynameL.place(relx=0.65, rely=0.3, anchor='se')

                Labeldescrip = tk.Label(top, text="Weather Type : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)
                Labeldescrip.place(relx=0.38, rely=0.4, anchor='se')

                Labelhumidity =  tk.Label(top, text="Humidity : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)
                Labelhumidity.place(relx=0.38, rely=0.48, anchor='se')

                Labelpressure =  tk.Label(top, text="Pressure : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)
                Labelpressure.place(relx=0.38, rely=0.56, anchor='se')

                LabelWind =  tk.Label(top, text="Wind Speed : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)
                LabelWind.place(relx=0.38, rely=0.64, anchor='se')

                LabelClouds =  tk.Label(top, text="Clouds : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)
                LabelClouds.place(relx=0.38, rely=0.72, anchor='se')

                LabelTemp =  tk.Label(top, text="Temp : ", bg="#13366d", fg="#E4FEFF", font=customFonttopL)
                LabelTemp.place(relx=0.38, rely=0.8, anchor='se')

                wdescripL =  tk.Label(top, textvariable=wdescrip, bg="#13366d", fg="white", font=customFont4)
                wdescripL.place(relx=0.73, rely=0.398, anchor='se')

                humidityL =  tk.Label(top, textvariable=humidity, bg="#13366d", fg="white")
                humidityL.place(relx=0.60, rely=0.47, anchor='se')

                pressureL =  tk.Label(top, textvariable=pressure, bg="#13366d", fg="white")
                pressureL.place(relx=0.62, rely=0.54, anchor='se')

                windSpeedL =  tk.Label(top, textvariable=windSpeed, bg="#13366d", fg="white")

                windSpeedL.place(relx=0.62, rely=0.62, anchor='se')
                cloudsL =  tk.Label(top, textvariable=clouds, bg="#13366d", fg="white")
                cloudsL.place(relx=0.59, rely=0.70, anchor='se')

                TempL =  tk.Label(top, textvariable=temperature, bg="#13366d", fg="white")
                TempL.place(relx=0.60, rely=0.79, anchor='se')

            # -------------------------------------------------Root_config---------------------------------------------------------------#
            b =  tk.Button(root, text="Get Weather !", command=getWeather, font=customFontR, bg="#ce1a1a", width=33,
                       height=3, fg="white")
            b.place(relx=0.83, rely=0.68, anchor='se')

            deveL =  tk.Label(root, text="-Developed By Rohan", bg="#13366d", fg="white", font=customFontD)
            deveL.place(relx=0.99, rely=0.99, anchor='se')

            root.mainloop()

         

        elif ('get call details') in put :
   
            import Tkinter as tk, tkFont
            from Tkinter import Text, Tk
            import trunofficial
            import Tkinter 
            import Tkinter as tk,tkFont
            from PIL import ImageTk,Image
            from PIL import Image, ImageTk


    

    

            customFontRe = tkFont(family="Vermin Vibes", size=31)
            customFont3 = Font(family="Oswald", size=13)
            customFontD = Font(family="Pristina", size=11)
            customFontR = Font(family="Product Sans", size=11)
            customFonttopL = Font(family="Tempus Sans ITC", size=15)
            customFont4 = Font(family="Sugarcubes", size=14)
            customFont5 = Font(family="Sugarcubes", size=27)

    # ---------------------------------------------TKINTER-ROOT CONFIG-------------------------------------------------------------#


            root =  Tk()  # A root window for displaying objects
            root.geometry("420x322")
            root.title('TrapCall')
            customFontRe = tkFont.Font(root,family="Vermin Vibes", size=31)
            customFont3 = Font(family="Oswald", size=13)
            customFontD = Font(family="Pristina", size=11)
            customFontR = Font(family="Product Sans", size=11)
            customFonttopL = Font(family="Tempus Sans ITC", size=15)
            customFont4 = Font(family="Sugarcubes", size=14)
            customFont5 = Font(family="Sugarcubes", size=27)

            tk_img = ImageTk.PhotoImage(file='image1.jpg')
            canvas1 =  tk.Canvas(root, relief=FLAT, width=410, height=280)
            canvas1.create_image(40, 80, image=tk_img)
            canvas1.pack(fill=BOTH, expand=TRUE)
    # ---------------------------------------------CANVAS_WIDTGETS-------------------------------------------------------------#

            labelT =  tk.Label(canvas1, text="TrapCall", fg="#05116d", bg='#DBDBDB', font=customFontRe)
            label_windowT = canvas1.create_window(173, 18, anchor=N, window=labelT)

            label =  tk.Label(canvas1, text="Enter Your Phone Number : ", fg="black", bg='#DBDBDB', font=customFont3)
            label_window = canvas1.create_window(102, 100, anchor=N, window=label)

            entry =  tk.Entry(canvas1, bd=4, width=26)
            canvas1.create_window(282, 118, window=entry)

    # ---------------------------------------------MAIN_FUNCTION -------------------------------------------------------------#

            def getDetails():
                owner = trunofficial.search(entry.get())
                mobile = owner.phone

        # ----------------------------------------------tk.StringVar()---------------------------------------------------------------#
                mobile_numberI = tk.StringVar()
                mobile_numberI.set(str(mobile.number))
                mobile_country_codeI = tk.StringVar()
                mobile_carrierI = tk.StringVar()
                mobile_cityI = tk.StringVar()
                mobile_timeZoneI = tk.StringVar()
                mobile_spamSC = tk.StringVar()
        # ---------------------------------------------SETTING_TEXTVARIABLES-------------------------------------------------------------#
                mobile_country_codeI.set(str(mobile.countrycode))
                mobile_carrierI.set(str(mobile.carrier))
                house = owner.address
                mobile_cityI.set(house.city)
                mobile_timeZoneI.set(str(house.timezone))
                mobile_spamSC.set(str(mobile.spamscore))

        # ---------------------------------------------TKINTER-TOPLEVEL CONFIG-------------------------------------------------------------#
                top =  tk.Toplevel(root)
                top.geometry('460x430')
                top.configure(background='#DBDBDB')

        # ---------------------------------------------TOP-LABELS-------------------------------------------------------------#
                tiltL =  tk.Label(top, text="--Mobile Info--", fg="#05116d", font=customFontRe, bg="#DBDBDB")
                tiltL.place(relx=0.84, rely=0.16, anchor='se')

                mobile_numberL =  tk.Label(top, textvariable=mobile_numberI, bg="#DBDBDB", fg="#ce1a1a", font=customFont5)
                mobile_numberL.place(relx=0.70, rely=0.3, anchor='se')

                country_codeL =  tk.Label(top, text="Country Code : ", bg="#DBDBDB", fg="#894de2", font=customFonttopL)
                country_codeL.place(relx=0.38, rely=0.4, anchor='se')

                carrierL =  tk.Label(top, text="Carrier : ", bg="#DBDBDB", fg="#894de2", font=customFonttopL)
                carrierL.place(relx=0.38, rely=0.48, anchor='se')

                cityL =  tk.Label(top, text="City : ", bg="#DBDBDB", fg="#894de2", font=customFonttopL)
                cityL.place(relx=0.38, rely=0.56, anchor='se')

                timezoneL =  tk.Label(top, text="TimeZone : ", bg="#DBDBDB", fg="#894de2", font=customFonttopL)
                timezoneL.place(relx=0.38, rely=0.64, anchor='se')

                SCL =  tk.Label(top, text="Spam Votes : ", bg="#DBDBDB", fg="#894de2", font=customFonttopL)
                SCL.place(relx=0.38, rely=0.74, anchor='se')
        # ---------------------------------------------TOP-INFO-LABELS-------------------------------------------------------------#
                country_code_top =  tk.Label(top, textvariable=mobile_country_codeI, bg="#DBDBDB", fg="black", font=customFont4)
                country_code_top.place(relx=0.53, rely=0.398, anchor='se')

                country_carrier_top =  tk.Label(top, textvariable=mobile_carrierI, bg="#DBDBDB", fg="black", font=customFont4)
                country_carrier_top.place(relx=0.57, rely=0.483, anchor='se')
                country_city_top =  tk.Label(top, textvariable=mobile_cityI, bg="#DBDBDB", fg="black", font=customFont4)
                country_city_top.place(relx=0.58, rely=0.553, anchor='se')

                country_timeZone_top =  tk.Label(top, textvariable=mobile_timeZoneI, bg="#DBDBDB", fg="black", font=customFont4)
                country_timeZone_top.place(relx=0.62, rely=0.63, anchor='se')

                spamScore_top =  tk.Label(top, textvariable=mobile_spamSC, bg="#DBDBDB", fg="black", font=customFont4)
                spamScore_top.place(relx=0.58, rely=0.72, anchor='se')

    # ---------------------------------------------TKINTER-ROOT CONFIG-------------------------------------------------------------#

            button1 =  tk.Button(root, text="GET INFO", font=customFontR)
            button1.configure(width=15, height=1, activebackground="#33B5E5", bg="#894de2", relief=RAISED, command=getDetails)
            button1_window = canvas1.create_window(192, 185, window=button1)

            root.mainloop()

  







        else :
                query = put[:]
                try:
                    # wolframalpha
                    client = wolframalpha.Client(app_id)
                    res = client.query(put)
                    ans = next(res.results).text
                    print ans
                    tellIt(ans)

                except:
                # wikipedia

                # print(put)
                    print (wikipedia.summary(query))
                    tellIt(wikipedia.summary(query))


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()


