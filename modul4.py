from os import path as p 
from os import listdir as ld #bu şekilde de içe aktarabiliyoruz .

from sys import*#Bu şekilde bir modül içindeki bütün fonksiyon ve nitelikleri içe aktarmış oluruz
                # (ismi _ ile başlayanlar hariç)
print(version)#yıldızlı içe aktarma yöntemiyle fonksiyon ve niteliklerin başına modül adını eklemeden kullanabiliriz.
#ama bu yöntem tavsiye edilmez.
#Yıldızlı içe aktarma işlemleri ancak modül seviyesinde, yani global isim alanında gerçekleştirilebilir.
#yani bir fonk tanımladığınızda onun lokal bölgesinde yıldızlı bir aktarma yapılamaz.
               

