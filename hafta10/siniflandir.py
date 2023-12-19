from sklearn.model_selection import train_test_split
with open("tum_data.csv", "r") as f:
    lines = f.readlines()
    f.close()

veri = []
etiket = []
for line in lines:
    veri.append(line.split(";")[0])
    etiket.append(line.split(";")[1].replace("\n", ""))

print(veri)

# pip install scikit-learn
# pip3 install scikit-learn
# py -m pip install scikit-learn *
# py -m pip3 install scikit-learn *
# python3 -m pip install scikit-learn


x_train, x_test, y_train, y_test = train_test_split(
    veri, etiket, test_size=0.25)

# buradaki veri bağımlı değişken olarakta adlandırılır.
# buradaki etiket bağımsız değişken olarakta adlandırılır.

print(x_train)
print("eğitim veri boyutu", len(x_train))
print("test veri boyutu", len(x_test))

train_ozellik_liste = []
test_ozellik_liste = []

for mail in x_train:
    ozellik = []
    if "gufum" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    if "gmail" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    if "hotmail" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    if "yahoo" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    if "edu" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    if "gov" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    train_ozellik_liste.append(ozellik)

for mail in x_test:
    ozellik = []
    if "gufum" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    if "gmail" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    if "hotmail" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    if "yahoo" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    if "edu" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    if "gov" in mail:
        ozellik.append(1)
    else:
        ozellik.append(0)

    test_ozellik_liste.append(ozellik)

print(train_ozellik_liste)
print("----------------------------------")
print(test_ozellik_liste)
