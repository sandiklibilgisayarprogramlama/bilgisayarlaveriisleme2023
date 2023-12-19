with open("tum_data.csv", "r") as f:
    lines = f.readlines()
    f.close()

veri = []
etiket = []
for line in lines:
    veri.append(line.split(";")[0])
    etiket.append(line.split(";")[1].replace("\n", ""))

print(etiket)
