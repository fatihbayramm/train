import webbrowser as web
from os import name , listdir , getcwd#bu şekilde os modülündeki yalnızca kullanacagımız fonksiyon ve nitelikleri
                                      #içe aktardık.  

web.open("www.youtube.com")

print(listdir())#Bu fonksiyon, o anda içinde bulunduğumuz dizindeki dosyaları listeler.
print(len(listdir()))

