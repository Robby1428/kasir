print("----------------- ARTISAN BEVERAGE -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. ABS Favourite Pizza - Rp 30000")
   print("2. Meaty Pizza - Rp 35000")
   print("3. Urban Farm Pizza - Rp 35000")
   print("4. Ayam Sambal Matah Pizza - Rp 45000")
   print("5. Rendah Sapi Pizza - Rp 45000")
   print("6. Banana Starberry - Rp 30000")
   print("7. Roasty Apple - Rp 30000")
   print("8. None - Rp 0")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*30000
       print (porsi," porsi ABS Favourite Pizza = Rp", totalmkn)
       mkn=("ABS Favourite Pizza")
   elif nomor==2:
       totalmkn=porsi*35000
       print (porsi," porsi Meaty Pizza = Rp", totalmkn)
       mkn=("Meaty Pizza")
   elif nomor==3:
       totalmkn=porsi*35000
       print (porsi," porsi Urban Farm Pizza = Rp", totalmkn)
       mkn=("Urban Farm Pizza")
   elif nomor==4:
       totalmkn=porsi*45000
       print (porsi," porsi Ayam Sambal Matah Pizza = Rp", totalmkn)
       mkn=("Ayam Sambal Matah Pizza")
   elif nomor==5:
       totalmkn=porsi*45000
       print (porsi," porsi Rendah Sapi Pizza = Rp", totalmkn)
       mkn=("Rendah Sapi Pizza")
   elif nomor==6:
       totalmkn=porsi*30000
       print (porsi," porsi Banana Starberry = Rp", totalmkn)
       mkn=("Banana Starberry")
   elif nomor==7:
       totalmkn=porsi*30000
       print (porsi," porsi Roasty Apple = Rp", totalmkn)
       mkn=("Roasty Apple")
   elif nomor==8:
       totalmkn=porsi*0
       print (porsi," porsi 0 = Rp", totalmkn)
       mkn=("0")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Italian Coffee Mocktail - Rp 15000")
   print("2. Italian Tea Mocktail - Rp 15000")
   print("3. Italian Milk Blend - Rp 15000")
   print("4. Italian Soda - Rp 15000")
   print("5. None - Rp 0")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*15000
       print (gelas, " Italian Coffee Mocktail = Rp", totalmnm)
       mnm=("Italian Coffee Mocktail")
   elif nomor==2:
       totalmnm=gelas*15000
       print (gelas, " Italian Tea Mocktail = Rp", totalmnm)
       mnm=("Italian Tea Mocktail")
   elif nomor==3:
       totalmnm=gelas*15000
       print (gelas, " Italian Milk Blend = Rp", totalmnm)
       mnm=("Italian Milk Blend")
   elif nomor==4:
       totalmnm=gelas*15000
       print (gelas, " Italian Soda = Rp", totalmnm)
       mnm=("Italian Soda")
   elif nomor==5:
       totalmnm=gelas*0
       print (gelas, " None = Rp", totalmnm)
       mnm=("None")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")