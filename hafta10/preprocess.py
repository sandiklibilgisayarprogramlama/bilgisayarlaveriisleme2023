import os  # işletim sistemi işlemleri için kullanılır

liste = []

for file in os.listdir("temporary"):
    print(file)
    with open("temporary/"+file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()

    for line in lines:
        liste.append(str(file) + ";" + line.replace("\n", ""))

site_control = []
for line in liste:
    ogrenci = line.split(";")[0]

    mail = line.split(";")[1]
    etiket = line.split(";")[2]
    # print(mail)
    site = str(mail.split("@")[1]).split(".")[0]
    # print(ogrenci,  site)
    # print("- web sayfası problemi yok -")

    site_control.append(site + ";" + ogrenci)
    if site_control.count(site + ";" + ogrenci) > 3:
        print("3 den fazla site var", ogrenci, site)


with open("tum_data.csv", "w", encoding="utf-8") as f:
    for line in liste:
        email = line.split(";")[1]
        label = line.split(";")[2]
        f.write(email + ";" + label + "\n")
    f.close()
