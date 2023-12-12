import os  # işletim sistemi işlemleri için kullanılır

liste = []

for file in os.listdir("temporary"):

    with open("temporary/"+file, "r") as f:
        lines = f.readlines()
        f.close()

    for line in lines:
        liste.append(str(file) + ";" + line)


"""
with open("tum_data.csv", "w", encoding="utf-8") as f:
    for line in liste:
        f.write(line)
    f.close()
"""
