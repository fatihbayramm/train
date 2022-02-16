sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesli =""
sessiz = ""
kelime ="istanbul"
for i in kelime:
    if i in sesli_harfler:
        sesli += i
    else:
        sessiz +=i
print("Sesli harfler:  " , sesli)
print("Sessiz harfler: " , sessiz)            