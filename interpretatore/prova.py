import tkinter
import subprocess
from tkinter import scrolledtext
from tkinter import filedialog
from gestisci import ottieni_dati
n=0
nuovo=False
path=''
def shift(m):
    for i in range(m,len(buttons)):
        if(i!=m):i+=1
        print(m,len(buttons),i)
        if i==0:
            buttons[i].pack(anchor='w', before=testo)
            buttons[i+1].place(x=buttons[i].winfo_width())
        else:
            app.update_idletasks()
            buttons[i].place(x=buttons[i-1].winfo_width()+buttons[i-1].winfo_x())
            buttons[i+1].place(x=buttons[i].winfo_width()+buttons[i].winfo_x())
        
        
def close_file(g):
    if g.cget("text")==path:testo.delete('1.0',tkinter.END)
    g.destroy()
    m=buttons.index(g)
    buttons.remove(g)
    buttons[m].destroy()
    buttons.pop(m)
    global n
    n-=1
    if len(buttons)==0:
        global nuovo
        nuovo=False
    else:
        shift(m)
def apri_file(path):
    with open(path,'r') as file:
        testo.delete('1.0',tkinter.END)
        testo.insert(tkinter.END,file.read())
def apri(event=None):
    xa=0
    global nuovo
    global path
    path=filedialog.askopenfilename()
    with open(path,'r') as file:
        testo.delete('1.0',tkinter.END)
        testo.insert(tkinter.END,file.read())
    global buttons
    button=tkinter.Button(app,text=path,fg='blue',command=lambda p=path: apri_file(p))
    global n
    for i in range(0,len(buttons)):
        xa+=buttons[i].winfo_width()
    if not nuovo:
        button.pack(anchor='w',before=testo)
    else:
        app.update_idletasks()
        button.place(x=xa)
    buttons.append(button)
    n+=1
    button2=tkinter.Button(app,text="X",fg="red",command=lambda g=button: close_file(g))
    app.update_idletasks()
    xa+=button.winfo_width()
    button2.place(x=xa)
    buttons.append(button2)
    n+=1
    nuovo=True
def salva(event=None):
    global nuovo
    global path
    if(not nuovo):
        path=filedialog.asksaveasfile(defaultextension='.wmll',filetypes=[('file di testo','.wmll')])
    with open(path,'w') as file:
        file.write(testo.get('1.0',tkinter.END))
def salva_nome():
    global path
    path=filedialog.asksaveasfile(defaultextension='.wmll',filetypes=[('file di testo','.wmll')])
    with open(path,'w') as file:
        file.write(testo.get('1.0',tkinter.END))
def chiudi():
    global nuovo
    nuovo=False
    testo.delete('1.0',tkinter.END)
subprocess.run('sposta.bat & exit')
app=tkinter.Tk()
app.title("windmill interpreter")
app.iconbitmap('windmill.ico')
men=tkinter.Menu(app)
opzioni= tkinter.Menu(men, tearoff=0)
opzioni.add_command(label="apri",command=apri)
opzioni.add_command(label="salva ctr+s",command=salva)
opzioni.add_command(label="salva con nome ctr+n",command=salva_nome)
opzioni.add_command(label='esci',command=app.quit)
men.add_cascade(label="opzioni",menu=opzioni)
app.bind('<Control-n>',salva_nome)
app.bind('<Control-s>',salva)
buttons=[]
testo=scrolledtext.ScrolledText(app,wrap=tkinter.WORD)
testo.pack(fill=tkinter.BOTH,expand=True)
app.config(menu=men)
app.mainloop()
