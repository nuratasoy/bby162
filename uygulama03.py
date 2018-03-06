__author__="Zefure Nur Atasoy"

urunler={"Aydınlatıcı stik":38.99, "Bb göz kremi":19.99,"Bb pudra":26,"Fondöten":53, "Kontür paleti":27.50}



print(urunler.keys())


urunismi=input("Fiyatını öğrenmek istediğiniz ürünün adını giriniz:")



if urunismi in urunler.keys():
    print( urunismi, "fiyatı:\n ", urunler[urunismi],"tl." )

else:
    print("Ürün adını doğru girdiğinizden emin olunuz!")

