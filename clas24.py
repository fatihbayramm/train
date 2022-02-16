import clas23

s = clas23.Sinif()


#gizli üye old için erişemiyoruz.

__gizli = 'gizli'
__gizli_ = 'gizli'
__gizli_üye = 'gizli'
__gizli_üye_ = 'gizli'#bunlar birer gizli üyedir.
#Gizli üyeler yalnızca sınıf dışına kapalıdır. Bu üyelere sınıf içinden rahatlıkla erişebiliriz.

print(s.ornek_metodu())

print("-"*30)

print(s._Sinif__gizli)#bu şekilde ise gizli üyeye erişebiliriz.



