import tkinter
import subprocess
from tkinter import scrolledtext
from tkinter import filedialog
from gestisci import ottieni_dati
nuovo=False
path=''
def apri():
    global nuovo
    global path
    path=filedialog.askopenfilename()
    with open(path,'r') as file:
        nuovo=True
        testo.delete('1.0',tkinter.END)
        testo.insert(tkinter.END,file.read())
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
subprocess.run('sposta.bat & exit')
app=tkinter.Tk()
app.title("windmill interpreter")
app.iconbitmap('windmill.ico')
testo=scrolledtext.ScrolledText(app,wrap=tkinter.WORD)
testo.pack(fill=tkinter.BOTH,expand=True)
men=tkinter.Menu(app)
opzioni= tkinter.Menu(men, tearoff=0)
opzioni.add_command(label="apri",command=apri)
opzioni.add_command(label="salva ctr+s",command=salva)
opzioni.add_command(label="salva con nome",command=salva_nome)
opzioni.add_command(label='esci',command=app.quit)
men.add_cascade(label="opzioni",menu=opzioni)
app.bind('<Control-s>',salva)
app.config(menu=men)
app.mainloop()