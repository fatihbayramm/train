kod_cozuculer = ["UTF-8" , "cp1254" , "latin-1" , "ASCII"]
harf = "İ"
for kc in kod_cozuculer:
    try:
        print("'{}' karakteri {} ile {} olarak ve {} sayısıyla temsil edilir .".format(harf , kc , harf.encode(kc) ,
                                                                                        ord(harf)))
    except UnicodeEncodeError:
        print("'{}' karakteri {} ile temsil edilemez !".format(harf , kc))     

                                                                                     