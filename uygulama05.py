import random

gizliKelime = random.choice(["kitap", "yönetim", "belge", "plaka", "yazılım", "pil", "muz", "mango", "kahve", "gazete","çilek","defter"])

harfhavuzu = []

kalanhak = 7

harfsayısınıgosterencizgi = "_"


gosterimyazisi = list(harfsayısınıgosterencizgi * len(gizliKelime))

dongu = 1


while dongu:

    print(" ".join(gosterimyazisi),"\n")

    alinanharf = input("Bir harf giriniz: ").lower()

    try:
        int(alinanharf)
        print("Doğru bir şeyler girdiğinden emin ol.\n")
    except:

        if len(alinanharf) > 1:
            print("Harf giriniz!\n")
        else:

            if alinanharf in harfhavuzu:
                print("Bu harfi zaten girdiniz.\n")
            else:

                bulduk = None

                for i in range(len(gizliKelime)):

                    if alinanharf == gizliKelime[i]:

                        bulduk = True

                        gosterimyazisi[i] = alinanharf

                        harfhavuzu.append(alinanharf)

                        if harfsayısınıgosterencizgi not in gosterimyazisi:

                            print(" ".join(gosterimyazisi)) 
                            print("\nTebrikler! Doğru kelimeyi buldunuz!")

                            dongu = 0

                else:

                    if bulduk != True:
                        kalanhak -= 1

                        print("Yanlış harf. Kalan hakkınız: %s\n" %kalanhak)

                        harfhavuzu.append(alinanharf) #

                if kalanhak == 0:
                    print("Kaybettiniz! Doğru kelime şuydu=  %s  \n " %gizliKelime)

                    break
