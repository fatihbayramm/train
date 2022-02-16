import tkinter as tk

class Pencere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW" , self.cıkıs)
        self.etiket = tk.Label(text = "Merhaba Zalim Dünya")
        self.etiket.pack()

        self.dugme = tk.Button(text = "Çık" , command = self.cıkıs)
        self.dugme.pack()

    def cıkıs(self):
        self.etiket["text"] = "Elveda Zalim Dünya ..."
        self.dugme["text"] = "Bekleyin..."
        self.dugme["state"] = "disabled"
        self.after(2000 , self.destroy)
       

pencere = Pencere()
pencere.geometry("1024x768") 
pencere.mainloop()        

