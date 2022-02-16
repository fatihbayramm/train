import random
liste = [random.randint(0,10000) for i in range(0,1000)]

import os 
print(dir(os))
print("-"*30)

print(os.name)#bu komut ile işletim sistemimizin adını öğrendik.

if os.name == "nt":
    print("Programı rahatlıkla kullanabilirsiniz !")
else:
    print("Bu program sadece windows işletim sisteminde çalıştırılabilir.")  

  