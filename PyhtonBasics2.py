# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 17:36:26 2025

@author: Turkuaz
"""
#%% Not Hesaplama
vize=float(input("Vize notunuzu giriniz: "))
final=float(input("final notunuzu giriniz: "))
harf_notu=""
ortalama=(final + vize)/2

if 0<=ortalama<50:
    harf_notu="FF"
    print("Kaldı")
elif 50<=ortalama<60:
    harf_notu="DD"
elif 60<=ortalama<65:
    harf_notu="CC"
elif 65<=ortalama<80:
    harf_notu="BB"
else:
    harf_notu="AA"

print("Ortalama:{} Harf notunuz:{}".format(ortalama,harf_notu))
#%% Yapıcalacaklar listesi
liste=[]
islem=0
while  islem !=4:
    print("1.Görev Ekle  2.Görevleri Listele  3.Görev Sil 4.Çıkış")
    islem=int(input("Yapmak istediğiniz işlemin numarasını giriniz: "))
    if islem==1:
        eleman=input("Girmek istediğiniz görevi yazınız:")
        liste.append(eleman)
        print("Başarıyla Eklendi")
    elif islem==2:
        if len(liste)==0:
            print("Herhangi bi görev eklemediniz lütfen önce görev ekleyiniz")
        else:
            print("Görevleriniz: ",liste)
    elif islem==3:
        if len(liste)==0:
            print("Herhangi bi görev eklemediniz lütfen önce görev ekleyiniz")
        else:
            print(liste)
            eleman=int(input("Silmek istediğiniz elemanın numarasını giriniz:"))
            del liste[eleman-1]
            print("Başaryıla Silindi")
            
print("Çıkış yapıldı.....")
#%% Dictionary örnek
urunler={"Elma":70,"Ekmek":11,"Süt":30,"İçecek":60}
sepet=[]
islem=0
while islem!=5:
 #islem=int(input("Yapmak istediğiniz işlemin numarasını giriniz: ")) eğer bu şekilde int olarak alırsak kullanıcı int girmediği zaman program çökebilir
 #Bu yüzden string olarak alıyoruz isdigit ise bi stringin sayılardan oluşup olumadıgını kontrol eden fonksiyondur
 print("1.Elma:70  2.Ekmek:11 3.Süt:30 4.İçecek:60 5.Çıkış")
 islem=input("Yapmak istediğiniz işlemin numarasını giriniz:")
 if not islem.isdigit():
     print("Hatalı giriş lütfen sayı giriniz...")
     continue
 islem=int(islem)
 if islem<1 or islem>5:
     print("Lütfen 1-4 arasında bir sayi giriniz")
     continue
 if islem==1:
     urun_adi="Elma"
     
 elif islem == 2:
        urun_adi = "Ekmek"
 elif islem == 3:
        urun_adi = "Süt"
 elif islem == 4:
        urun_adi = "İçecek"
 elif islem == 5:
        print("Çıkış yapılıyor...")
        break  # Döngüyü kır

    # Sepete ekleme ve toplam hesaplama
 if islem != 5:
    sepet.append(urun_adi)
    toplam = sum([urunler[u] for u in sepet])#Anahtar ı girerek değeri alıyoruz eğer u sepetin içindeyse örneğin urunler[elma]=70 i verir bize 
    print(f"{urun_adi} sepete eklendi.")
    print(f"Sepetteki ürünler: {sepet}")
    print(f"Toplam tutar: {toplam} TL")
#%% fonksiyon faktoriyel
def faktoriyel(n):
    sayi=1
    for i in range(1,n+1):
        sayi=sayi*i
    print(sayi)

faktoriyel(5)
#%% tek mi çift fonksiyon
def tekciftfonk(n):
    if n%2==0:
        print("Girilen sayi çift")
    else:
        print("Girilen sayi tek")
        
tekciftfonk(5)

#%% Asal sayi fonk
def asal(n):
    for i in range(2,n):
        if n%i==0:
         print("Asal değildir")
         break#Diyelim ki sayımız asal değildi ama break olmasaydı döngü devam edecekti asal yazacktı 
    else:
         print("Asaldır")
asal(7)
#%% Sesli harf sayma
def sesli_harf_sayi(metin):
    sesli="aeoöuüiı"
    sayac=0
    for harf in metin.lower():
       if harf in sesli:
           sayac+=1
           
    print(sayac,"Adet sesli harf vardır")
         
sesli_harf_sayi("furkan")    
sesli_harf_sayi("aeoöuüiı")

#%% Polindrom mu değil mi 
def Polindrom(metin):
   kucuk=metin.lower()
   liste=list(kucuk)
   liste.reverse()
  
   if liste==list(kucuk):
       print("Polindromdur")
   else:
       print(metin,"Tersi: ",''.join(liste))
Polindrom("Radar")
Polindrom("furkan")
#%% Basamaklara ayırma 
def basamak(n):
    if n<0:
        n=n*(-1)
        
    basamaklar=[]
    while n>0:
        basamak=n%10
        basamaklar.append(basamak)
        n=n//10 # // operatörü tam bölme yapıyor yani 45 bölü 10 yaptı 459 ü 10 böldü 45 i bıraktı 9 u sildi
    basamaklar.reverse()
    print(basamaklar)
    
basamak(459)       
basamak(-123)

#%% Armstrong sayı bulma 

# 153 → 1³ + 5³ + 3³ = 153 bu bir armstrong sayıdır 
def armstrong(n):
    i=0
    toplam=0
    asılsayi=n # ilk while dögünüsnde n sıfırlandıgı için burada girilen sayıyı tuttuk if de kullanmak için
    if n<0:
        print("Lütfen negatif sayı girmeyiniz")
        return # negatif sayı armstrong olamayacagı için burada kalan kısımların çalışmasını engelledik 
    basamaklar=[]
    while n>0:# Bu döngüde sayıyı basamaklarına ayırdık 
        basamak= n%10
        basamaklar.append(basamak)
        n=n//10
        
    basamak_sayisi=len(basamaklar)
    while i<len(basamaklar):# burada i basamaklar listesinin uzunlugundan küçükse işlem yapmayı sağladık
    
       sayi=basamaklar[i]
       toplam=toplam+sayi**basamak_sayisi # armstron sayi kaç basamaklıysa sayı o kuvvet ile hesaplanır o yüzden basamak sayısını kullanarak kuvvet aldık
       i=i+1
       
 
    if toplam==asılsayi:
        print("Girilen sayı armstrong sayıdır")
    else:
        print("Girilen sayi armstrong değildir")
armstrong(153)        
armstrong(111)    
armstrong(9474)
armstrong(-123)
armstrong(54748)

    
        