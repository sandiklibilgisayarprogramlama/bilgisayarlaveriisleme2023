from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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
# py -m pip install scikit-learn
# py -m pip3 install scikit-learn
# python3 -m pip install scikit-learn


x_train, x_test, y_train, y_test = train_test_split(
    veri, etiket, test_size=0.25, random_state=23)

# buradaki veri bağımlı değişken olarakta adlandırılır.
# buradaki etiket bağımsız değişken olarakta adlandırılır.

print(x_train)
print("eğitim veri boyutu", len(x_train))
print("test veri boyutu", len(x_test))

vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 3))
train_ozellik_liste = vectorizer.fit_transform(x_train)
test_ozellik_liste = vectorizer.transform(x_test)

print(train_ozellik_liste)

ogretici = DecisionTreeClassifier(random_state=42)
# eğitim verileri ile eğitim yapılıyor.
ogretici.fit(train_ozellik_liste, y_train)

# test verileri ile tahmin yapılıyor.
tahmin = ogretici.predict(test_ozellik_liste)

print(tahmin)  # bilgisayarın öğrenme neticesinde tahmin ettiği değerler
print(y_test)  # gerçek değerler


accuracy = accuracy_score(y_test, tahmin)
print("Doğruluk (Accuracy):", accuracy)

# Sınıflandırma raporu
print("\nSınıflandırma Raporu:")
print(classification_report(y_test, tahmin))
