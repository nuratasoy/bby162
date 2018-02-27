__author__:"Zefure Nur Atasoy"
saniye=float(input("Saniye giriniz:"))

yil=saniye /(365*24*3600)
saniye=saniye%(365*24*3600)

ay=saniye/(30*24*3600)
saniye=saniye%(30*24*3600)

hafta=saniye/(7*24*3600)
saniye=saniye/(7*24*3600)

gun=saniye/(24*3600)
saniye=saniye%(24*3600)

saat=saniye/(3600)
saniye%=3600

dakika=saniye/60
saniye %=60

saniye=saniye
print(int(yil) , "Yıl" , " " , int(ay) ,"Ay" , " " , int(gun) ,"Gün" , " " , int(saat) , "Saat" , " " , int(dakika)  ,"Dakika", " " , int(saniye) , "Saniye")


