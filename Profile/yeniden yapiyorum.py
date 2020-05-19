import pickle
import time
import os

##Functions
global Errorcode
global Sifirla
global Sifirla1
Errorcode = "[Hata]: Yaptığınız işlem algılanmadı."
Sifirla = "Boş Slot"
Sifirla1 = "0"


##Classes
class Bitkiler:
    def __init__(turu,isim,sicaklik,nem):
        turu.isim = isim
        turu.sicaklik = sicaklik
        turu.nem = nem

##Defines

def baslangic():    
    print("<------------------||----------------->")
    print("Bitki Profili Oluştur >> {1}")
    print("<------------------||----------------->")
    sorusor = input("-->: ")
    if sorusor == "1":
        bitkiprofilleri()
    else:
        print("Hata")
        time.sleep(1)
        baslangic()

##

def bitkiprofilleri():
    slotyukle()
    global Errorcode
    global Slotcount1
    global Slotcount2
    global Slotcount3
    global quest1
    slotlar()
    quest1 = input("Seçmek istediğiniz slotu seçiniz")
    #
    if (quest1 == "1"):
        if (Slotcount1 == "Boş Slot"):
            quest11 = str(input("Seçtiğiniz slot boş üzerinde işlem yapmak ister misiniz ?"))
            if (quest11 == "EVET" or "E" or "EVT"):
                print("Bitki oluşturma menüsü")
                time.sleep(1)
                olustur()
                baslangic()
            elif (quest11 != "EVET" or "E" or "EVT"):
                print(Errorcode)
        else:
            menugoster()
    #
    elif (quest1 == "2"):
        if (Slotcount2 == "Boş Slot"):
            quest22 = str(input("Seçtiğiniz slot boş üzerinde işlem yapmak ister misiniz ?"))
            if (quest22 == "EVET" or "E" or "EVT"):
                print("Bitki oluşturma menüsü")
                time.sleep(1)
                olustur()
                baslangic()
            elif (quest22 != "EVET" or "E" or "EVT"):
                print(Errorcode)
        else:
            menugoster()
    #
    elif (quest1 == "3"):
        if (Slotcount3 == "Boş Slot"):
            quest33 = str(input("Seçtiğiniz slot boş üzerinde işlem yapmak ister misiniz ?"))
            if (quest33 == "EVET" or "E" or "EVT"):
                print("Bitki oluşturma menüsü")
                time.sleep(1)
                olustur()
                baslangic()
            elif (quest33 != "EVET" or "E" or "EVT"):
                print(Errorcode)
        else:
            menugoster()
    #
    else:
        print(Errorcode)
        bitkiprofilleri()
    #

##

def olustur():
    global quest1
    
    if (quest1 == "1"):
        print("Oluşturma menüsüne hoşgeldiniz")
        quest = input("Bitkinizin adını giriniz.")
        quest2 = input("Bitkiniz için gerekli olan nem miktarını giriniz.")
        quest3 = input("Ayarlanması istediğiniz sıcaklığı seçiniz.")
        print("Kayıt ediliyor.")
        Bitkiler3 = Bitkiler(quest,quest2,quest3)
        pickle.dump(Bitkiler3,open("BaranBerkDincer","wb"))
        time.sleep(2)
        print("Kaydetme işlemi başarılı")
        bitkikontrol = quest
        pickle.dump(bitkikontrol,open("bitkilistesi","wb"))
        baslangic()
    
        
    elif (quest1 == "2"):
        print("Oluşturma menüsüne hoşgeldiniz")
        quest = input("Bitkinizin adını giriniz.")
        quest2 = input("Bitkiniz için gerekli olan nem miktarını giriniz.")
        quest3 = input("Ayarlanması istediğiniz sıcaklığı seçiniz.")
        print("Kayıt ediliyor.")
        Bitkiler3 = Bitkiler(quest,quest2,quest3)
        pickle.dump(Bitkiler3,open("BaranBerkDincer2","wb"))
        time.sleep(2)
        print("Kaydetme işlemi başarılı")
        bitkikontrol = quest
        pickle.dump(bitkikontrol,open("bitkilistesi2","wb"))
        baslangic()
        
    elif (quest1 == "3"):
        print("Oluşturma menüsüne hoşgeldiniz")
        quest = input("Bitkinizin adını giriniz.")
        quest2 = input("Bitkiniz için gerekli olan nem miktarını giriniz.")
        quest3 = input("Ayarlanması istediğiniz sıcaklığı seçiniz.")
        print("Kayıt ediliyor.")
        Bitkiler3 = Bitkiler(quest,quest2,quest3)
        pickle.dump(Bitkiler3,open("BaranBerkDincer3","wb"))
        time.sleep(2)
        print("Kaydetme işlemi başarılı")
        bitkikontrol = quest
        pickle.dump(bitkikontrol,open("bitkilistesi3","wb"))
        baslangic()
        
##
        
def menugoster():
    slotyukle()
    bilgiyukle()
    global Berk1
    global Berk2
    global Berk3
    global quest1
    global Errorcode
    while True:
        if (quest1 == "1"):       
            print("%s üzerinde işlem yapmaktasınız"%Slotcount1)
            print("Bitkiniz üzerinde yapmak istediğinizi seçiniz.")
            print("|1| Bitkim hakkında bilgi")
            print("|2| Düzenleme menüsü")
            cevap = input("-->: ")
            if (cevap == "1"):  
                print("Bitkinizin istatislikleri:")
                print("Bitkinizin Adı: ", Berk1.isim)
                print("Bitkinizin Sıcaklığı: ",Berk1.sicaklik)
                print("Bitkinizin Nemi: ",Berk1.nem)
                menugoster()
                continue
            elif (cevap == "2"):
                duzenle()
            else:
                print(Errorcode)
        
        elif (quest1 == "2"):       
            print("%s üzerinde işlem yapmaktasınız"%Slotcount2)
            print("Bitkiniz üzerinde yapmak istediğinizi seçiniz.")
            print("|1| Bitkim hakkında bilgi")
            print("|2| Düzenleme menüsü")
            cevap = input("-->: ")
            if (cevap == "1"):    
                print("Bitkinizin istatislikleri:")
                print("Bitkinizin Adı: ", Berk2.isim)
                print("Bitkinizin Sıcaklığı: ",Berk2.sicaklik)
                print("Bitkinizin Nemi: ",Berk2.nem)
                menugoster()
                continue
            elif (cevap == "2"):
                duzenle()
            else:
                print(Errorcode)
        
        elif (quest1 == "3"):       
            print("%s üzerinde işlem yapmaktasınız"%Slotcount3)
            print("Bitkiniz üzerinde yapmak istediğinizi seçiniz.")
            print("|1| Bitkim hakkında bilgi")
            print("|2| Düzenleme menüsü")
            cevap = input("-->: ")
            if (cevap == "1"):
                Bitkiler3 = pickle.load(open("BaranBerkDincer3","rb"))    
                print("Bitkinizin istatislikleri:")
                print("Bitkinizin Adı: ", Berk3.isim)
                print("Bitkinizin Sıcaklığı: ",Berk3.sicaklik)
                print("Bitkinizin Nemi: ",Berk3.nem)
                menugoster()
                continue
            elif (cevap == "2"):
                duzenle()
            else:
                print(Errorcode)
                
        
##

def duzenle():
    slotyukle()
    bilgiyukle()
    global Slotcount1
    global Slotcount2
    global Slotcount3
    global quest1
    global Sifirla
    global Sifirla1
    global Errorcode
    global Berk1
    global Berk2
    global Berk3
    print("Yapmak istediğiniz düzenlemeleyi seçiniz:")
    print("<------------------||----------------->")
    print("|1| - Profil Sil")
    print("|2| - Profil Düzenle")
    print("<------------------||----------------->")
    cevap = input("-->: ")
    if (quest1 == "1"):
        if (cevap == "1"):
            cevap2 = input("Profilinizi gerçekten silmek istediğinize emin misiniz ? Mevcut profil: %s"%Slotcount1)
            if (cevap2 == "EVT" or "EVET" or "E"):
                print("Silme işleminiz başlatılıyor.")
                Siliniyor = Bitkiler(Sifirla,Sifirla1,Sifirla1)
                pickle.dump(Siliniyor,open("BaranBerkDincer","wb"))
                pickle.dump(Sifirla,open("bitkilistesi","wb"))
                time.sleep(2)
                print("Silme işlemi başarılı")
                baslangic()
            else:
                print(Errorcode)
        if (cevap == "2"):
            print("Düzenlemek istediğiniz seçeneği seçiniz.")
            print("|1| Profil İsim")
            print("|2| Sıcaklık Miktarı")
            print("|3| Nem Miktarı")
            cevap2 = input("-->: ")
            if (cevap2 == "1"):
                soru1 = input("Yeni isminizi giriniz. Eski isim: %s"%Slotcount1)
                print("İsminiz %s olarak değiştiriliyor..."%soru1)
                Duzenliyorum = Bitkiler(soru1,Berk1.sicaklik,Berk1.nem)
                pickle.dump(Duzenliyorum,open("BaranBerkDincer","wb"))
                pickle.dump(soru1,open("bitkilistesi","wb"))
                time.sleep(1)
                print("Profilinizin ismi değiştirildi")
                baslangic()
                
            if (cevap2 == "2"):
                soru1 = input("Yeni Sıcaklık Değerinizi giriniz. Eski sıcaklık: %s"%Berk1.sicaklik)
                print("Sıcaklık değeriniz %s olarak değiştiriliyor..."%soru1)
                Duzenliyorum = Bitkiler(Berk1.isim,soru1,Berk1.nem)
                pickle.dump(Duzenliyorum,open("BaranBerkDincer","wb"))
                time.sleep(1)
                print("Sıcaklık değeriniz değiştirildi")
                baslangic()
                
            if (cevap2 == "3"):
                soru1 = input("Yeni Nem Değerinizi giriniz. Eski Nem: %s"%Berk1.nem)
                print("Nem değeriniz %s olarak değiştiriliyor..."%soru1)
                Duzenliyorum = Bitkiler(Berk1.isim,Berk1.sicaklik,soru1)
                pickle.dump(Duzenliyorum,open("BaranBerkDincer","wb"))
                time.sleep(1)
                print("Nem değeriniz değiştirildi")
                baslangic()
            else:
                print(Errorcode)

    if (quest1 == "2"):
        if (cevap == "1"):
            cevap2 = input("Profilinizi gerçekten silmek istediğinize emin misiniz ? Mevcut profil: %s"%Slotcount2)
            if (cevap2 == "EVT" or "EVET" or "E"):
                print("Silme işleminiz başlatılıyor.")
                Siliniyor = Bitkiler(Sifirla,Sifirla1,Sifirla1)
                pickle.dump(Siliniyor,open("BaranBerkDincer2","wb"))
                pickle.dump(Sifirla,open("bitkilistesi2","wb"))
                time.sleep(2)
                print("Silme işlemi başarılı")
                baslangic()
            else:
                print(Errorcode)
        if (cevap == "2"):
            print("Düzenlemek istediğiniz seçeneği seçiniz.")
            print("|1| Profil İsim")
            print("|2| Sıcaklık Miktarı")
            print("|3| Nem Miktarı")
            cevap2 = input("-->: ")
            if (cevap2 == "1"):
                soru1 = input("Yeni isminizi giriniz. Eski isim: %s"%Slotcount2)
                print("İsminiz %s olarak değiştiriliyor..."%soru1)
                Duzenliyorum = Bitkiler(soru1,Berk2.sicaklik,Berk2.nem)
                pickle.dump(Duzenliyorum,open("BaranBerkDincer2","wb"))
                pickle.dump(soru1,open("bitkilistesi2","wb"))
                time.sleep(1)
                print("Profilinizin ismi değiştirildi")
                baslangic()
                
            if (cevap2 == "2"):
                soru1 = input("Yeni Sıcaklık Değerinizi giriniz. Eski sıcaklık: %s"%Berk2.sicaklik)
                print("Sıcaklık değeriniz %s olarak değiştiriliyor..."%soru1)
                Duzenliyorum = Bitkiler(Berk2.isim,soru1,Berk2.nem)
                pickle.dump(Duzenliyorum,open("BaranBerkDincer2","wb"))
                time.sleep(1)
                print("Sıcaklık değeriniz değiştirildi")
                baslangic()
                
            if (cevap2 == "3"):
                soru1 = int(input("Yeni Nem Değerinizi giriniz. Eski Nem: %s"%Berk2.nem))
                print("Nem değeriniz %s olarak değiştiriliyor..."%soru1)
                Duzenliyorum = Bitkiler(Berk2.isim,Berk2.sicaklik,soru1)
                pickle.dump(Duzenliyorum,open("BaranBerkDincer2","wb"))
                time.sleep(1)
                print("Nem değeriniz değiştirildi")
                baslangic()
            else:
                print(Errorcode)

    if (quest1 == "3"):
        if (cevap == "1"):
            cevap2 = input("Profilinizi gerçekten silmek istediğinize emin misiniz ? Mevcut profil: %s"%Slotcount3)
            if (cevap2 == "EVT" or "EVET" or "E"):
                print("Silme işleminiz başlatılıyor.")
                Siliniyor = Bitkiler(Sifirla,Sifirla1,Sifirla1)
                pickle.dump(Siliniyor,open("BaranBerkDincer3","wb"))
                pickle.dump(Sifirla,open("bitkilistesi3","wb"))
                time.sleep(2)
                print("Silme işlemi başarılı")
                baslangic()
            else:
                print(Errorcode)
        if (cevap == "2"):
            print("Düzenlemek istediğiniz seçeneği seçiniz.")
            print("|1| Profil İsim")
            print("|2| Sıcaklık Miktarı")
            print("|3| Nem Miktarı")
            cevap2 = input("-->: ")
            if (cevap2 == "1"):
                soru1 = input("Yeni isminizi giriniz. Eski isim: %s"%Slotcount3)
                print("İsminiz %s olarak değiştiriliyor..."%soru1)
                Duzenliyorum = Bitkiler(soru1,Berk3.sicaklik,Berk3.nem)
                pickle.dump(Duzenliyorum,open("BaranBerkDincer3","wb"))
                pickle.dump(soru1,open("bitkilistesi3","wb"))
                time.sleep(1)
                print("Profilinizin ismi değiştirildi")
                baslangic()
                
            if (cevap2 == "2"):
                soru1 = input("Yeni Sıcaklık Değerinizi giriniz. Eski sıcaklık: %s"%Berk3.sicaklik)
                print("Sıcaklık değeriniz %s olarak değiştiriliyor..."%soru1)
                Duzenliyorum = Bitkiler(Berk3.isim,soru1,Berk3.nem)
                pickle.dump(Duzenliyorum,open("BaranBerkDincer3","wb"))
                time.sleep(1)
                print("Sıcaklık değeriniz değiştirildi")
                baslangic()
                
            if (cevap2 == "3"):
                soru1 = input("Yeni Nem Değerinizi giriniz. Eski Nem: %s"%Berk3.nem)
                print("Nem değeriniz %s olarak değiştiriliyor..."%soru1)
                Duzenliyorum = Bitkiler(Berk3.isim,Berk3.sicaklik,soru1)
                pickle.dump(Duzenliyorum,open("BaranBerkDincer3","wb"))
                time.sleep(1)
                print("Nem değeriniz değiştirildi")
                baslangic()
            else:
                print(Errorcode)
                
##

def slotlar():
    slotyukle()
    global Slotcount1
    global Slotcount2
    global Slotcount3
    print("Slot 1: ",Slotcount1)
    print("Slot 2: ",Slotcount2)
    print("Slot 3: ",Slotcount3)

##

def slotyukle():
    global Slotcount1
    global Slotcount2
    global Slotcount3
    Slotcount1 = pickle.load(open("bitkilistesi","rb"))
    Slotcount2 = pickle.load(open("bitkilistesi2","rb"))
    Slotcount3 = pickle.load(open("bitkilistesi3","rb"))

def bilgiyukle():
    global Berk1
    global Berk2
    global Berk3
    Berk1 = pickle.load(open("BaranBerkDincer","rb"))
    Berk2 = pickle.load(open("BaranBerkDincer2","rb"))
    Berk3 = pickle.load(open("BaranBerkDincer3","rb"))

##

#Start code
baslangic()

