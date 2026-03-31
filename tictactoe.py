import datetime
import random
import os


if not os.path.exists("files"):
    os.makedirs("files")

oyun_tahtasi = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
oyuncu_skor = 0
bilgisayar_skor = 0


def oyun_tahtasi_goster():
    print("\t " + oyun_tahtasi[1] + " | " + oyun_tahtasi[2] + " | " + oyun_tahtasi[3] + " ")
    print("\t-----------")
    print("\t " + oyun_tahtasi[4] + " | " + oyun_tahtasi[5] + " | " + oyun_tahtasi[6] + " ")
    print("\t-----------")
    print("\t " + oyun_tahtasi[7] + " | " + oyun_tahtasi[8] + " | " + oyun_tahtasi[9] + " ")
    print()
    print("###############")
    print()


def oyuncu_kazandi_mi():
    for i in range(1, 11, 3):
        if oyun_tahtasi[i:i + 3] == ["X", "X", "X"]:
            print("Oyuncu kazandı!")
            return True
    for i in range(1, 4):
        if oyun_tahtasi[i:(i + 7):3] == ["X", "X", "X"]:
            print("Oyuncu kazandı!")
            return True
    if (oyun_tahtasi[1] == oyun_tahtasi[5] == oyun_tahtasi[9] == "X") or \
            (oyun_tahtasi[3] == oyun_tahtasi[5] == oyun_tahtasi[7] == "X"):
        print("Oyuncu kazandı!")
        return True
    return False


def bilgisayar_kazandi_mi():
    for i in range(1, 11, 3):
        if oyun_tahtasi[i:i + 3] == ["O", "O", "O"]:
            print("Bilgisayar kazandı!")
            return True
    for i in range(1, 4):
        if oyun_tahtasi[i:(i + 7):3] == ["O", "O", "O"]:
            print("Bilgisayar kazandı!")
            return True
    if (oyun_tahtasi[1] == oyun_tahtasi[5] == oyun_tahtasi[9] == "O") or \
            (oyun_tahtasi[3] == oyun_tahtasi[5] == oyun_tahtasi[7] == "O"):
        print("Bilgisayar kazandı!")
        return True
    return False




def oyuncunun_kazanmasini_engelle():

    if oyun_tahtasi[1:4].count("X") == 2:
        for i in range(1, 4):
            if oyun_tahtasi[i] == str(i):
                oyun_tahtasi[i] = "O"
                return True

    if oyun_tahtasi[4:7].count("X") == 2:
        for i in range(4, 7):
            if oyun_tahtasi[i] == str(i):
                oyun_tahtasi[i] = "O"
                return True

    if oyun_tahtasi[7:10].count("X") == 2:
        for i in range(7, 10):
            if oyun_tahtasi[i] == str(i):
                oyun_tahtasi[i] = "O"
                return True


    for liste in [[1, 4, 7], [2, 5, 8], [3, 6, 9]]:
        if [oyun_tahtasi[i] for i in liste].count("X") == 2:
            for i in liste:
                if oyun_tahtasi[i] == str(i):
                    oyun_tahtasi[i] = "O"
                    return True


    if [oyun_tahtasi[1], oyun_tahtasi[5], oyun_tahtasi[9]].count("X") == 2:
        for i in [1, 5, 9]:
            if oyun_tahtasi[i] == str(i):
                oyun_tahtasi[i] = "O"
                return True


    if [oyun_tahtasi[3], oyun_tahtasi[5], oyun_tahtasi[7]].count("X") == 2:
        for i in [3, 5, 7]:
            if oyun_tahtasi[i] == str(i):
                oyun_tahtasi[i] = "O"
                return True

    return False


def oyuncu_hamle():
    while True:
        secim = input("Bir sayı seçiniz (1-9):")
        if secim not in oyun_tahtasi or secim == "":
            print("Hatalı hamle, tekrar deneyin.")
            continue
        secim_index = int(secim)
        oyun_tahtasi[secim_index] = "X"
        break


def hamle_yapacak_yer_var_mi():
    for i in range(1, len(oyun_tahtasi)):
        if oyun_tahtasi[i] == str(i):
            return True
    return False


def bilgisayar_hamlesi():
    if oyuncunun_kazanmasini_engelle():
        return
    while hamle_yapacak_yer_var_mi():
        bilgisayar_secim_index = random.randint(1, 9)
        if str(bilgisayar_secim_index) not in oyun_tahtasi:
            continue
        oyun_tahtasi[bilgisayar_secim_index] = "O"
        break



while True:
    oyun_tahtasi_goster()
    oyuncu_hamle()
    if oyuncu_kazandi_mi():
        oyun_tahtasi_goster()
        oyun_tahtasi = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        oyuncu_skor += 1
        secim = input("Çıkmak için X, devam etmek için herhangi bir tuşa basınız: ")
        if secim.upper() == "X":
            break

    if not hamle_yapacak_yer_var_mi():
        print("Hamle yapacak yer kalmadı! Durum berabere.")
        oyun_tahtasi = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        continue

    bilgisayar_hamlesi()
    if bilgisayar_kazandi_mi():
        oyun_tahtasi_goster()
        oyun_tahtasi = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        bilgisayar_skor += 1
        secim = input("Çıkmak için X, devam etmek için herhangi bir tuşa basınız: ")
        if secim.upper() == "X":
            break


print(f"Final Skoru -> Oyuncu: {oyuncu_skor} - Bilgisayar: {bilgisayar_skor}")
with open("files/score.txt", "a") as f:
    f.write(f"{datetime.datetime.now()} > Oyuncu: {oyuncu_skor} - Bilgisayar: {bilgisayar_skor}\n")