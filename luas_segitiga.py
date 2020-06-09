
nama = input('Siapa nama anda:')
nilai = int(input('Nilai ulangan salto berapa:'))

if nilai >= 94:
    grade = 'summa cumlaude'
    print(f'{nama}, kamu mendapat nilai {nilai} dan mendapat predikat {grade}')
elif nilai >= 91:
    grade = 'magna cumlaude'
    print(f'{nama}, kamu mendapat nilai {nilai} dan mendapat predikat {grade}')
elif nilai >= 88:
    grade = 'cumlaude'
    print(f'{nama}, kamu mendapat nilai {nilai} dan mendapat predikat {grade}')

else:
    grade = 'Jangan patah semangat'
    print(f'{nama}, kamu mendapat nilai {nilai} dan mendapat predikat {grade}')
