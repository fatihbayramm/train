birlestir = lambda ifade , birlestirici : birlestirici.join(ifade.split())
a = birlestir("İstanbul Büyükşehir Belediyesi" , "-")
print(a)

def birles(ifade , birlestirici):
    return birlestirici.join(ifade.split())

b = birles("İstanbul Büyükşehir Belediyesi" , "-")    
print(b)

import tkinter
import tkinter.ttk as ttk

pen = tkinter.Tk()

btn = ttk.Button(text='merhaba', command=lambda: print('merhaba'))
btn.pack(padx=20, pady=20)

pen.mainloop()