import tkinter
def ottieni_parola(n=0,testo=0):
    a=testo.get('1.0',tkinter.END)
    b=a.split()
    print( b[n])