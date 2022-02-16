import urllib.request#urllib paketinden reques modülünü içe aktardık.
urllib.request.urlopen("https://twitter.com/home?lang=tr")
#urllib.request önekiyle erişebiliriz
from urllib import request#bu şekilde daha kolay oluyor.
request.urlopen("https://twitter.com/home?lang=tr")

from urllib.request import urlopen#daha da kolay
urlopen("https://twitter.com/home?lang=tr")

from urllib.request import *
#Bu şekilde urllib paketi içindeki request modülünün
#bütün nitelik ve metotlarını doğrudan mevcut isim alanına aktarmış olduk.
