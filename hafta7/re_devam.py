"""
[a-zA-Z0-9] -> büyük küçük tüm harfler ve rakamlar
+ -> 1 veya daha fazla
* -> 0 veya daha fazla
{3} -> 3 tane
"""

# Örnek: tcno içeren cümleleri listeleyiniz

import re
cumle = "ahmetin tcno'su 12345678901 ve ayşenin tcno'su 02345678901'dur."

sonuc = re.findall("[1-9][0-9]{10}", cumle)
if len(sonuc) > 0:
    print(sonuc)
else:
    print("tcno bulunamadı")


# . -> herhangi bir karakter a-z A-Z 0-9

# Örnek: ikinci harfi o ve dördüncü harfi e olan kelimeleri listeleyiniz

cumle = "Contrary to popular belief, Lorem Ipsum is not simply random text."

sonuc = re.findall(".o.e[a-zA-Z]*", cumle)
print(sonuc)

# * -> kendinden önceki gelen ifadeyi 0 veya daha fazla

# Örnek : ilk dışında a harfi içeren kelimeleri listeleyiniz

liste = ["salim", "Ca", "Naber", "lakin", "Yakın", "belief", "Lorem"]
for i in liste:
    if re.match("[b-zB-Z]{1}a+.*", i):
        print(i)


# + -> kendinden önceki gelen ifadeyi 1 veya daha fazla

# Örnek: bir şifre için içinde noktalama işareti (.!),
# rakam ve büyük harf bulunması gerektiğini kontrol ediniz

liste = ["A1Adasd1", "2343as!", "dasAda1", "asdA!3dad", "dasdasd.!"]

for i in liste:
    if re.match("[A-Z0-9a-z]+[!.]+[A-Za-z0-9]+", i):
        print(i)
