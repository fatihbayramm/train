import tkinter as tk 

pencere = tk.Tk()
pencere.geometry("1024x768")


etiket = tk.Label(text = "Merhaba Zalim Dünya ! ")
etiket.pack()

dugme = tk.Button(text = "Tamam")
dugme.pack()

etiket2 = tk.Label(text = "2.etiket")
etiket2.pack()

dugme2 = tk.Button(text = "Çık" , command = pencere.destroy)
dugme2.pack()
pencere.mainloop()