kadinismi = input("Bir kadın adı giriniz...:")
erkekismi = input("Bir erkek adı giriniz...:")
mısra    = int(input("Mısra sayısı giriniz...Maksimum 10 mısra yazdırılabilir.."))


import random

sarki = [erkekismi + "Günler geceler çabuk geçer. "+ kadinismi +"Çabuk geçmez şaşkın bir çocuğun hüznü  ", "Vapurlar, arabalar, karlar çabuk geçer." + kadinismi ,"Ayrılık da özlem de her şey... ","Herşey çabuk geçer", erkekismi + "Birden gün ağarır." + kadinismi + " " "Gidilir herhalde gelinir. "]

for olusturulacak_sarki in sarki[:mısra]:
    print(random.choice(sarki))


if mısra > 10:
    print("Geçerli bir mısra sayısı girmediniz..")
    print("Yazdırılan mısra sayısı: 10")

else:
    print("Yazdırılan mısra sayısı:", mısra)
