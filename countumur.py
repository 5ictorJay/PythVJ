import datetime

def now():
    now = datetime.date.today()
    return now

def born():
    born = input('Tanggal lahir anda (yyyy-mm-dd):')
    return born

list_now = [now().year, now().month, now().day]

# umur = now().year-born.year
# print(umur)

while True:
    pil = input('Apakah anda ingin menghitung umur? (y/n):')
    if pil == 'y':
        born1 = born().split('-')
        born.year = int(born1[0])
        born.month = int(born1[1])
        born.day = int(born1[2])
        if born.month<now().month:
            umur = now().year-born.year
            print(f'Ok, umurmu adalah {umur}')
        elif born.month==now().month:
            if born.day<=now().day:
                umur1 = now().year-born.year
                print(f'Ok, umurmu adalah {umur1}')
            else:
                umur2 = (now().year-born.year)-1
                print(f'Ok, umurmu adalah {umur2}')
        elif born.month>now().month:
            umur3 = (now().year-born.year)-1
            print(f'Ok, umurmu adalah {umur3}')
    else:
        break

