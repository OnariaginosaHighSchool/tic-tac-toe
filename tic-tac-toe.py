#rowspan for making boxes be that big. 


from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox 
from PIL import Image, ImageTk

#check
count = 0

x = [10, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

All = [x,y,z]

player1 = 0

player2 = 1



def winner():
    label0.config(text="winner")

def tie():
    label0.config(text="tie")


def nextplayer():
    print" "

#vertical check
def vcheck():
    if All[0][0] == All[0][1] == All[0][2]:
        winner()
    if All[1][0] == All[1][1] == All[1][2]:
        winner()
    if All[2][0] == All[2][1] == All[2][2]:
        winner()
    else:
        nextplayer()
        
#horizontal check
def hcheck():
    if All[0][0] == All[1][0] == All[2][0]:
        winner()
    if All[0][1] == All[1][1] == All[2][1]:
        winner()
    if All[0][2] == All[1][2] == All[2][2]:
        winner()
    else:
        nextplayer()
        
#diagonal check
def dcheck():
    if All[0][0] == All[1][1] == All[2][2]:
        winner()
    if All[2][0] == All[1][1] == All[0][2]:
        winner()
    else:
        nextplayer()


def check():
    global count
    if count == 9:
        tie()
    else:
        hcheck()
        vcheck()
        dcheck()
        count =+1
        if count == 9:
            tie()

    
def switch1(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)
    
    label1 = Label(image=photo)
    label1.image = photo # keep a reference!
    label1.grid(row=7, column =0 )
    All[0][0] = player2
    label0.config(text="left click turn")
    check()
    
def switch2(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label2 = Label(image=photo)
    label2.image = photo # keep a reference!
    label2.grid(row=30, column =0 )
    All[0][1] = player2
    label0.config(text="left click turn")
    check()
    
def switch3(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label3 = Label(image=photo)
    label3.image = photo # keep a reference!
    label3.grid(row=70, column =0 )
    All[0][2] = player2
    label0.config(text="left click turn")
    check()
    
def switch4(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label4 = Label(image=photo)
    label4.image = photo # keep a reference!
    label4.grid(row=7, column =1 )
    All[1][0] = player2
    label0.config(text="left click turn")
    check()
    
def switch5(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label5 = Label(image=photo)
    label5.image = photo # keep a reference!
    label5.grid(row=30, column =1 )
    All[1][1] = player2
    label0.config(text="left click turn")
    check()
    
def switch6(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label6 = Label(image=photo)
    label6.image = photo # keep a reference!
    label6.grid(row=70, column =1 )
    All[1][2] = player2
    label0.config(text="left click turn")
    check()
    
def switch7(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label7 = Label(image=photo)
    label7.image = photo # keep a reference!
    label7.grid(row=7, column =2 )
    All[2][0] = player2
    label0.config(text="left click turn")
    check()
    
def switch8(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label8 = Label(image=photo)
    label8.image = photo # keep a reference!
    label8.grid(row=30, column =2 )
    All[2][1] = player2
    label0.config(text="left click turn")
    check()
    
def switch9(event):
    X = Image.open("X.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label9 = Label(image=photo)
    label9.image = photo # keep a reference!
    label9.grid(row=70, column =2 )
    All[2][2] = player2
    label0.config(text="left click turn")
    check()

def switch11(event):
    X = Image.open("O.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label1 = Label(image=photo)
    label1.image = photo # keep a reference!
    label1.grid(row=7, column =0 )
    All[0][0] = player1
    label0.config(text="right click turn")
    check()
    
def switch22(event):
    X = Image.open("O.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label2 = Label(image=photo)
    label2.image = photo # keep a reference!
    label2.grid(row=30, column =0 )
    All[0][1] = player1
    label0.config(text="right click turn")
    check()
    
def switch33(event):
    X = Image.open("O.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label3 = Label(image=photo)
    label3.image = photo # keep a reference!
    label3.grid(row=70, column =0 )
    All[0][2] = player1
    label0.config(text="right click turn")
    check()
    
def switch44(event):
    X = Image.open("O.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label4 = Label(image=photo)
    label4.image = photo # keep a reference!
    label4.grid(row=7, column =1 )
    All[1][0] = player1
    label0.config(text="right click turn")
    check()
    
def switch55(event):
    X = Image.open("O.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label5 = Label(image=photo)
    label5.image = photo # keep a reference!
    label5.grid(row=30, column =1 )
    All[1][1] = player1
    label0.config(text="right click turn")
    check()
    
def switch66(event):
    X = Image.open("O.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label6 = Label(image=photo)
    label6.image = photo # keep a reference!
    label6.grid(row=70, column =1 )
    All[1][2] = player1
    label0.config(text="right click turn")
    check()
    
def switch77(event):
    X = Image.open("O.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label7 = Label(image=photo)
    label7.image = photo # keep a reference!
    label7.grid(row=7, column =2 )
    All[2][0] = player1
    label0.config(text="right click turn")
    check()
    
def switch88(event):
    X = Image.open("O.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label8 = Label(image=photo)
    label8.image = photo # keep a reference!
    label8.grid(row=30, column =2 )
    All[2][1] = player1
    label0.config(text="right click turn")
    check()
    
def switch99(event):
    X = Image.open("O.png")
    X = X.resize((100,100))
    photo = ImageTk.PhotoImage(X)

    label9 = Label(image=photo)
    label9.image = photo # keep a reference!
    label9.grid(row=70, column =2 )
    All[2][2] = player1
    label0.config(text="right click turn")
    check()

def openselabel1():
    if All[0][0] == 0:
         O = Image.open("O.png")
         O = O.resize((100,100))
         photo = ImageTk.PhotoImage(O)
        
         label1 = Label(image=photo)
         label1.image = photo # keep a reference!
         label1.grid(row=7, column =0 )
         All[0][0] = player1
         label0.config(text="right click turn")
         check()
    if All[0][0] == 1:
        X = Image.open("X.png")
        X = X.resize((100,100))
        photo = ImageTk.PhotoImage(X)
        
        label1 = Label(image=photo)
        label1.image = photo # keep a reference!
        label1.grid(row=7, column =0 )
        All[0][0] = player2
        label0.config(text="left click turn")
        check()
        
    else:
        image = Image.open("blank.png")
        image = image.resize((100,100))
        photo = ImageTk.PhotoImage(image)
    
        label1 = Label(image=photo)
        label1.image = photo # keep a reference
        label1.grid(row=7, column =0 )
        label1.bind("<Button-3>", switch1)
        label1.bind("<Button-1>", switch11)

def openselabel2():
    if All[0][1] == 0:
         O = Image.open("O.png")
         O = O.resize((100,100))
         photo = ImageTk.PhotoImage(O)
        
         label2 = Label(image=photo)
         label2.image = photo # keep a reference!
         label2.grid(row=30, column =0 )
         All[0][1] = player1
         label0.config(text="right click turn")
         check()
    if All[0][1] == 1:
        X = Image.open("X.png")
        X = X.resize((100,100))
        photo = ImageTk.PhotoImage(X)
        
        label2 = Label(image=photo)
        label2.image = photo # keep a reference!
        label2.grid(row=30, column =0 )
        All[0][1] = player2
        label0.config(text="left click turn")
        check()
        
    else:
        image = Image.open("blank.png")
        image = image.resize((100,100))
        photo = ImageTk.PhotoImage(image)
    
        label2 = Label(image=photo)
        label2.image = photo # keep a reference
        label2.grid(row=30, column =0 )
        label2.bind("<Button-3>", switch2)
        label2.bind("<Button-1>", switch22)
        
def openselabel3():
    if All[0][2] == 0:
         O = Image.open("O.png")
         O = O.resize((100,100))
         photo = ImageTk.PhotoImage(O)
        
         label3 = Label(image=photo)
         label3.image = photo # keep a reference!
         label3.grid(row=70, column =0 )
         All[0][2] = player1
         label0.config(text="right click turn")
         check()
    if All[0][2] == 1:
        X = Image.open("X.png")
        X = X.resize((100,100))
        photo = ImageTk.PhotoImage(X)
        
        label3 = Label(image=photo)
        label3.image = photo # keep a reference!
        label3.grid(row=70, column =0 )
        All[0][2] = player2
        label0.config(text="left click turn")
        check()
        
    else:
        image = Image.open("blank.png")
        image = image.resize((100,100))
        photo = ImageTk.PhotoImage(image)
    
        label3 = Label(image=photo)
        label3.image = photo # keep a reference
        label3.grid(row=70, column =0 )
        label3.bind("<Button-3>", switch3)
        label3.bind("<Button-1>", switch33)
   
def openselabel4():
    if All[1][0] == 0:
         O = Image.open("O.png")
         O = O.resize((100,100))
         photo = ImageTk.PhotoImage(O)
        
         label4 = Label(image=photo)
         label4.image = photo # keep a reference!
         label4.grid(row=7, column =1 )
         All[1][0] = player1
         label0.config(text="right click turn")
         check()
    if All[1][0] == 1:
        X = Image.open("X.png")
        X = X.resize((100,100))
        photo = ImageTk.PhotoImage(X)
        
        label4 = Label(image=photo)
        label4.image = photo # keep a reference!
        label4.grid(row=7, column =1 )
        All[1][0] = player2
        label0.config(text="left click turn")
        check()
        
    else:
        image = Image.open("blank.png")
        image = image.resize((100,100))
        photo = ImageTk.PhotoImage(image)
        label4 = Label(image=photo)
        label4.image = photo # keep a reference
        label4.grid(row=7, column =1 )
        label4.bind("<Button-3>", switch4)
        label4.bind("<Button-1>", switch44)
        
def openselabel5():
    if All[1][1] == 0:
         O = Image.open("O.png")
         O = O.resize((100,100))
         photo = ImageTk.PhotoImage(O)
        
         label5 = Label(image=photo)
         label5.image = photo # keep a reference!
         label5.grid(row=30, column =1 )
         All[1][1] = player1
         label0.config(text="right click turn")
         check()
    if All[1][1] == 1:
        X = Image.open("X.png")
        X = X.resize((100,100))
        photo = ImageTk.PhotoImage(X)
        
        label5 = Label(image=photo)
        label5.image = photo # keep a reference!
        label5.grid(row=30, column =1 )
        All[1][1] = player2
        label0.config(text="left click turn")
        check()
        
    else:
        image = Image.open("blank.png")
        image = image.resize((100,100))
        photo = ImageTk.PhotoImage(image)
        
        label5 = Label(image=photo)
        label5.image = photo # keep a reference
        label5.grid(row=30, column =1 )
        label5.bind("<Button-3>", switch5)
        label5.bind("<Button-1>", switch55)
        
def openselabel6():
    if All[1][2] == 0:
         O = Image.open("O.png")
         O = O.resize((100,100))
         photo = ImageTk.PhotoImage(O)
        
         label6 = Label(image=photo)
         label6.image = photo # keep a reference!
         label6.grid(row=70, column =1 )
         All[1][2] = player1
         label0.config(text="right click turn")
         check()
    if All[1][2] == 1:
        X = Image.open("X.png")
        X = X.resize((100,100))
        photo = ImageTk.PhotoImage(X)
        
        label6 = Label(image=photo)
        label6.image = photo # keep a reference!
        label6.grid(row=70, column =1 )
        All[1][2] = player2
        label0.config(text="left click turn")
        check()
        
    else:
        image = Image.open("blank.png")
        image = image.resize((100,100))
        photo = ImageTk.PhotoImage(image)
    
        label6 = Label(image=photo)
        label6.image = photo # keep a reference
        label6.grid(row=70, column =1 )
        label6.bind("<Button-3>", switch6)
        label6.bind("<Button-1>", switch66)
        
def openselabel7():
    if All[2][0] == 0:
         O = Image.open("O.png")
         O = O.resize((100,100))
         photo = ImageTk.PhotoImage(O)
        
         label7 = Label(image=photo)
         label7.image = photo # keep a reference!
         label7.grid(row=7, column =2 )
         All[2][0] = player1
         label0.config(text="right click turn")
         check()
    if All[2][0] == 1:
        X = Image.open("X.png")
        X = X.resize((100,100))
        photo = ImageTk.PhotoImage(X)
        
        label7 = Label(image=photo)
        label7.image = photo # keep a reference!
        label7.grid(row=7, column =2 )
        All[2][0] = player2
        label0.config(text="left click turn")
        check()
        
    else:
        image = Image.open("blank.png")
        image = image.resize((100,100))
        photo = ImageTk.PhotoImage(image)
        label7 = Label(image=photo)
        label7.image = photo # keep a reference
        label7.grid(row=7, column =2 )
        label7.bind("<Button-3>", switch7)
        label7.bind("<Button-1>", switch77)

def openselabel8():
    if All[2][1] == 0:
         O = Image.open("O.png")
         O = O.resize((100,100))
         photo = ImageTk.PhotoImage(O)
        
         label8 = Label(image=photo)
         label8.image = photo # keep a reference!
         label8.grid(row=30, column =2 )
         All[2][1] = player1
         label0.config(text="right click turn")
         check()
    if All[2][1] == 1:
        X = Image.open("X.png")
        X = X.resize((100,100))
        photo = ImageTk.PhotoImage(X)
        
        label8 = Label(image=photo)
        label8.image = photo # keep a reference!
        label8.grid(row=30, column =2 )
        All[2][1] = player2
        label8.config(text="left click turn")
        check()
        
    else:
        image = Image.open("blank.png")
        image = image.resize((100,100))
        photo = ImageTk.PhotoImage(image)
    
        label8 = Label(image=photo)
        label8.image = photo # keep a reference
        label8.grid(row=30, column =2 )
        label8.bind("<Button-3>", switch8)
        label8.bind("<Button-1>", switch88)
        
def openselabel9():
    if All[2][2] == 0:
        O = Image.open("O.png")
        O = O.resize((100,100))
        photo = ImageTk.PhotoImage(O)
        
        label9 = Label(image=photo)
        label9.image = photo # keep a reference!
        label9.grid(row=70, column =2 )
        All[2][2] = player1
        label0.config(text="right click turn")
        check()
    if All[2][2] == 1:
        X = Image.open("X.png")
        X = X.resize((100,100))
        photo = ImageTk.PhotoImage(X)
        
        label9 = Label(image=photo)
        label9.image = photo # keep a reference!
        label9.grid(row=70, column =2 )
        All[2][2] = player2
        label0.config(text="left click turn")
        check()
        
    else:
        image = Image.open("blank.png")
        image = image.resize((100,100))
        photo = ImageTk.PhotoImage(image)
        
        label9 = Label(image=photo)
        label9.image = photo # keep a reference
        label9.grid(row=70, column =2 )
        label9.bind("<Button-3>", switch9)
        label9.bind("<Button-1>", switch99)
   
          
def opense():
    openselabel1()
    openselabel2()
    openselabel3()
    openselabel4()
    openselabel5()
    openselabel6()
    openselabel7()
    openselabel8()
    openselabel9()

def openfileR():
    f = open("Readme.txt", "r")
    for line in f:
        name = line
        All[0][0] = int(name[0])
        All[0][1] = int(name[1])
        All[0][2] = int(name[2])
        All[1][0] = int(name[3])
        All[1][1] = int(name[4])
        All[1][2] = int(name[5])
        All[2][0] = int(name[6])
        All[2][1] = int(name[7])
        All[2][2] = int(name[8])
        opense()
    f.close()
    


def openfileW():
    f = open("Readme.txt", 'w')
    f.write(str(All[0][0]) + str(All[0][1]) + str(All[0][2]) + str(All[1][0]) + str(All[1][1]) + str(All[1][2]) + str(All[2][0]) + str(All[2][1]) + str(All[2][2]) )
    f.close()
   
def Directions():
    tkMessageBox.showinfo("Directions","Play tic tac toe and don't cheat by clicking the same picture twice or going when it is not your turn. We didn't have enough time to fix that. If you are actually wondering how to  play tic tac toe, then I pity you because you didn't have a childhood and go and look up the directions online. It's the 21st century, the internet is usually your friend.")
   
def reset():
    label0 = Label(root, text ="Left Click Go First", bg="pink", anchor=W)
    label0.grid(row=0, column=0, sticky=EW, columnspan=3)

    x = [10, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]
    All[0] = x
    All[1] = y
    All[2] = z
    opense()
      
def start():
    root = Tk() #gives us a blank canvas object to work with
    root.title = ("GUI Program")
   
    label0 = Label(root, text ="Left Click Go First", bg="pink", anchor=W)
    label0.grid(row=0, column=0, sticky=EW, columnspan=3)
    
    image = Image.open("blank.png")
    image = image.resize((100,100))
    photo = ImageTk.PhotoImage(image)
    
    label1 = Label(image=photo)
    label1.image = photo # keep a reference
    label1.grid(row=70, column =0 )
    label1.bind("<Button-3>", switch1)
    label1.bind("<Button-1>", switch11)
    
    label2 = Label(image=photo)
    label2.image = photo # keep a reference!
    label2.grid(row=30, column =0 )
    label2.bind("<Button-3>", switch2)
    label2.bind("<Button-1>", switch22)

    label3 = Label(image=photo)
    label3.image = photo # keep a reference!
    label3.grid(row=70, column =0 )
    label3.bind("<Button-3>", switch3)
    label3.bind("<Button-1>", switch33)

    label4 = Label(image=photo)
    label4.image = photo # keep a reference!
    label4.grid(row=7, column =1 )
    label4.bind("<Button-3>", switch4 )
    label4.bind("<Button-1>", switch44)
    
    label5 = Label(image=photo)
    label5.image = photo # keep a reference!
    label5.grid(row=30, column =1 )
    label5.bind("<Button-3>", switch5)
    label5.bind("<Button-1>", switch55)

    label6 = Label(image=photo)
    label6.image = photo # keep a reference!
    label6.grid(row=70, column =1 )
    label6.bind("<Button-3>", switch6 )
    label6.bind("<Button-1>", switch66)
    
    label7 = Label(image=photo)
    label7.image = photo # keep a reference!
    label7.grid(row=7, column =2 )
    label7.bind("<Button-3>", switch7)
    label7.bind("<Button-1>", switch77)
    
    label8 = Label(image=photo)
    label8.image = photo # keep a reference!
    label8.grid(row=30, column =2 )
    label8.bind("<Button-3>", switch8 )
    label8.bind("<Button-1>", switch88)
    
    label9 = Label(image=photo)
    label9.image = photo # keep a reference!
    label9.grid(row=70, column =2 )
    label9.bind("<Button-3>", switch9)
    label9.bind("<Button-1>", switch99)


root = Tk() #gives us a blank canvas object to work with
root.title = ("Tic Tac Toe")

label0 = Label(root, text ="Left Click Go First", bg="pink", anchor=W)
label0.grid(row=0, column=0, sticky=EW, columnspan=3)
    
    
    
image = Image.open("blank.png")
image = image.resize((100,100))
photo = ImageTk.PhotoImage(image)



label1 = Label(image=photo)
label1.image = photo # keep a reference!
label1.grid(row=7, column =0 )
label1.bind("<Button-3>", switch1)
label1.bind("<Button-1>", switch11)

label2 = Label(image=photo)
label2.image = photo # keep a reference!
label2.grid(row=30, column =0 )
label2.bind("<Button-3>", switch2)
label2.bind("<Button-1>", switch22)

label3 = Label(image=photo)
label3.image = photo # keep a reference!
label3.grid(row=70, column =0 )
label3.bind("<Button-3>", switch3)
label3.bind("<Button-1>", switch33)

label4 = Label(image=photo)
label4.image = photo # keep a reference!
label4.grid(row=7, column =1 )
label4.bind("<Button-3>", switch4 )
label4.bind("<Button-1>", switch44)

label5 = Label(image=photo)
label5.image = photo # keep a reference!
label5.grid(row=30, column =1 )
label5.bind("<Button-3>", switch5)
label5.bind("<Button-1>", switch55)

label6 = Label(image=photo)
label6.image = photo # keep a reference!
label6.grid(row=70, column =1 )
label6.bind("<Button-3>", switch6 )
label6.bind("<Button-1>", switch66)

label7 = Label(image=photo)
label7.image = photo # keep a reference!
label7.grid(row=7, column =2 )
label7.bind("<Button-3>", switch7)
label7.bind("<Button-1>", switch77)

label8 = Label(image=photo)
label8.image = photo # keep a reference!
label8.grid(row=30, column =2 )
label8.bind("<Button-3>", switch8 )
label8.bind("<Button-1>", switch88)

label9 = Label(image=photo)
label9.image = photo # keep a reference!
label9.grid(row=70, column =2 )
label9.bind("<Button-3>", switch9)
label9.bind("<Button-1>", switch99)



menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Game Reset", command=reset)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)
filemenu.add_separator()
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Directions", command=Directions)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)


root.config(menu=menubar)

start()

mainloop() #causes the windows to display on the screen until program closes


