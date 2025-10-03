# %% deggiskenler variable
tam_sayi_degisken=10
ondalikli_sayi=3.6
print(tam_sayi_degisken)

#dört işlem özellikleri
a=4
b=8
topla=a+b+4
cikar=a-5
carpma=a*b
bolme=b/a
print("toplam:{} fark:{} carpma:{}  bolme{}".format(topla,cikar,carpma,bolme))

#stringler
string="furkan"
print(string)


"""
yorum
kodu seçip ctrl+1 e basarsanız yoruma alır hepsini
"""
#yorum

# %% liste veri tipi 

"""

-bilesik ver veri türüdür(birden fazla veri türünü içinde barındırabilir farklı) ve çok yönlüdür 

"""

liste=[1,2,5,6,8]
print(liste)
print(type(liste))
hafta=["ocak","şubat","mart","nisan","mayıs"]

#ilk eleman
print(hafta[0])

#boyut
print(len(hafta))

#son eleman
print(hafta[len(hafta)-1])

print(hafta[-1])#bu da son eleman demektir 

#liste 2-3-4 elemanı yaz 1,2,3 indeks
print(hafta[1:4])# ilk elemanı dahil tutar ikinciyi tutmaz o yüzden bir fazla yazdık

#ekleme-cıkarma
sayi_listesi=[1,2,3,4,5,6,7]
sayi_listesi.append(8)#sonuna ekler
print(sayi_listesi)

sayi_listesi.remove(4)#direkt elemanı ççıkardı bu indexx değil
print(sayi_listesi)

#listeyi ters cevir
sayi_listesi.reverse()
print(sayi_listesi)

#listeyi sırala
sayi_listesi=[1,15,6,74,78,0]
sayi_listesi.sort()#kücükten büyüğe sıralar
print(sayi_listesi)

#%% tuple
"""
Degistirilemez ve sıralı bir veri tipidir
(1,2,3)

"""
tuple_veritipi=(1,2,3,3,4,5,5,5,6)

#ilk eleman
print(tuple_veritipi[0])

#2.indeksten sonraki elemanları yazdır
print(tuple_veritipi[2:])
#count eleman
print(tuple_veritipi.count(5))

#%%  deque
"""
listeden farkı oluştururken önceden boyutu belirlenir
bunu daire olarak düşünebilirz örneğin 3 elemanlı dörndücü eklersen ilki çıkar ddeque dan

"""
from collections import deque
dq=deque(maxlen=3)

dq.append(1)
print(dq)

dq.append(2)
print(dq)


dq.append(3)
print(dq)


dq.append(4)
print(dq)

#%% sözlük
"""

-Bir çeşit karma tablo türüdür
-anahtar ve değer çiftlerinden oluşur
-{"anahtar":Değer}

"""
dictionary={"ankara":6,
            "izmir":35,
            "konya":42}

print(dictionary)

#ankara anahtarının değeri

print(dictionary["ankara"])


#anahtarlar
print(dictionary.keys())

#değerler
print(dictionary.values())
#%% if-else
sayi1=13.6
sayi2=14.5
print("sayi1",sayi1,"sayi2",sayi2)
if sayi1<sayi2:
    print("sayi1 kücüktür sayi2 den")
else:
    print("sayi2 küçüktür sayi1den")

liste=[1,23,4,5,6]
deger=32
if deger in liste:
    print("{}deger listenin içinde".format(deger))
else:
    print("{} degeri listenin içinde değildir".format(deger))

dictionary={"türkiye":"ankara","ingiltere":"londra","ispanya":"madrid"}
keys=dictionary.keys()
anahtar="türkiye"
if anahtar in keys:
    print("evet")
else:
    print("hayır")
    
#%% döngüler
"""
Tekrar eden işleri yapmak için kullanılır

"""
for i in range(1,5):
    print(i)


liste=[1,4,6,7,9,0,5,4]
toplam=0
for i in liste:
    toplam=toplam+i

print(toplam)

#while
i=0
while i<4:
    print(i)
    i=i+1
liste=[1,4,6,7,9,0,5,4]
sinir=len(liste)
index=0
toplam=0
while index<sinir:
    toplam=toplam+liste[index]
    index+=1
print(toplam)

#%% Fonksiyonlar
"""
-Karmaşık işlemleri bir araya toplamak ve bu işlemleri tek adımda yapmak için kullanılır
-Aynı işlemi birden fazla yerde yapmak gerektiği zaman kullanılır
-Daha düzenli kod
-Kod düzenleme kolaylığı
-İki tip var Built-in Functions(Gömülü fonksiyonlar).User-Defined Functions(Kullanıcı Tanımlı Fonksiyonlar)
"""
#Kullanıcı tarafından tanımlanan fonksiyonlar
def selam(isim):
    print("Merhaba",isim)
selam("furkan")

def topla(x,y):
    print(f"x + y= {x+y}")

topla(3, 5)

def ortalama_hesapla(liste):
    toplam=sum(liste)
    adet=len(liste)
    sonuc=toplam/adet
    print(f"Ortalama:{sonuc}")


ortalama_hesapla([1,2,3,4,5,6,7])

def buyuk_harfe_cevir(metin):
    metin=metin.upper()
    print(metin)

buyuk_harfe_cevir("fngFthkoO")



def selamla(mesaj,isim):
    print(f"{mesaj} {isim}.")

selamla("merhaba", "furkan")


def ort(x,y):
    return(x+y)/2 #return elde ettiğimiz sonucu tekrar kullanmak istedğimiz zaman tekrar döndürmesi için kullanırız.Örneğin başka bi değişkene aktarmak için

#fonkisyon sonucunu saklamak,kullanmak için return kullanırız
ort(5, 7)






