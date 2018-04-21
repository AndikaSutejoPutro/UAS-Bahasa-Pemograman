import texttable as tt
def pembayaran():
    print("\n============================================")
    nama = input("\n\tmasukkan nama = ")
    nim = input("\tmasukkan nim = ")
    semester=input("\tmasukkan semester saat ini = ")
    print("\n\t---pilihan pembayaran---")
    print("\t1. pembayaran spp")
    print("\t2. pembayaran uts")
    print("\t3. pembayaran uas")
    print("\t4. pembayaran spp & uts")
    print("\t5. pembayaran spp & uas")
    pilih = input("\n\tsilahkan pilih : ")
    if pilih == "1" :
        spp()
    elif pilih == "2" :
        uts()
    elif pilih == "3" :
        uas()
    elif pilih == "4" :
        spp_uts()
    elif pilih == "5" :
        spp_uas()
    else:
       exit
       tanya()

def spp():
    bulan = int(input("\n\tjumlah bulan yang di bayar = "))
    bulan = float(bulan)
    total = 350000 * bulan
    print("==========================================================")
    print("\ttotal bayar spp Rp.350000 *" ,bulan," = Rp.",total)

def uas():
    matkul =int(input("\n\tjumlah mata kuliah = "))
    matkul =float(matkul)
    byr_uas = 50000*matkul
    print("==========================================================")
    print("\ttotal bayar uas Rp.50000 *",matkul," = Rp.",byr_uas)

def uts():
    matkul =int(input("\n\tjumlah mata kuliah = "))
    matkul =float(matkul)
    byr_uts = 25000*matkul
    print("==========================================================")
    print("\ttotal bayar uas Rp.25000 *",matkul," = Rp.",byr_uts)

def spp_uas():
    bulan =int(input("\n\tjumlah bulan yang di bayar = "))
    matkul =int(input("\tjumlah mata kuliah = "))
    matkul =float(matkul)
    bulan =float(bulan)
    total_spp = 350000 * bulan
    byr_uas = 50000*matkul
    total = total_spp + byr_uas + 5000
    print("\n\ttotal bayar spp Rp.350000 * ",bulan," = Rp.",total_spp)
    print("\ttotal bayar uas Rp.25000 * ",matkul," = Rp.",byr_uas)
    print("\tbiaya tambahan server sebesar Rp.5000")
    print("============================================================")
    print("\ttotal yang harus di bayar Rp.",total)

def spp_uts():
    bulan = int(input("\n\tjumlah bulan yang di bayar = "))
    matkul = int(input("\tjumlah mata kuliah = "))
    matkul = float(matkul)
    bulan = float(bulan)
    total_spp = 3500000 * bulan
    byr_uts = 25000 * matkul
    total = total_spp + byr_uts + 5000
    print("\n\ttotal bayar uas Rp.50000 * ",matkul," = Rp.",byr_uts)
    print("\ttotal bayar spp Rp.350000 * ",bulan," = Rp.",total_spp)
    print("\tbiaya tambahan server sebesar Rp.5000")
    print("===========================================================")
    print("\ttotal yang harus di bayar" ,total)
