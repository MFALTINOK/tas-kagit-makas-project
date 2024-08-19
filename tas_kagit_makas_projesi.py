
# Import edilmesi gereken kütüphaneler
import random
import time

# Ana fonksiyon tanımlaması
def tas_kagit_makas_MELIH_FAHRI_ALTINOK():

    # Oyun elemanlarının oluşturulması
    eleman_liste = ["tas","kagit","makas"]
    
    # Kazanma durumlarını dictionary yaptım
    kazanma = {"tas": "makas", "makas": "kagit", "kagit": "tas"}

    # Arttırılacak değerlerin girilmesi     
    oyuncu_puani = 0                    
    bilgisayar_puani = 0
    oyuncu_tur_puani = 0
    bilgisayar_tur_puani = 0
    oyun = 0                    # Buradaki oyun değeri aslında turu ifade ediyor.
    round = 0                   # Round her turun içindeki bir müsabakaya denk.

    # Oyun tanıtım görseli
    print("  _ _ _ _ _ _ _ _ _  _ _ _  _ _ _    _ _ _ _ _ _ ")
    print(" /_ _/_ _/_ _/_ _ /-/   /  /   /-/  / \\\\     / \\\\/-")
    print("      //    /-/    / / /  /   /-/  /   \\\\   /   \\\\/-")
    print("     //    /-/    / / /__/_ _/_/  /  _  \\\\_/ _  \\\\/-")
    print("    //    /-/    / / /____/_/_   /  / \\\\    / \\\\  /-")
    print("   //    /-/    / / /   /   /-/ /  /   \\\\  /   \\\\ /-")
    print("  //____/-/    /___/_  /___/-/ /__/     \\\\/      /-")
    print("____*|*_________________________by Melih Fahri Altınok")

    # Selamlama ve oyun tanıtım mesajları
    print("\nMerhaba, burada olduğuna göre benimle taş-kağıt-makas oynamak istiyorsun demektir :)")
    
    print("\n** Taş makası kırabilir ama kağıt taşı sarabilir.   Yani taş makası yener ama kağıda yenilir.")
    print("** Makas kağıdı kesebilir ama taş makası kırabilir. Yani makas kağıdı yener ama taşa yenilir.")
    print("** Kağıt taşı sarabilir ama makas kağıdı kesebilir. Yani kağıt taşı yener ama makasa yenilir.")
    
    print("\n_________________| Bu üç ifadeden birini seçeceksin, ben de rastgele birini seçeceğim")
    print("_________________| Her oyun birden fazla tur sürecek, iki tur alan oyunu kazanacak")
    print("_________________| İki oyun oynayacağız, kazanma, kaybetme ve beraberlik söz konusu")
    print("_________________| Oyun bitmeden çıkmanı tavsiye etmem, ama olur da acil şekilde çıkman gerekirse exit ile oyunu sonlandırabilirsin\n")

    ifade = input(". . . . . .Kazanma kaybetme durumları için 'a', oyuna başlamak için 'basla' yaz(çıkış için exit)..: ")
    
    # Kazanma kaybetme durumlarının oyuncuya gösterilmesi
    if ifade == "a":
        print("BİLGİSAYAR - OYUNCU - KAZANMA DURUMU")
        print("tas        - makas  - bilgisayar kazanır")
        print("tas        - kagit  - oyuncu     kazanır")
        print("kagit      - tas    - bilgisayar kazanır")
        print("kagit      - makas  - oyuncu     kazanır")
        print("makas      - kagit  - bilgisayar kazanır")
        print("makas      - tas    - oyuncu     kazanır")
        ifade2 = input("Ana ekrana dönmek için 'b' girin..: ")
        if ifade2 == "b":
            return tas_kagit_makas_MELIH_FAHRI_ALTINOK()
    
    # Oyun başlangıcı
    elif ifade == "basla":
            
            # Gerekli değerler
            oyun += 1
            round += 1
            
            # 1. turun döngüsü ------------------------------------> İki turu tek döngü halinde yapmak istedim ancak olmadı o yüzden iki turun döngüsü:)
            while True:
                if oyuncu_puani == 2 or bilgisayar_puani == 2:
                    break
                
                # Round
                print("\n&&&&&&&&&&&&&&&&_ ROUND -",round,"_&&&&&&&&&&&&&&&&&&&")
                oyuncu_eleman = input(". . . . . Hangisini seçtin(tas, kagit, makas)(çıkış için exit)..: ")

                # Çıkış ve yanlış girdi durumları                
                if oyuncu_eleman not in eleman_liste:
                    if oyuncu_eleman == "exit":
                        exit()
                    else:
                        print("\nAnlamadım, lütfen şunlardan birini yaz(tas, kagit, makas)")
                
                # Doğru girdi girilmesi
                elif oyuncu_eleman in eleman_liste:
                    bilgisayar_eleman = random.choice(eleman_liste)
                    print(". . . . . Bilgisayar seçimi..: ", bilgisayar_eleman)
                    if bilgisayar_eleman == oyuncu_eleman:
                        print("\nBerabere.")
                        oyuncu_puani += 1
                        bilgisayar_puani += 1
                        print("\nOyuncu......: ", oyuncu_puani)
                        print("Bilgisayar..: ", bilgisayar_puani)
                        round += 1
                    elif bilgisayar_eleman in kazanma and oyuncu_eleman == kazanma[bilgisayar_eleman]:
                        print("\nBen kazandım yani bilgisayar heheheh..")
                        bilgisayar_puani += 1
                        print("\nOyuncu......: ", oyuncu_puani)
                        print("Bilgisayar..: ", bilgisayar_puani)
                        round += 1
                    elif oyuncu_eleman in kazanma and bilgisayar_eleman == kazanma[oyuncu_eleman]:
                        print("\nSen kazandın, tebrik ederim ;)")
                        oyuncu_puani += 1
                        print("\nOyuncu......: ", oyuncu_puani)
                        print("Bilgisayar..: ", bilgisayar_puani)
                        round += 1
            
            # İlk tur değerlendirme mesajı
            if bilgisayar_puani > oyuncu_puani:
                print("\n** İlk turu ben kazandım, sıra ikinci turda. **")
                bilgisayar_tur_puani += 1
            elif oyuncu_puani > bilgisayar_puani:
                print("\n** İlk turu sen kazandın ama her şey değişebilir. Sıra ikinci turda **")
                oyuncu_tur_puani += 1
            elif oyuncu_puani == bilgisayar_puani:
                print("\n** Bakalım ikinci turda da beraberlik devam edecek mi **")
                oyuncu_tur_puani += 1
                bilgisayar_tur_puani += 1
            
            # Kazanılan tur puanları
            print("\nBilgisayar tur puanı..: ", bilgisayar_tur_puani)
            print("Oyuncu tur puanı......: ", oyuncu_tur_puani)
            
            # Değişkenlerin arttırılması ve sıfırlanması
            oyun += 1
            round = 1
            oyuncu_puani = 0
            bilgisayar_puani = 0
            
            # 2. tur döngüsü
            while True:
                if oyuncu_puani == 2 or bilgisayar_puani == 2:
                    break
                print("\n&&&&&&&&&&&&&&&&_ ROUND -",round,"_&&&&&&&&&&&&&&&&&&&")
                oyuncu_eleman = input(". . . . . Hangisini seçtin(tas, kagit, makas)..: ")
                if oyuncu_eleman not in eleman_liste:
                    print("\nAnlamadım, lütfen şunlardan birini yaz(tas, kagit, makas)")
                elif oyuncu_eleman in eleman_liste:
                    bilgisayar_eleman = random.choice(eleman_liste)
                    print(". . . . . Bilgisayar seçimi..: ", bilgisayar_eleman)
                    if bilgisayar_eleman == oyuncu_eleman:
                        print("\nBerabere.")
                        oyuncu_puani += 1
                        bilgisayar_puani += 1
                        print("\nOyuncu......: ", oyuncu_puani)
                        print("Bilgisayar..: ", bilgisayar_puani)
                        round += 1
                    elif bilgisayar_eleman in kazanma and oyuncu_eleman == kazanma[bilgisayar_eleman]:
                        print("\nBen kazandım yani bilgisayar heheheh..")
                        bilgisayar_puani += 1
                        print("\nOyuncu......: ", oyuncu_puani)
                        print("Bilgisayar..: ", bilgisayar_puani)
                        round += 1
                    elif oyuncu_eleman in kazanma and bilgisayar_eleman == kazanma[oyuncu_eleman]:
                        print("\nSen kazandın, tebrik ederim ;)")
                        oyuncu_puani += 1
                        print("\nOyuncu......: ", oyuncu_puani)
                        print("Bilgisayar..: ", bilgisayar_puani)
                        round += 1
            
            # Tur değerlendirme mesajı
            if bilgisayar_puani > oyuncu_puani:
                print("\n** İkinci turu ben kazandım **")
                bilgisayar_tur_puani += 1
            elif oyuncu_puani > bilgisayar_puani:
                print("\n** Tebrikler, ikinci turu sen kazandın **")
                oyuncu_tur_puani += 1
            elif oyuncu_puani == bilgisayar_puani:
                print("\n** İkinci tur berabere bitti **")
                oyuncu_tur_puani += 1
                bilgisayar_tur_puani += 1

            # Oyun sonu puanları ve değerlendirme mesajı
            print("\nBilgisayar tur puanı..: ", bilgisayar_tur_puani)
            print("Oyuncu tur puanı......: ", oyuncu_tur_puani)

            if bilgisayar_tur_puani > oyuncu_tur_puani:
                print("\n/////////////Oyunu ben kazandım, bu oyun böyle oynanır:)")
            elif oyuncu_tur_puani > bilgisayar_tur_puani:
                print("\n/////////////Tebrik ederim oyunu sen kazandın:)")
            elif bilgisayar_tur_puani == oyuncu_tur_puani:
                print("\n/////////////Oyun bitti, dostluk kazandı:)")
            
            # Tekrar oynamak isteyip istememe    
            oyuncu_istek = input("\nBir daha oynamak ister misin(evet, hayır)..: ")
            if oyuncu_istek == "evet":
                bilgisayar_karar = ["evet","hayır"]
                bilgisayar_istek = random.choice(bilgisayar_karar)
                if bilgisayar_istek == oyuncu_istek:
                    print("\nBana da olur hadi bir daha oynayalım")
                    time.sleep(1)
                    return tas_kagit_makas_MELIH_FAHRI_ALTINOK()
                elif bilgisayar_istek == "hayır":
                    print("Yalnız benim işim çıktı, daha sonra oynayalım olur mu:)")
                    exit()
            elif oyuncu_istek == "hayır":
                print("Peki o zaman görüşmek üzere:)")
                exit()
    
    # Oyun başında girilen ifade çıkış ise
    elif ifade == "exit":
        exit()

    # Oyun başında girilen ifade geçersizse
    else:
        print("Anlamadım, lütfen geçerli bir durum gir.")
        time.sleep(1)
        return tas_kagit_makas_MELIH_FAHRI_ALTINOK()
            

# Oyunu çalıştıran fonksiyon
tas_kagit_makas_MELIH_FAHRI_ALTINOK()