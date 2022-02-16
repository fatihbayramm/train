for i in range(3):
    parola = input("Parola belirleyin :")
    if not parola:
        pass
    elif len(parola) in range(3 , 8):
        print("Parolanız :" , parola)
        break
    elif i == 2:
        print(" Parolayı 3 kez yanlış girdiniz .\n" ,
        "Lütfen 30 dakika sonra tekrar deneyin .")
    else:
        print("Parola 8 karakterden uzun , 3 karakterden kısa olmamalı .")            