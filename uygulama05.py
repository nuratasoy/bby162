import random



kelimeler =(["kale", "bilgisayar", "peçete", "fevkalade","aspiratör","ambale", "zirve","fırça", "ürtiker","lezyon","egzoz"])

toplamhak = 5
i=0


kelimesec=random.choice(kelimeler)
girilmişharfler =[]
karakterGosterimi="_"

for kelime in kelimesec:
    girilmişharfler.append(karakterGosterimi)
print(girilmişharfler)

while toplamhak>0:
    alinanharf = input("Lütfen bir harf giriniz=").lower()
    if alinanharf in kelimesec:
        for kontrol in kelimesec:
            if alinanharf==kelimesec[i]:
                girilmişharfler[i] = alinanharf
            i +=1
        print(girilmişharfler)
        i=0


    kontrolEt= alinanharf in kelimesec
    if kontrolEt == False:
        toplamhak-=1
    print("Kalan can sayınız=", toplamhak)
    i=0

    if toplamhak == 0:
     print("Oyunu kaybettiniz.Doğru kelime '{}' idi.".format(kelimesec))

     break

    if karakterGosterimi not in girilmişharfler:
        print("Tebrikler.Doğru kelimeyi buldunuz")
        break







