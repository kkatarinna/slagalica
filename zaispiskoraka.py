from os import sep
import random

def tekstKoraka():
    print("Ovo je igra korak po korak!")
    print("Ovako se ova igra igra:")
    print("Dobijaćš rečenice koje te asociraju na jedan pojam, tvoj zadatak je da pogodiš koji je to pojam")
    print("Budi pažljiv, imaš samo 6 koraka dok")
    print("Ukoliko ne želite da pogađate ovaj pojam unesite sa tastature: 'dalje' i to će odabrati nove korake za vas :)")


def odaberiKorake():
    file = open("D:/fakultet/osnove programiranja/vezbe/domaci/korak po korak/koraci.txt", "r", encoding="utf-8")
    content = file.readlines()
    n = 7 #koliko delova ima lista u listi  
    x = [content[i:i + n] for i in range(0, len(content), n)] #podeli listu na podliste
    randombr = random.randint(0,31) #generise random indeks za podlistu u listi

    kombinacija = x[randombr]
    file.close()
    return kombinacija

def dalje():
    kombinacija = odaberiKorake()
    pogodiKorake(kombinacija)

def pogodiKorake(koraci):
    i=0
    while i < 6:
        print("KORAK >>>>>>>>>>>>>>>",koraci[i][:-1],"<<<<<<<<<<<<<<<")
        print(koraci[6][:-1])
        while True:
            unos = input("Unesi: ")
            unos = unos.title()
            res = unos.isalpha()
            if res == True:
                break
            else:
                print("Odgovor može da sadrži samo slova! Unesi opet: ")

        if unos == "Dalje":
            print("====================================================")
            print("====================================================")
            main()
            break
        
        elif unos == koraci[6][:-1]:
            print("Bravo, tvoje rešenje je tačno!")
            print("Ti si POBEDNIK u ovoj igri!")
            bodoviKorak(i)
            break
        else:
            i += 1
    if i == 6:
        print("Nažalost izgubio si")   
    return i

def bodoviKorak(korak):
    bodovi = (6 - korak) * 5
    print("Broj osvojenih bodova u ovoj igri je:",bodovi)
    print("Čestitamo!")

def main():
    tekstKoraka()
    koraci = odaberiKorake()
    pogodiKorake(koraci)

if __name__ == "__main__":
    main()