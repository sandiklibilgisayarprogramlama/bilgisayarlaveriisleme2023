
satir=input("v için gerekli satır sayısını giriniz: ")

if int(satir) <2 :
    print("Satır sayısı 2'den küçük olamaz.")
    exit() #programı sonlandırır.


for i in range(int(satir),0,-1):
    print(" "*i+"*")

"""
* *
 *

*   *
 * *
  *
*           *   11           7           4
 *         *   9             6           3
  *       *   7              5           2
   *     *   5               4           1
    *   *  3                 3           0
     * *  1                  2           -1
      *   
"""