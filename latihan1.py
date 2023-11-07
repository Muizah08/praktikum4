import random

n = int(input("Masukkan nilai n: "))  # Meminta pengguna untuk memasukkan nilai n

count = 0  # Inisialisasi penghitung
while count < n:
    random_number = random.random()  # Menghasilkan bilangan acak antara 0 dan 1
    if random_number < 0.5:
        print(random_number)
        count += 1  # Menambahkan 1 ke penghitung

print("Selesai")
