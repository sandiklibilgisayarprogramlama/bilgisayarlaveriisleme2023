with open("SMSSpamCollection", "r") as file:
    mesajlar = file.readlines()
    file.close()

spam_kelimeler=['won','get','prize','reply','claim',
'$','€','£','+','stop','text',
'mobile', 'txt', 'free', 'call']

print(len(spam_kelimeler))
spam_list=[]
ham_list=[]
for mesaj in mesajlar:
    mesaj_list=mesaj.split('\t')
    if mesaj_list[0]=="spam":
        spam_list.append(mesaj)
    else:
        ham_list.append(mesaj)


print(len(spam_list))
sayac=0
for spam_mesaj in spam_list:
    for kelime in spam_kelimeler:
        if kelime in spam_mesaj:
            sayac+=1
            break

print("Spam olarak bulunan mesaj sayısı:")
print(sayac)
print(100*sayac/747)

ham_sayac=0
for ham_mesaj in ham_list:
    for kelime in spam_kelimeler:
        if kelime in ham_mesaj:
            ham_sayac+=1
            break

ham_sayi = len(ham_list)

print("ham olarak bulunan mesaj sayısı:")
print(ham_sayac)
print("Ham  mesaj sayısı: "+str(ham_sayi))
print(100*ham_sayac/ham_sayi)