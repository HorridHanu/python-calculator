
########################################################################################
########################################################################################
## # CODE LANGUAGE IS PYHTON!          ##      ##                                     ##
## # DATE: 1-JULY-2021                 ##      ##   ########   ##          ##     ##  ##
## # CODE BY HANU!                     ##########         ##   #########   ##     ##  ##
## # ONLY FOR EDUCATIONAL PURPOSE!     ##########    #######   ##     ##   ##     ##  ##
## # GUI CALCULATOR!                   ##      ##    ##   ##   ##     ##   ##     ##  ##
## # ITS ONLY DEMO!                    ##      ##    #######   ##     ##   ########   ##
########################################################################################
########################################################################################



from tkinter import *
import tkinter.messagebox as tmsg


# define function for Help
def Help():
    tmsg.showwarning("Help", "contact us on Go To ->Github.com/HorridHanu<-\n "
                            "For More Update And Versions....")


# define function for About
def About():
    tmsg.showwarning("About","Code BY Hanu\n"
                             "Faulty calulator version 2.0\n"
                             "\nCopy Right 2021 Hanu Corporation. "
                            "All Right Reserved!"
                            " For All OS {Windows}, {Linux}, {MacOS}"
                            " User Interface Are Protected By Trademark"
                            " And Other Pendings"
                            " Or Existing Intellecutal Property Right In "
                            " United State And Other Countries.")


# define functions for claculator
def click(event):
    global scvalue
    text = event.widget.cget("text")


    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())
            scvalue.set(value)
            screen.update()



    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()



root = Tk()
root.geometry("200x350")
root.resizable(0, 0)
root.title("Calculator")
root.wm_iconbitmap('1.ico.jpg')
root.config(bg="white")


# menubar
menu_main = Menu(root)
m1 = Menu(menu_main, tearoff=0)
m1.add_command(label="Veiw Help", command=Help)
m1.add_command(label="About", command=About)
m1.add_command(label="Exit", command=exit)
menu_main.add_cascade(label="Help", menu=m1)
root.config(menu=menu_main)


# Entry Screen
scvalue= StringVar()
scvalue.get()
screen=Entry(root, text=scvalue, font=("lucida 15 italic"))
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


# frame
f1 = Frame(root, bg="grey", relief=SUNKEN)
f1.pack()

# button
b1 = Button(f1, fg="red",text="c", font=("lucida 20 italic"))
b1.pack(side=LEFT, padx=0, pady=0)
b1.bind("<Button-1>", click)

# button
b1 = Button(f1, fg="red",text="/", font=("lucida 20 italic"))
b1.pack(side=LEFT, padx=0, pady=0)
b1.bind("<Button-1>", click)

# button
b1 = Button(f1, fg="red",text="*", font=("lucida 20 italic"))
b1.pack(side=LEFT, padx=0, pady=0)
b1.bind("<Button-1>", click)

# button
b1 = Button(f1, fg="red", text="=", font=("lucida 20 italic"))
b1.pack(side=LEFT, padx=0, pady=0)
b1.bind("<Button-1>", click)


# frame
f2 = Frame(root, bg="grey", relief=SUNKEN)
f2.pack()

# button
b2 = Button(f2, fg="red",text="7", font=("lucida 20 italic"))
b2.pack(side=LEFT, padx=0, pady=0)
b2.bind("<Button-1>", click)

# button
b2 = Button(f2, fg="red",text="8", font=("lucida 20 italic"))
b2.pack(side=LEFT, padx=0, pady=0)
b2.bind("<Button-1>", click)

# button
b2 = Button(f2, fg="red",text="9", font=("lucida 20 italic"))
b2.pack(side=LEFT, padx=0, pady=0)
b2.bind("<Button-1>", click)

# button
b2 = Button(f2, fg="red", text="-", font=("lucida 20 italic"))
b2.pack(side=LEFT, padx=0, pady=0)
b2.bind("<Button-1>", click)



# frame
f3 = Frame(root, bg="grey", relief=SUNKEN)
f3.pack()

# button
b3 = Button(f3, fg="red",text="4", font=("lucida 20 italic"))
b3.pack(side=LEFT, padx=0, pady=0)
b3.bind("<Button-1>", click)

# button
b3 = Button(f3, fg="red",text="5", font=("lucida 20 italic"))
b3.pack(side=LEFT, padx=0, pady=0)
b3.bind("<Button-1>", click)

# button
b3 = Button(f3, fg="red",text="6", font=("lucida 20 italic"))
b3.pack(side=LEFT, padx=0, pady=0)
b3.bind("<Button-1>", click)

# button
b3 = Button(f3, fg="red", text="+", font=("lucida 20 italic"))
b3.pack(side=LEFT, padx=0, pady=0)
b3.bind("<Button-1>", click)



# frame
f4 = Frame(root, bg="grey", relief=SUNKEN)
f4.pack()

# button
b4 = Button(f4, fg="red",text="1", font=("lucida 20 italic"))
b4.pack(side=LEFT, padx=0, pady=0)
b4.bind("<Button-1>", click)

# button
b4 = Button(f4, fg="red",text="2", font=("lucida 20 italic"))
b4.pack(side=LEFT, padx=0, pady=0)
b4.bind("<Button-1>", click)

# button
b4 = Button(f4, fg="red",text="3", font=("lucida 20 italic"))
b4.pack(side=LEFT, padx=0, pady=0)
b4.bind("<Button-1>", click)

# button
b4 = Button(f4, fg="red", text="0", font=("lucida 20 italic"))
b4.pack(side=LEFT, padx=0, pady=0)
b4.bind("<Button-1>", click)



# frame
f5 = Frame(root, bg="grey", relief=SUNKEN)
f5.pack()

# button
b5 = Button(f5, fg="red",text=".", font=("lucida 20 italic"))
b5.pack(side=LEFT, padx=0, pady=0)
b5.bind("<Button-1>", click)

# button
b5 = Button(f5, fg="red",text="(", font=("lucida 20 italic"))
b5.pack(side=LEFT, padx=0, pady=0)
b5.bind("<Button-1>", click)

# button
b5 = Button(f5, fg="red",text=")", font=("lucida 20 italic"))
b5.pack(side=LEFT, padx=0, pady=0)
b5.bind("<Button-1>", click)

# button
b5 = Label(f5, fg="Black", text="Hanu", font=("lucida 15 italic"))
b5.pack(side=LEFT, padx=0, pady=0)




root.mainloop()


########################################################################################
########################################################################################