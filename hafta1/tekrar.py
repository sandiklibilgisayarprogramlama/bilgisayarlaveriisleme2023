"""
sayi=10 # integer 
aa = 10.1 # float
kelime = '' # string
durum = True # boolean

print(sayi)
print("merhaba","selam",sep='-',end='.')
print("naber")
# \n - new line : yeni satır
# sep - seperator : araya ne koyacağımızı belirler
# end - sonuna ne koyacağımızı belirler
# atama Operatörü
# = - atama operatörü

# == - eşitlik operatörü
# != - eşit değil operatörü
# > - büyüktür operatörü
# < - küçüktür operatörü
# >= - büyük eşittir operatörü
# <= - küçük eşittir operatörü


print(10==10) # True
print(10!=10) # False
print(10>10) # False
print(10<10) # False
print(10>=10) # True
print(10<=10) # True


print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print(10==10 and 10>10) # False
print(10==10 or 10>10) # True
print(not 10!=10) # True

if 10!=10:
    print("10 eşittir 10")
elif 10>10:
    print("10 büyüktür 10")
elif 10<10:
    print("10 küçüktür 10")
else:
    print("10 eşit değildir 10")

klavyeden bilgi almak için input() fonksiyonu kullanılır
input() fonksiyonu her zaman string değer döner

int -> int(input())
float -> float(input())
bool -> bool(input())





sayi = 10.3
girilen=float(input("sayi giiniz"))

if girilen>sayi:
    print("girilen sayı büyüktür")



print(range(10)==range(0,10)) # == range(0,10) 0 dan 10 a kadar olan sayıları verir
print(range(4,10)) # 4 den 10 a kadar olan sayıları verir
print(range(3,10,2)) # 3 den 10 a kadar olan sayıları 2 şer 2 şer verir

for i in range(3,15,3):
    print(i)

# 0 ile 40 arasındaki 8 e bölünebilen sayıları ekrana yazdırın

for i in range(0,41,8):
    print(i)

for i in range(41):
    if i%8==0:
        print(i)

for i in range(101):
  if i%2!=0 and i%5==0:
    print(i)
    



yazilacak_metin = "Dahaçokpythonöğrenmeliyim"

# len -> length : uzunluk

for i in range(len(yazilacak_metin)):
    print(i*" "+yazilacak_metin[i])



klavyeden girilen bir kelimenin karakter
sayısı kadar o kelimeyi alt alta yazan programo
kodlayınız


kelime = input("kelime giriniz : ")
for i in range(len(kelime)):
    print(kelime)

# while döngüsü kullanarak 100 den geriye dogru,
# 4 e bölünebilen sayıları ekrana yazdırınız

for k in range(100,0,-4):
    print(k)
"""

sayi=100

while sayi>0:
    if sayi%4==0:
        print(sayi)
    sayi=sayi-1


