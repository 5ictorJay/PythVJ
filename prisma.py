class Segitiga:
    #constructor, init=initial
    def __init__(self, jenis):
        self.jenis = jenis
        self.alas = int(input(f'Alas segitiga:'))
        self.tinggi = int(input(f'Tinggi segitiga:'))

    def lain(self):
        tg = int(input(f'Tinggi prisma:'))
        volume = ((self.alas*self.tinggi)/2)*tg
        print(f'Volume prisma segitiga:{volume}')

sgtg = Segitiga('siku-siku')
sgtg.lain()