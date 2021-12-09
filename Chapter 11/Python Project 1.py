from datetime import *

try:
    def diffDate(x):
        skrg = datetime.date(datetime.now())
        print('Hari ini tanggal: ', skrg)
        splitt = x.split('-')
        x = date(year = int(splitt[0]), month = int(splitt[1]), day = int(splitt[2]))
        selisih = x - skrg
        print(selisih.days)
        return

    tanggal = input('Masukkan format tanggal (tahun-bulan-tanggal): ')
    diffDate (tanggal)
except ValueError:
    print('Maaf format tanggal salah')
except IndexError:
    print('Maaf format tanggal salah')