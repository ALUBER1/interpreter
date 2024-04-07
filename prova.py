import tkinter
import subprocess
from tkinter import scrolledtext
from tkinter import filedialog
def apri():
    file1=filedialog.askopenfilename()
    with open(file1,'r') as file:
        testo.delete('1.0',tkinter.END)
        testo.insert(tkinter.END,file.read())
def salva(event=None):
    file1=filedialog.askopenfilename()
    with open(file1,'w') as file:
        file.write(testo.get('1.0',tkinter.END))
subprocess.run('sposta.bat & exit')
app=tkinter.Tk()
app.title("windmill compiler")
app.iconbitmap('windmill.ico')
testo=scrolledtext.ScrolledText(app,wrap=tkinter.WORD)
testo.pack(fill=tkinter.BOTH,expand=True)
men=tkinter.Menu(app)
opzioni= tkinter.Menu(men, tearoff=0)
opzioni.add_command(label="apri",command=apri)
opzioni.add_command(label="salva ctr+s",command=salva)
opzioni.add_command(label='esci',command=app.quit)
men.add_cascade(label="opzioni",menu=opzioni)
app.bind('<Control-s>',salva)
app.config(menu=men)
app.mainloop()