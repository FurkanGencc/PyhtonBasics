# -*- coding: utf-8 -*-
"""
Python Temel seviye Calışmalarım
Basic Python exercises and mini projects

@author: Turkuaz

"""
# Created: 2025-10-03

#%% tek mi cift mi
sayi=0
sayi=int(input("bir sayi giriniz: "))  #input stringe döndürüyor o yüzden int çevirerek kullanılır int(input("bir sayi giriniz: "))
if sayi%2==0:
    print("Girdiğiniz sayi çift")
elif sayi%2!=0:
    print("Girdiğiniz sayi tek")
    
#%% 1 100 topla
topla=0
for i in range (1,101):
    topla=topla+i
print(topla)
#%% kelimeyi tersten yazdır
kelime=input("Kelime giriniz: ")
ters=""
for harf in kelime:
    ters=harf+ters
print(ters)
#%% hesap makinesi
sayi1=int(input("Birinci sayiyi giriniz: "))
sayi2=int(input("İkinci sayiyi giriniz: "))
islem=""
islem=input("+,-,x,/ Yapmak istediğiniz işlemi seçiniz")
sonuc=0
if islem=="+":
    sonuc=sayi1+sayi2
    
elif islem=="-":
    sonuc=sayi1-sayi2

elif islem=="x":
    sonuc=sayi1*sayi2
 
elif islem=="/":
    sonuc=sayi1/sayi2
  
print(sonuc)
    
#%%asal mı değil mi
sayi=int(input("Bir tane sayi giriniz"))  
for i in range(2,sayi):
    if sayi%i==0:
        print("asal değil")
        break
else:
    print("asal")
#%% faktoriyel
sayi=int(input("sayı gir"))
faktoriyel=1
for i in range(1,sayi+1):
   faktoriyel*=i
print(faktoriyel)
#%% 1-20 arası sayı tahmin oyunu
import random
sayi=random.randint(1, 21)#randit random int üret random kütüphanesinin fonksiyonu
print("1-20 arasında bir sayı tuttum tahmin et")
sayial=int(input("Bir sayi tahmin ediniz: "))

while sayi!=sayial:
    print("Yanlış tahmin! Tekrar dene.")
    
    sayial=int(input("Bir sayi tahmin ediniz: "))
print("tebrikler")
#%% sifre alma
kullanici_adi="furkangenc"
sifre=718293

kullanici_al=input("Kullanıcı adınız: ")
sifre_al=int(input("Sifre Giriniz: "))    
while kullanici_al !="furkangenc"or sifre_al !=718293:
    print("Kullanıcı adınız veya şifreniz yanlış tekrar deneyiniz....")
    kullanici_al=input("Kullanıcı adınız: ")
    sifre_al=int(input("Sifre Giriniz: "))    
    
print("Giriş yapıldı")
#%% 1-100 tahmin
import random
sayi=random.randint(1, 101)
print(sayi)
print("1-100 arası sayı tuttum")
sayi1=int(input("Bir sayı tahmin et: ")) 
while sayi1 !=sayi:
    if sayi1>sayi:
        print("DAHA KÜÇÜK TAHMİN ETTİM")
        sayi1=int(input("Bir sayı tahmin et: ")) 
    elif sayi1<sayi:
        print("DAHA BÜYÜK TAHMİN ETTİM")
        sayi1=int(input("Bir sayı tahmin et: ")) 
print("Tebrikler")
        
"""
import random

sayi = random.randint(1, 100)  # 1-100 arası sayı
print("1-100 arası bir sayı tuttum. Tahmin etmeye çalış!")

deneme = 0  # tahmin sayacı

sayi1 = int(input("Bir sayı tahmin et: "))

while sayi1 != sayi:
    deneme += 1
    if sayi1 > sayi:
        print("DAHA KÜÇÜK TUTTUM")
    else:
        print("DAHA BÜYÜK TUTTUM")
    sayi1 = int(input("Tekrar tahmin et: "))

deneme += 1  # son doğru tahmin
print(f"Tebrikler! {deneme} denemede bildiniz ")
daha temiz kod hali input girişi daha az

"""
#%% Basit Atm uygulaması        

Yeni_bakiye=10000
cikis=""
islem=0
miktar=0
while islem!=4:
    print("1.PARA ÇEK 2.PARA YATIR 3.BAKİYE SORGU 4.CIKIŞ")
    islem=int(input("Yapmak istediğiniz işlemin numarasını giriniz:"))
    if islem==1:
        miktar=int(input("Cekilecek miktar:"))
        if miktar>Yeni_bakiye:
            print("Yetersiz bakiye  lütfen tekrar deneyiniz. Bakiyeniz:",Yeni_bakiye)
            miktar=int(input("Cekilecek miktar:"))
        else:
            Yeni_bakiye=Yeni_bakiye-miktar
            print("İşlem başarılı yeni bakiyeniz:" , Yeni_bakiye)
    if islem==2:
        miktar=int(input("Yatırılacak miktar:"))
        Yeni_bakiye=Yeni_bakiye+miktar
        print("İşlem başarılı yeni bakiyeniz:" , Yeni_bakiye)
  
    if islem==3:
        print("Bakiyeniz:",Yeni_bakiye)
        
        
print("Çıkış Yapıldı")



"""
**** parola eklemek istenirse  bu adım da eklenebilir ****
while deneme < max_deneme:
    girilen_parola = input("Parolanızı giriniz: ")
    if girilen_parola == parola:
        print("Parola doğru. ATM'ye hoşgeldiniz ")
        break
    else:
        deneme += 1
        print(f"Parola yanlış! Kalan hakkınız: {max_deneme - deneme}")
else:
    print("Hakkınız doldu. ATM kullanımı engellendi ")
    exit() 


"""
