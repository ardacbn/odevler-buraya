islem = int(input("""HESAP MAKİNESİ
1-Toplama 
2-Çıkarma
3-Çarpma
4-Bölme
5-Kalan
6-Üs Alma 
7-Tam Bölüm
 İşlem Numarasını Gir: """))
sayi1 = int(input("1. sayıyı gir: "))
sayi2 = int(input("2.sayiyi gir: "))
if islem==1 :
    print("Sonuç: ", int(sayi1+sayi2))
elif islem==2 :
    print("Sonuç:", int(sayi1-sayi2))
elif islem==3 :
    print("Sonuç:", int(sayi1*sayi2))
elif islem==4 :
    print("Sonuç:", float(sayi1/sayi2))
elif islem==5 :
    print("Sonuç:", int(sayi1%sayi2))
elif islem==6 :
    print("Sonuç:", int(sayi1**sayi2))
elif islem==7 :
    print("Sonuç:", int(sayi1//sayi2))
else:
    print("Geçersiz işlem")
