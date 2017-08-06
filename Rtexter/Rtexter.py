#(Aug 2017)GUI BUILD IN PYTHON BY Rohan Patil
#------------------------------------------------IMPORTS--------------------------------------------------------------------#
import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox



#-------------------------------------------------root_&_ScrollTextPad---------------------------------------------------------#
root=Tk()
root.title("Rtexter")
root.geometry('793x473')
root.configure(background='#00f4bb')
textPad = ScrolledText(root, width=40, height=50,font=('Raleway',18))               


#------------------------------------------------Functions_For_Menu------------------------------------------------------------#
def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()

def save_command():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        
        # To get Rid Of The Extra Last Character From Get, We Slice It Off
        data = textPad.get('1.0', END+'-1c')  
        file.write(data)
        file.close()
        
def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def about_command():
    label = tkMessageBox.showinfo("About", "Rtexter \nDeveloped By Rohan")
        
#------------------------------------------------Creating_Menu----------------------------------------------------------------#       
def dummy():
    print "I am a Dummy Command, I will be removed in the next step"
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)




#-----------------------------------------------------Packing----------------------------------------------------------------#       
textPad.pack()
root.bind('<Escape>',save_command )
root.mainloop()
#-------------------------------------------Email:prorohan8@gmail.com------------------------------------------------------#
