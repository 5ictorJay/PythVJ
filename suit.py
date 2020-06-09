import random

pilih = ['batu', 'gunting', 'kertas']

def user():
    user = input('batu, gunting, kertas!')
    return user

while True:
    pil1 = pilih[random.randint(0,2)]
    jawaban = user()
    if jawaban == 'batu':
        if pil1 == 'batu':
            print('Wah, seri kita! Coba lagi!')
        elif pil1 == 'gunting':
            print('Weishh menang, selamat!')
            break
        else:
            print('Yahh kalah, ayo coba lagi!')
    
    elif jawaban == 'kertas':
        if pil1 == 'kertas':
            print('Wah, seri kita! Coba lagi!')
        elif pil1 == 'batu':
            print('Weishh menang, selamat!')
            break
        else:
            print('Yahh kalah, ayo coba lagi!')
        
    elif jawaban == 'gunting':
        if pil1 == 'gunting':
            print('Wah, seri kita! Coba lagi!')
        elif pil1 == 'kertas':
            print('Weishh menang, selamat!')
            break
        else:
            print('Yahh kalah, ayo coba lagi!')
    else:
        print('Input kamu salah!')
        
            