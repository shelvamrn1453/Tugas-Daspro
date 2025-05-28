from modules.utils import simpan_ke_file, muat_dari_file

DATA_FILE = "data/calon.json"
data_calon = muat_dari_file(DATA_FILE)

def simpan():
    simpan_ke_file(DATA_FILE, data_calon)

def tambah_calon(id_calon, nama_calon, visi, misi):
    for calon in data_calon:
        if calon["id_calon"] == id_calon:
            return f"Calon dengan ID {id_calon} sudah ada."

    data_calon.append({
        "id_calon": id_calon,
        "nama_calon": nama_calon,
        "visi": visi,
        "misi": misi
    })
    simpan()
    return f"Calon {nama_calon} berhasil ditambahkan."