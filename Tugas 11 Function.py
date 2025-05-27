def reverse_per_kata(kalimat):
    lisKata = kalimat.split() #split digunakan untuk memisahkan kalimat menjadi daftar kata berdasarkan spasi
    hasil = [kata[::-1] for kata in lisKata] #list comprehesion membalikkan kata. "[kata[::-1]]" mengambil semua karakter dalam kata namun dalam urutan terbalik
    return ' '.join(hasil) #menggabungkan kembali daftar kata yang sudah dibalikkan menjadi satu string dengan spasi pemisah " ".

print(reverse_per_kata('AKU CINTA KAMU'))
# Output: "UKA ATNIC UMAK"

def urutkan_kalimat(kalimat, urutan):
    lisKata = kalimat.split() #split digunakan untuk memisahkan kalimat menjadi daftar kata berdasarkan spasi
    hasil = [lisKata[kalimat_item - 1] for kalimat_item in urutan] #"[kalimat_item - 1]" Indeks dalam Python dimulai dari 0, maka menggeser "-1" pengambilan indeks dari indeks ke 4 
    return ' '.join(hasil) #menggabungkan kembali daftar kata yang sudah dibalikkan menjadi satu string dengan spasi pemisah " ".

print(urutkan_kalimat('HARI INI SEDANG BELAJAR PYTHON', [5, 1, 4, 3, 2]))
# Output: "PYTHON HARI BELAJAR SEDANG INI"

def ganti_vokal(kalimat, opsi):
    vokal_kecil = {'a':'4', 'i':'1', 'u':'|_|', 'e':'3', 'o':'0'} #Mengubah huruf vokal kecil menjadi karakter spesial.
    vokal_kapital = {'A':'4', 'I':'1', 'U':'|_|', 'E':'3', 'O':'0'} #Mengubah huruf vokal kapital menjadi karakter spesial.
    hasil = ' ' #enyimpan teks yang sudah dimodifikasi
    for huruf in kalimat:
        if opsi == 1 and huruf in vokal_kecil:
            hasil += vokal_kecil[huruf]
        elif opsi == 2 and huruf in vokal_kapital:
            hasil += vokal_kapital[huruf]
        else:
            hasil += huruf
    return hasil

print(ganti_vokal('Aku Cinta Kamu', 1))
print(ganti_vokal('Aku Cinta Kamu', 2))
# Output1: "Ak|_| C1nt4 K4m|_|"
# Output2: "4ku Cinta Kamu"
        