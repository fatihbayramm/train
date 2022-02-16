import tkinter as tk

pencere = tk.Tk()

def cıkıs():
    etiket["text"] = "Elveda Zalim Dünya ..."
    dugme["text"] = "Bekleyin..."
    dugme["state"] = "disabled"
    pencere.after(2000 , pencere.destroy)

etiket = tk.Label(text = "Merhaba Zalim Dünya !")
etiket.pack()

dugme = tk.Button(text = "Çık" , command = cıkıs)
dugme.pack()

pencere.protocol("WM_DELETE_WINDOW" , cıkıs)

pencere.mainloop()