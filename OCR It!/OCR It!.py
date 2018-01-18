
import os
from Tkinter import *



import subprocess
import os


root = Tk()
root.geometry('563x535')
root.title('OCR It !!')

customFont = tkFont.Font(family="Product Sans", size=38)
customFontRe = tkFont.Font(family="Product Sans", size=23)
customFont1 = tkFont.Font(family="Product Sans", size=12)
customFont2 = tkFont.Font(family="Consolas", size=10)
customFont3 = tkFont.Font(family="Oswald", size=13)
customFontD = tkFont.Font(family="Pristina", size=11)
customFontR = tkFont.Font(family="Product Sans", size=11)
customFonttopL = tkFont.Font(family="Tempus Sans ITC", size=15)
customFont4 = tkFont.Font(family="Square721 BT", size=14)
customFont5 = tkFont.Font(family="Product Sans", size=27)

welcomeLabel = Label(root, text="OCR It !!", font=customFont, bg="#EA0927", fg="white")
welcomeLabel.place(relx=0.61, rely=0.20, anchor='se')

DirNameL = Label(root, text="Enter Directory       :  ", font=customFont3, bg="#C8001C", fg="white")
DirNameL.place(relx=0.399, rely=0.55, anchor='se')

DirNameE = Entry(root, bd=3, width=24, bg="#fca549", fg="#161613", font=customFont1)
DirNameE.place(relx=0.87, rely=0.55, anchor='se')

ImageNameL = Label(root, text="Enter Image Name :  ", font=customFont3, bg="#D2001D", fg="white")
ImageNameL.place(relx=0.4, rely=0.44, anchor='se')

ImageNameE = Entry(root, bd=3, width=24, bg="#fca549", fg="#161613", font=customFont1)
ImageNameE.place(relx=0.87, rely=0.44, anchor='se')



FileNameL = Label(root, text="Enter Output Name     :  ", font=customFont3, bg="#C7001F", fg="white")
FileNameL.place(relx=0.4, rely=0.66, anchor='se')

FileNameE = Entry(root, bd=3, width=24, bg="#fca549", fg="#161613", font=customFont1)
FileNameE.place(relx=0.87, rely=0.66, anchor='se')






def hide():
    dirr = str(DirNameE.get())
    #str(DirNameE.get())
    os.chdir(dirr)
    code ='tesseract '+str(ImageNameE.get())+' '+FileNameE.get()
    subprocess.call(code, shell=True)



b = Button(root, text="Text It !",command=hide, bg="#ff0000", width=23, height=2,
        fg="white")
b.place(relx=0.64, rely=0.899, anchor='se')

root.mainloop()
