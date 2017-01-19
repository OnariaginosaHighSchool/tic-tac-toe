#use rowspan for making boxes be that big. 


from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox 
from PIL import Image, ImageTk


def switch1(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label1 = Label(image=photo)
    label1.image = photo # keep a reference!
    label1.grid(row=7, column =0 )
    
def switch2(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label2 = Label(image=photo)
    label2.image = photo # keep a reference!
    label2.grid(row=30, column =0 )
def switch3(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label3 = Label(image=photo)
    label3.image = photo # keep a reference!
    label3.grid(row=70, column =0 )
def switch4(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label4 = Label(image=photo)
    label4.image = photo # keep a reference!
    label4.grid(row=7, column =1 )
def switch5(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label5 = Label(image=photo)
    label5.image = photo # keep a reference!
    label5.grid(row=30, column =1 )
def switch6(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label6 = Label(image=photo)
    label6.image = photo # keep a reference!
    label6.grid(row=70, column =1 )
def switch7(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label7 = Label(image=photo)
    label7.image = photo # keep a reference!
    label7.grid(row=7, column =2 )
def switch8(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label8 = Label(image=photo)
    label8.image = photo # keep a reference!
    label8.grid(row=30, column =2 )
def switch9(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label9 = Label(image=photo)
    label9.image = photo # keep a reference!
    label9.grid(row=70, column =2 )


def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("You typed: ", entrytxt)
    
def openfileR():
    clearlist2()
    f = open("Readme.txt", "r")
    for line in f:

        name = line[0:-1]

    f.close()

def openfileW():
    f = open("Readme.txt", 'w')
    for i in names:    
        f.write(i + "\n") 
    

root = Tk() #gives us a blank canvas object to work with
root.title = ("GUI Program")




label1 = Label(root, text ="Player 1 Go First", bg="pink", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=2)





image = Image.open("blank.png")
image = image.resize((100,100))
photo = ImageTk.PhotoImage(image)
    

    
    
label1 = Label(image=photo)
label1.image = photo # keep a reference!
label1.grid(row=7, column =0 )
label1.bind("<Button-3>", switch1)

label2 = Label(image=photo)
label2.image = photo # keep a reference!
label2.grid(row=30, column =0 )
label2.bind("<Button-3>", switch2)

label3 = Label(image=photo)
label3.image = photo # keep a reference!
label3.grid(row=70, column =0 )
label3.bind("<Button-3>", switch3)

label4 = Label(image=photo)
label4.image = photo # keep a reference!
label4.grid(row=7, column =1 )
label4.bind("<Button-3>", switch4 )

label5 = Label(image=photo)
label5.image = photo # keep a reference!
label5.grid(row=30, column =1 )
label5.bind("<Button-3>", switch5)

label6 = Label(image=photo)
label6.image = photo # keep a reference!
label6.grid(row=70, column =1 )
label6.bind("<Button-3>", switch6 )

label7 = Label(image=photo)
label7.image = photo # keep a reference!
label7.grid(row=7, column =2 )
label7.bind("<Button-3>", switch7)

label8 = Label(image=photo)
label8.image = photo # keep a reference!
label8.grid(row=30, column =2 )
label8.bind("<Button-3>", switch8 )

label9 = Label(image=photo)
label9.image = photo # keep a reference!
label9.grid(row=70, column =2 )
label9.bind("<Button-3>", switch9)

def callback(event):
    print "clicked at", event.x, event.y

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_command(label="Save", command=openfileW)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)


mainloop() #causes the windows to display on the screen until program closes

