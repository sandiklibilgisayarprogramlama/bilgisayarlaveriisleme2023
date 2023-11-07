import re  # modüle dahil etme
"""
cumle = "Bilgisayarla veri işleme dersinde python kullanıyoruz."

# match metodu
# başlangıcı kontrol eder
# re.match ("arama_yapılacak_kelime", "arama_yapılacak_cümle)
sonuc = re.match("Bilgisayarla veri işleme", cumle)
# match sadece başlangıçta arama yapar
print(sonuc)
print(sonuc.span())  # sadece aralıgı getirir

# search metodu
# içinde arama yapar ama ilk bulduğunu getirir

cumle = "Bilgisayarla veri işleme dersinde python kullanıyoruz. Bilgisayarı çok seviyoruz."

sonuc = re.search("Bilgisayar", cumle)

print(sonuc)
print(sonuc.span())
"""

cumle = "Bilgisayarla veri işleme dersinde python kullanıyoruz. Bilgisayarı çok seviyoruz."
# findall metodu
# içinde arama yapar ve bulduklarını listeler
sonuc = re.findall("Bilgisayar", cumle)
print(sonuc)

# Örnek lorem veya Lorem ifadesi aşağıdaki cümlede kaç kere geçiyor

lorem = """Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
"""

cumle = lorem.lower()

sonuc = re.findall("lorem", cumle)
print(len(sonuc))

# Örnek: baş harfi ö ile başlayan ve son harfi n ile biten isimleri listeleyiniz

liste = ["özcan", "mehmet", "süleyman", "selim",
         "kemal", "özkan", "esra", "dündar", "esin",
         "esma", "özhan", "özlem", "ön",
         "ösdasdasdaAAsdasdadan", "öAgd7h0213on"]

# 1. yol
# for eleman in liste:
#    if eleman[0] == "ö" and eleman[-1] == "n":
#        print(eleman)
"""
# 2. yol
for eleman in liste:
    sonuc = re.match("ö[a-zA-Z0-9]*n$", eleman)
    if sonuc:
        print(eleman)

[] -> özel karakter tanımlama (a-z) a,b A-Z A,B 0-9 1,2,3
* -> 0 veya daha fazla
$ -> son karakter
"""

# Örnek: 0 ile başlayan ve 5 ile biten sayıları listeleyiniz
liste = ["087875", "3131232", "3123123", "07656567", "16565788",
         "06786876875", "05789036756", "04423975777"]

for eleman in liste:
    sonuc = re.match("0[0-9]*5$", eleman)
    if sonuc:
        print(eleman)
print("-cep telefonları-")
# cep telefonu içeren cümleleri listeleyiniz
# {} içerisine kaç tane olacağını yazabiliriz
for eleman in liste:
    sonuc = re.match("05[0-9]{9}", eleman)
    if sonuc:
        print(eleman)
