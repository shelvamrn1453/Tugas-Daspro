from modules.pemilih import data_pemilih
from modules.calon import data_calon

def hitung_hasil():
    hasil = {calon["id_calon"]: 0 for calon in data_calon}
    for pemilih in data_pemilih:
        if pemilih["sudah_memilih"] and pemilih["pilihan"]:
            hasil[pemilih["pilihan"]] += 1
    return hasil

def tampilkan_hasil():
    hasil = hitung_hasil()
    if not hasil:
        print("Belum ada suara yang masuk.")
        return

    print("\n=== Hasil Pemungutan Suara ===")
    for calon in data_calon:
        suara = hasil.get(calon["id_calon"], 0)
        print(f'{calon["nama_calon"]} ({calon["id_calon"]}): {suara} suara')

def tampilkan_statistik():
    total_pemilih = len(data_pemilih)
    pemilih_sudah = sum(1 for p in data_pemilih if p["sudah_memilih"])
    pemilih_belum = total_pemilih - pemilih_sudah
    persentase = (pemilih_sudah / total_pemilih) * 100 if total_pemilih else 0

    print("\n=== Statistik Partisipasi ===")
    print(f"Total Pemilih: {total_pemilih}")
    print(f"Sudah Memilih: {pemilih_sudah}")
    print(f"Belum Memilih: {pemilih_belum}")
    print(f"Persentase Partisipasi: {persentase:.2f}%")