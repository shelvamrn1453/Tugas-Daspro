from modules.pemilih import data_pemilih, simpan as simpan_pemilih
from modules.calon import data_calon

def lakukan_voting(nim, id_calon):
    for pemilih in data_pemilih:
        if pemilih["nim"] == nim:
            if pemilih["sudah_memilih"]:
                return f"Pemilih dengan NIM {nim} sudah memilih."
            break
    else:
        return f"Pemilih dengan NIM {nim} tidak ditemukan."

    for calon in data_calon:
        if calon["id_calon"] == id_calon:
            break
    else:
        return f"Calon dengan ID {id_calon} tidak ditemukan."

    for pemilih in data_pemilih:
        if pemilih["nim"] == nim:
            pemilih["sudah_memilih"] = True
            pemilih["pilihan"] = id_calon
            break

    simpan_pemilih()
    return f"Pemilih {nim} berhasil memberikan suara untuk calon {id_calon}."