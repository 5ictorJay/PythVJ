pemakaian = input('Apakah anda ingin pakai kalkulator? (Y/N):')
if pemakaian == 'Y':
    angka1 = int(input('Masukkan angka pertama:'))
    print(f'Baiklah, angka pertama anda adalah {angka1}')
    operator = int(input(
    'sekarang pilihlah operator berikut: 1 = tambah, 2 = kurang, 3 = kali, 4 = bagi:'))
    if operator == 1:
        angka2 = int(input('Masukkan angka kedua:'))
        hasil = angka1 + angka2
        print(f'Angka pertama anda adalah {angka1}, ditambah angka kedua {angka2}, hasilnya {hasil}')
    elif operator == 2:
        angka2 = int(input('Masukkan angka kedua:'))
        hasil = angka1 - angka2
        print(f'Angka pertama anda adalah {angka1}, dikurang angka kedua {angka2}, hasilnya {hasil}')
    elif operator == 3:
        angka2 = int(input('Masukkan angka kedua:'))
        hasil = angka1 * angka2
        print(f'Angka pertama anda adalah {angka1}, dikali angka kedua {angka2}, hasilnya {hasil}')
    elif operator == 4:
        angka2 = int(input('Masukkan angka kedua:'))
        hasil = angka1 / angka2
        print(f'Angka pertama anda adalah {angka1}, dibagi angka kedua {angka2}, hasilnya {hasil}')

elif pemakaian == 'N':
    print('Okdeh, siap bos')


    