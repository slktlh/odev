import random 
liste = []
for _ in range(100):
    liste.append(random.randint(0,250))

buyuktenKucuge = []

while liste:
    buyuktenKucuge.append(max(liste))
    liste.remove(max(liste))

print(f"Sayıların büyükten küçüğe sıralanışı: {buyuktenKucuge}")


print(f"En büyük sayı: {buyuktenKucuge[0]}")
print(f"En küçük sayı: {buyuktenKucuge[-1]}")


i = 0
toplam = 0
while i < len(buyuktenKucuge):
    toplam += buyuktenKucuge[i]
    i += 1

print(f"Sayıların toplamı: {toplam}")



ortalama = toplam / 100
print(f"Sayıların ortalaması: {ortalama}")



ii = 0
toplam = 0
listeCift = 0
listeTek = 0

while ii < len(buyuktenKucuge):
    if buyuktenKucuge[ii] % 2 == 0:
        listeCift += 1
        ii += 1
    else:
        listeTek += 1
        ii += 1

print(f"Sayıların {listeCift} tanesi çiftir.")
print(f"Sayıların {listeTek} tanesi tekdir.")



en_cok_tekrar = 0
en_cok_sayi = 0

for sayi in buyuktenKucuge:
    tekrar = 0
    for digerSayi in buyuktenKucuge:
        if sayi == digerSayi:
            tekrar += 1
        if tekrar > en_cok_sayi:
            en_cok_sayi = tekrar
            en_cok_tekrar = sayi

print(f"En çok tekrar eden sayı: {en_cok_tekrar} (toplamda {en_cok_sayi} kere tekrar etmiştir)")