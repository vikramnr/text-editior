# imports
from tkinter import *
import tkinter.filedialog
root = Tk()
text = Text(root)
text.grid()

# saving file
def saveas():
    global text
    # get the positon to save file
    t = text.get('1.0',"end-1c")
    savelocation = tkinter.filedialog.asksaveasfilename()
    
    # writing the content to file location
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()


# save as button
button = Button(root,text='Save', command=saveas)
button.grid()

# setting fonts
def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

# font menu buttons
font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] =font.menu
helvetica = IntVar()
courier = IntVar()

font.menu.add_checkbutton(label='Courier', variable=courier, command=FontCourier)
font.menu.add_checkbutton(label='Helvetica', variable=helvetica, command=FontHelvetica)

root.mainloop()
