
import tkinter
import subprocess
from tkinter import scrolledtext
from tkinter import filedialog
from gestisci import ottieni_dati
n=0
nuovo=False
path=''
def nuovo_(event=None):
    testo.delete('1.0',tkinter.END)
    global path
    path=''
    global nuovo
    nuovo=False
def shift(m):
    for i in range(m,len(buttons)):
        if i==0:
            buttons[i].pack(anchor='w', before=testo)
        else:
            app.update_idletasks()
            buttons[i].place(x=buttons[i-1].winfo_width()+buttons[i-1].winfo_x())
def close_file(g):
    if g.cget("text") == path:
        testo.delete('1.0', tkinter.END)
        with open("messaggi\path.txt",'w')as file_path:
            file_path.write('')
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
def apri_file(path1):
    with open(path1,'r') as file:
        testo.delete('1.0',tkinter.END)
        testo.insert(tkinter.END,file.read())
    with open("messaggi\path.txt",'w')as file_path:
        file_path.write(path1)
    global nuovo,path
    path=path1
    nuovo=True
def apri(event=None,path1=''):
    xa=0
    global nuovo,path,n,buttons
    if path1=='':path=filedialog.askopenfilename()
    else : path=path1
    with open("messaggi\path.txt",'w')as file_path:
        file_path.write(path)
    with open(path,'r') as file:
        testo.delete('1.0',tkinter.END)
        testo.insert(tkinter.END,file.read())
    button=tkinter.Button(app,text=path,fg='blue',command=lambda p=path: apri_file(p))
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
    global nuovo,path
    if(not nuovo):
        path=filedialog.asksaveasfile(defaultextension='.wmll',filetypes=[('file di testo','.wmll')])
    else:   
        with open(path,'w') as file:
            file.write(testo.get('1.0',tkinter.END))
    with open("messaggi\path.txt",'w')as file_path:
        file_path.write(path.name)
        apri(path1=path.name)
def salva_nome():
    global path
    path=filedialog.asksaveasfile(defaultextension='.wmll',filetypes=[('file di testo','.wmll')])
    with open(path,'w') as file:
        file.write(testo.get('1.0',tkinter.END))
    with open("messaggi\path.txt",'w')as file_path:
        file_path.write(path)
subprocess.run('sposta.bat & exit')
with open("messaggi\path.txt",'w')as file_path:
    file_path.write('')
app=tkinter.Tk()
app.title("windmill interpreter")
app.iconbitmap('windmill.ico')
men=tkinter.Menu(app)
opzioni= tkinter.Menu(men, tearoff=0)
opzioni.add_command(label="apri",command=apri)
opzioni.add_command(label="nuovo ctr+n",command=nuovo_)
opzioni.add_command(label="salva ctr+s",command=salva)
opzioni.add_command(label="salva con nome ctr+n",command=salva_nome)
opzioni.add_command(label='esci',command=app.quit)
men.add_cascade(label="opzioni",menu=opzioni)
app.bind('<Control-n>',nuovo_)
app.bind('<Control-s>',salva)
buttons=[]
testo=scrolledtext.ScrolledText(app,wrap=tkinter.WORD)
testo.pack(fill=tkinter.BOTH,expand=True)
app.config(menu=men)
app.mainloop()
