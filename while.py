import time

awal= int(input('Insert time (in seconds):'))
quest= input('Ready to start? (Y/N):')
if quest == 'Y':
    while awal > 0:
        time.sleep(1)
        print(awal)
        awal -= 1
    print('DONE!')

else:
    while quest != 'Y':
        quest= input('Ready to start? (Y/N):')
        if quest == 'Y':
            while awal > 0:
                time.sleep(1)
                print(awal)
                awal -= 1
            print('DONE!')

    


