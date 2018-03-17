import random

rastgelesayi = random.randint(1,100)
print("_________Tahmin Oyunu_________")
print("Sayıyı 1 ile 100 arasında giriniz!")

while True:
    print("===========================")
    tahmin = int(input("Tahmin ettiğiniz sayı?="))

    if tahmin == rastgelesayi:
        print("****************")
        for i in range(5):
            print("Doğru tahmin.Tebrikler")
        print("****************")
        break



    elif tahmin < rastgelesayi:
        print("===========================")
        print("Daha büyük bir sayı giriniz!")

    elif tahmin > rastgelesayi:
        print("===========================")
        print("Daha küçük bir sayı giriniz!")

    if tahmin >= 101 :
        print("Belirtilen aralıkta bir sayı girmediniz!!!")
    if tahmin <=0:
        print("Belirtilen aralıkta bir sayı girmediniz!!!")

