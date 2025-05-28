from .utils import simpan_ke_file, muat_dari_file  # Impor relatif

DATA_FILE = "data/pemilih.json"
data_pemilih = muat_dari_file(DATA_FILE)

def simpan():
    simpan_ke_file(DATA_FILE, data_pemilih)

def tambah_pemilih(nim, nama, jurusan):
    # Cek NIM duplikat
    for pemilih in data_pemilih:
        if pemilih["nim"] == str(nim):  # Konversi ke string untuk konsistensi
            return f"Gagal: NIM {nim} sudah terdaftar!"
    
    # Tambahkan pemilih baru
    data_pemilih.append({
        "nim": str(nim),
        "nama": nama,
        "jurusan": jurusan,
        "sudah_memilih": False,
        "pilihan": None
    })
    
    simpan()  # Simpan ke JSON
    return f"Berhasil: {nama} ({nim}) ditambahkan sebagai pemilih."

# Fungsi tambahan untuk keperluan testing
if _name_ == "_main_":
    # Test tambah pemilih
    print(tambah_pemilih("123", "Budi", "Teknik Informatika"))
    print(tambah_pemilih("456", "Ani", "Sistem Informasi"))