from tkinter import *
from tkinter import messagebox,colorchooser,filedialog,ttk
from tkinter.ttk import Progressbar
import time
def click():
    messagebox.showinfo(title="messagebix",message="you are handsome")
    messagebox.showerror(title="error",message='warning')
    messagebox.askquestion(title="question")
    

window= Tk()

newtab=ttk.Notebook(window)

tab1=Frame(newtab)
tab2=Frame(newtab)

newtab.add(tab1,text="1")
newtab.add(tab2,text='2')

newtab.place(x=0,y=0)

def start():
   total=100
   x=0
   speed=1
   while x<total:
       time.sleep(0.05)
       bar['value']+=(speed/total)*100
       x+=speed
       window.update_idletasks() 

bar=Progressbar(window,orient=HORIZONTAL,length=2000)
bar.place(x=0,y=100)
Button(window,text="download",
       command=start).place(x=0,y=20)

photo=PhotoImage(file='qr.png')




label =Label(window,text="Hello world",
             fg="green",bg="black",
             font=("Arial", 130,"bold"),
             bd=10,
             relief=SUNKEN,
             padx=10, pady=10,
            
             compound='bottom')
label.pack()

def co():
    color=colorchooser.askcolor()
    colorhex=color[1]
    
    window.config(bg=colorhex)

color=Button(window,
             text='colors',
             bg='cyan',
             command=co,)
color.pack()
def delete():
    entry.delete(0,END) 

def backspace():
    entry.delete(len(entry.get())-1,END)
   

entry=Entry(window,
            font=("arial",20),  
            fg="green",
            )
entry.pack()
frame=Frame(window)
frame.pack()
del_button=Button(frame, command=delete,text="clear")
del_button.pack(side='left')


back_space=Button(frame,text="backspace",command=backspace)
back_space.pack(side='right')

def open1():
    file=filedialog.askopenfilename()
    fil1=open(file,'r')
    print(fil1.read())
    fil1.close()

openbutton=Button(window,
                   command=open1,
                  text="open")
openbutton.pack()



def save():
    filesave=filedialog.asksaveasfile(
        defaultextension='.txt',
        filetypes=[("text",".txt"),
                   
                   ("all",".*")]
    )
    files=str(text.get(1.0,END))
    filesave.write(files)
    filesave.close()
text=Text(window)
text.pack()
savebutton=Button(window,
                  command=save,
                  text='save')
savebutton.pack()

canvas=Canvas(window,height=500,width=500)
canvas.create_line(0,0,500,500)
canvas.create_line(0,500,500,0)
canvas.place(x=100,y=500)


def temobutton():
    print("temprerature is ")       
    print(scale.get())

scale=Scale(window,
            from_=100,
            to=0,
            length=1000,
            tickinterval=10,
            font=("arial",30,'bold'),
            bg='cyan',
            troughcolor="blue"            )
scale.pack(side="left")

temobutto1n=Button(window,
                  text="Temp",command=temobutton)
temobutto1n.pack(side="left")




check=Checkbutton(window,
                  text="Agree term & conditions")
check.pack(side="bottom")
button=Button(window,
              text="Submit",
              command=click,
              fg='red',
              font=('arial',10),
              activeforeground='red',
              
              compound='bottom')
button.pack(side="bottom")
window.title("CAL")
window.mainloop()