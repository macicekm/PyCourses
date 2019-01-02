
#https://likegeeks.com/python-gui-examples-tkinter-tutorial/

from tkinter import *

window = Tk()

window.title("Some guji")

window.geometry('350x200')

lbl = Label(window,text = "Heloo there")#, font = ("Arial Bold", 50))

lbl.grid(column=0,row=0)

txt = Entry(window, width = 10, state = 'normal') # disabled, readonly
txt.grid(column=1, row=0)
txt.focus()

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text = res)

btn = Button(window, text= "Clikc me", bg = "green", fg = "grey", command = clicked)
btn.grid(column=2,row=0)



window.mainloop()



###########################################################################################

#Add a combobox widget

from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

combo = Combobox(window)

combo['values'] = (1,2,3,4,5,"Text")

combo.current(1) # set the selected item

combo.grid(column=0, row=0)

lbl = Label(window,text = combo.get())#, font = ("Arial Bold", 50))

lbl.grid(column=1,row=0)

window.mainloop()

###########################################################################################

# Add a Checkbutton widget (Tkinter checkbox)

from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

chk_state = BooleanVar()

chk_state.set(True)  # set check state

chk = Checkbutton(window, text='Choose', var=chk_state)

chk.grid(column=0, row=0)

window.mainloop()

###########################################################################################

# Add radio buttons widgets

from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to LikeGeeks app")

selected = IntVar()

rad1 = Radiobutton(window, text='First', value=1, variable=selected)

rad2 = Radiobutton(window, text='Second', value=2, variable=selected)

rad3 = Radiobutton(window, text='Third', value=3, variable=selected)


def clicked():
    print(selected.get())


btn = Button(window, text="Click Me", command=clicked)

rad1.grid(column=0, row=0)

rad2.grid(column=1, row=0)

rad3.grid(column=2, row=0)

btn.grid(column=3, row=0)

window.mainloop()



# Create a MessageBox

from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')


#def clicked():
    #messagebox.showinfo('Message title', 'Message content')
    #messagebox.showwarning('Message title', 'Message content')
    #messagebox.showerror('Message title', 'Message content')


    # res = messagebox.askquestion('Message title', 'Message content')
    # res = messagebox.askyesno('Message title', 'Message content')
    # res = messagebox.askyesnocancel('Message title', 'Message content')
    # res = messagebox.askokcancel('Message title', 'Message content')
    # res = messagebox.askretrycancel('Message title', 'Message content')

def clicked():

    return messagebox.askyesnocancel('Message title', 'Message content')

btn = Button(window, text='Click here', command=clicked)

btn.grid(column=0, row=0)

lbl = Label(window,text = clicked())#, font = ("Arial Bold", 50))

lbl.grid(column=1,row=0)

window.mainloop()

###########################################################################################

# Add a SpinBox (numbers widget)

from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

spin = Spinbox(window, from_=0, to=100, width=5)

spin.grid(column=0, row=0)

window.mainloop()

###########################################################################################

# Progress Bar


from tkinter import *

from tkinter.ttk import Progressbar

from tkinter import ttk

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

style = ttk.Style()

style.theme_use('default')

style.configure("black.Horizontal.TProgressbar", background='black')

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

bar['value'] = 70

bar.grid(column=0, row=0)

window.mainloop()

###########################################################################################

# Add a Menu bar

from tkinter import *

from tkinter import Menu

window = Tk()

window.title("Welcome to LikeGeeks app")

menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='New')

new_item.add_separator()

new_item.add_command(label='Edit')

new_item2 = Menu(menu)

new_item2.add_command(label='New2')

new_item2.add_separator()

new_item2.add_command(label='Edit2')

menu.add_cascade(label='File', menu=new_item)
menu.add_cascade(label='Options', menu=new_item2)

window.config(menu=menu)

window.mainloop()

###########################################################################################

# Add Widgets

from tkinter import *

from tkinter import ttk

window = Tk()

window.title("Welcome to LikeGeeks app")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')

tab_control.add(tab2, text='Second')

lbl1 = Label(tab1, text='label1')

lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text='label2')

lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

window.mainloop()