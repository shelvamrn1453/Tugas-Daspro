import json
import os

def simpan_ke_file(nama_file, data):
    # Pastikan folder tujuan ada
    folder = os.path.dirname(nama_file)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    
    with open(nama_file, "w") as f:
        json.dump(data, f, indent=4)

def muat_dari_file(nama_file):
    # Jika file tidak ada, buat file dengan array kosong
    if not os.path.exists(nama_file):
        folder = os.path.dirname(nama_file)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        with open(nama_file, "w") as f:
            json.dump([], f)
        return []
    
    # Jika file ada, baca dan handle error
    try:
        with open(nama_file, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []  # Kembalikan array kosong jika file korup