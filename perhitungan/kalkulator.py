def tambah ():
    print("\t1. penjumlahan")
    a = int(input("\tmasukan nilai x= "))
    b = int(input("\tmasukan nilai y="))
    c = a+b
    print ("\tx+y=",c)
    tanya()
def kurang ():
    print("\t2. pengurangan")
    a = int(input("\tmasukan nilai x= "))
    b = int(input("\tmasukan nilai y="))
    c = a-b
    print ("\tx-y=",c)
    tanya()
def bagi ():
    print("\t3. pembagian")
    a = int(input("\tmasukan nilai x= "))
    b = int(input("\tmasukan nilai y="))
    c = a/b
    print ("\tx/y=",c)
    tanya()
def kali ():
    print("\t4. pembagian")
    a = int(input("\tmasukan nilai x= "))
    b = int(input("\tmasukan nilai y="))
    c = a*b
    print ("\tx*y=",c)
    tanya()
def tanya():
    tanya = input("\n\tkembali ke menu kalkulator (y/t)? ")
    if tanya == "y":
        cal()
    elif tanya == "t":
        exit
    else:
        print ("\n\tsalah input..................!!!!")
        
def cal():
    print("\n\t=================================")
    print("\tprogram kalkulator sederhana")
    print("\n\t=================================")
    print("\t1.penjumlahan")
    print("\t2.pengurangan")
    print("\t3.pembagian")
    print("\t4.perkalian")
    print("\n\t=================================")
    print("\silahkan pilih 1-4")
    print(" ")
    pil = input(" masukan pilihan : ")
    if pil == '1':
        tambah()
    elif pil == '2':
        kurang()
    elif pil == '3':
        bagi()
    elif pil == '4':
        kali()
    else:
        print("maaf, input yang anda masukkan salah")
        print("coba ulangi kembali...")
        tanya()
    
    
    
