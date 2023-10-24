import string

with open("SMSSpamCollection","r") as dosya:
    mesaj_listesi = dosya.readlines()
    dosya.close()

with open("english_stop_words.txt","r") as words:
    stop_words = words.read()
    words.close()


stop_word_list =  stop_words.split(",")


#print(mesaj_listesi)

ham_mesajlar=[]
spam_mesajlar=[]

for mesaj in mesaj_listesi:
    if mesaj.startswith("ham"):
        mesaj = mesaj.replace("ham\t","")
        ham_mesajlar.append(mesaj)
    else:
        mesaj = mesaj.replace("spam\t","")
        spam_mesajlar.append(mesaj)

# tüm kelimeleri küçük harfe çevirme

#for mesaj in ham_mesajlar:
#    mesaj=mesaj.lower()
islenmis_spam_mesajlar=[]
para_birimi = "$€£"
rakamlar="0123456789"

for mesaj in ham_mesajlar:
    mesaj=mesaj.lower()
    for noktalama in string.punctuation:
        mesaj = mesaj.replace(noktalama,"") # 
    
    for para in para_birimi:
        mesaj = mesaj.replace(para,"") # 

    for kelime in mesaj.split(" "):
        if str(kelime).isdecimal():
            kelimeler = mesaj.split(" ")
            kelimeler.remove(kelime)
            mesaj = " ".join(kelimeler)
    
    for rakam in rakamlar:
        for kelime in mesaj.split(" "):
            if rakam in kelime:
                kelimeler = mesaj.split(" ")
                kelimeler.remove(kelime)
                mesaj = " ".join(kelimeler)
        
    for kelime in mesaj.split(" "):
        if len(kelime)<3:
            kelimeler = mesaj.split(" ")
            kelimeler.remove(kelime)
            mesaj = " ".join(kelimeler)
    
    for sw in stop_word_list:
        kelimeler = mesaj.split(" ")
        if sw in kelimeler:
            kelimeler.remove(sw)
            mesaj = " ".join(kelimeler)

    mesaj = mesaj.replace("\n","")
    islenmis_spam_mesajlar.append(mesaj)

#print(islenmis_spam_mesajlar)

kelime_sayilar = {}

for spam_mesaj in islenmis_spam_mesajlar:
    for kelime in spam_mesaj.split(" "):
        if kelime not in kelime_sayilar:
            kelime_sayilar[kelime]=1
        else:
            kelime_sayilar[kelime]+=1

print(dict(sorted(kelime_sayilar.items(), key=lambda x: x[1])))

