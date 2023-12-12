import os  # işletim sistemi işlemleri için kullanılır

liste = []

for file in os.listdir("temporary"):

    with open("temporary/"+file, "r") as f:
        lines = f.readlines()
        f.close()

    for line in lines:
        liste.append(str(file) + ";" + line.replace("\n", ""))

site_control = []
for line in liste:
    ogrenci = line.split(";")[0]

    mail = line.split(";")[1]
    etiket = line.split(";")[2]
    site = str(mail.split("@")[1]).split(".")[0]
    # print(ogrenci,  site)
    # print("- web sayfası problemi yok -")

    site_control.append(site + ";" + ogrenci)
    if site_control.count(site + ";" + ogrenci) > 3:
        print("3 den fazla site var", ogrenci, site)

        site_control.remove(site + ";" + ogrenci)


"""
with open("tum_data.csv", "w", encoding="utf-8") as f:
    for line in liste:
        f.write(line)
    f.close()
"""
