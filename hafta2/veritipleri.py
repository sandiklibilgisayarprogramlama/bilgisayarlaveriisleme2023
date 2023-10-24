pasaj = """Lorem Ipsum is simply dummy text 
of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy 
text ever since the 1500s, when an unknown printer took a galley of 
type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the 
leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset 
sheets containing LoReM Ipsum passages, 
and more recently with desktop publishing software like
Aldus PageMaker including versions of LoreM Ipsum.
"""

"""
Yukarıda verilen pasajda kaç tane lorem ifadesi geçmektedir.
Sonucu ekrana yazan programı kodlayınız.

pasaj = pasaj.lower() # pasajı küçük harfe çevirdik
kelime_listesi = pasaj.split(" ")
sayac = 0

for kelime in kelime_listesi:
    if  "lorem" in kelime :
        sayac = sayac+1

print(sayac)
"""

# noktalama işaretlerini kaldırma amaçlı kullanılan kod
import string

for karakter in pasaj:
    if karakter in string.punctuation: # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        pasaj = pasaj.replace(karakter,"")

print(pasaj)