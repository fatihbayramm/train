import os

yukleyici = os.__loader__#Bu nitelik, ilgili modülü içe aktaran mekanizma hakkında bize çeşitli 
                        #bilgiler veren birtakım araçlar sunar

print(dir(yukleyici))

import webbrowser
yukleyici2 = webbrowser.__loader__#Mesela, içe aktardığınız bir modülün kaynak kodlarını görüntülemek için bu modülden yararlanabilirsiniz
kaynak = yukleyici2.get_data(webbrowser.__file__)
print(kaynak)