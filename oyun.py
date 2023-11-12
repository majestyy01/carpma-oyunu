from random import randint
import colorama
from colorama import Fore, Back, Style

#WoxicDEV
#İnstagram : @woxicdev

print(Fore.RED +"-" * 100)
print(Fore.RED +"\t\t  __      __            .__       ________  _______________   ____")
print(Fore.RED +"\t\t /  \    /  \_______  __|__| ____ \______ \ \_   _____/\   \ /   /")
print(Fore.RED +"\t\t \   \/\/   /  _ \  \/  /  |/ ___\ |    |  \ |    __)_  \   Y   / ")
print(Fore.RED +"\t\t  \        (  <_> >    <|  \  \___ |    `   \|        \  \     / ")
print(Fore.RED +"\t\t   \__/\  / \____/__/\_ \__|\___  >_______  /_______  /   \___/  ")
print(Fore.RED +"\t\t        \/             \/       \/        \/        \/    ")
print(Fore.CYAN +"\t\t                                                        @WoxicDEV    ")
print(Fore.RED +"-" * 100, "\n")


print("Yapabileceğine inanıyorum <3")
print(Style.RESET_ALL)
isim=input("İsmin Nedir?: ")
print("Hoşgeldin ",isim)



def carpim(m, a, k):
    if k != "e":
        result = str(m * a)
        if result == k:
            print("\t\t***** Harika,Doğru Bildin! *****")
        else:
            print("\t!!! Yanlış cevap %s olacaktı" % result)
    else:

        secim()


def basla(rng_1, rng_2):
    if rng_1 > 10:
        x = 10
    else:
        x = 5
    for i in range(0, x):
        for j in range(0, x):
            sayi_1 = randint(rng_1, rng_2)
            sayi_2 = randint(rng_1, rng_2)
            print("_" * 50, "\n")
            print("\t%d x %d kaça eşittir? (çıkış = e)" % (sayi_1, sayi_2))
            sonuc = input("sonuc >> ")
            carpim(sayi_1, sayi_2, sonuc)

            if i == 4 and j == 4:
                print("\n *-- Bu seviye bitti herhangi bir seviyeye geçebilsiniz --*\n")
                secim()


def secim():
    print(" Hangi seviyeden başlamak istiyorsunuz (çıkış = e) ?\n")
    print("  1 - Kolay ")
    print("  2 - Orta ")
    print("  3 - Zor")
    print("  4 - Çok zor\n")

    seviye = input(" >> ")

    if seviye == "1":
        basla(1, 6)

    elif seviye == "2":
        basla(6, 12)

    elif seviye == "3":
        basla(12, 25)

    elif seviye == "4":
        basla(25, 100)

    else:
        exit(0)


if __name__ == '__main__':
    secim()
