#use rowspan for making boxes be that big. 


from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox 
from PIL import Image, ImageTk



def switch():
    x = 0
    if x % 2 == 0:
        print'hey'
        x += 1
    else:
        print'no'
        x+=1
    
    
def turn():
    
    label1.config(text=switch())

def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("You typed: ", entrytxt)
    
def openfileR():
    clearlist2()
    f = open("Readme.txt", "r")
    for line in f:

        name = line[0:-1]
        listbox1.insert(END, name)
    f.close()

def openfileW():
    f = open("Readme.txt", 'w')
    names = listbox1.get(0,END)
    for i in names:    
        f.write(i + "\n") 
    
    f.close()
    

root = Tk() #gives us a blank canvas object to work with
root.title = ("GUI Program")




label1 = Label(root, text ="Player 1 Go First", bg="pink", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=2)

turn()




image = Image.open("blank.png")
image = image.resize((100,100))
photo = ImageTk.PhotoImage(image)
    
label1 = Label(image=photo)
label1.image = photo # keep a reference!
label1.grid(row=7, column =0 )
label1.bind("<Button-3>",switch )

label2 = Label(image=photo)
label2.image = photo # keep a reference!
label2.grid(row=30, column =0 )
label2.bind("<Button-3>",switch )

label3 = Label(image=photo)
label3.image = photo # keep a reference!
label3.grid(row=70, column =0 )
label3.bind("<Button-3>",switch )

label4 = Label(image=photo)
label4.image = photo # keep a reference!
label4.grid(row=7, column =1 )
label4.bind("<Button-3>",switch )

label5 = Label(image=photo)
label5.image = photo # keep a reference!
label5.grid(row=30, column =1 )
label5.bind("<Button-3>",switch )

label6 = Label(image=photo)
label6.image = photo # keep a reference!
label6.grid(row=70, column =1 )
label6.bind("<Button-3>",switch )

label7 = Label(image=photo)
label7.image = photo # keep a reference!
label7.grid(row=7, column =2 )
label7.bind("<Button-3>",switch)

label8 = Label(image=photo)
label8.image = photo # keep a reference!
label8.grid(row=30, column =2 )
label8.bind("<Button-3>",switch )

label9 = Label(image=photo)
label9.image = photo # keep a reference!
label9.grid(row=70, column =2 )
label9.bind("<Button-3>",switch )


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_command(label="Save", command=openfileW)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)


mainloop() #causes the windows to display on the screen until program closes

