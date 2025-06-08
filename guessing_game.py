import random

def main():
    print("Selamat datang di Permainan Tebak Angka!")
    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    while True:
        try:
            tebakan = int(input("Tebak angka antara 1 sampai 100: "))
            percobaan += 1
            if tebakan < angka_rahasia:
                print("Terlalu kecil!")
            elif tebakan > angka_rahasia:
                print("Terlalu besar!")
            else:
                print(f"Selamat! Kamu menebak angka dalam {percobaan} percobaan.")
                break
        except ValueError:
            print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()