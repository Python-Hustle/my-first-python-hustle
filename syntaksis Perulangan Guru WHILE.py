"""
Guru sedang mengecek dan meng acc tugas dari siswanya yang berjumlah 50 orang.
"""
tugas = 10
jumlah_tugas_sudah_dicek = 0
jumlah_tugas_sudah_dicek_acc = 0

print(f"{tugas} siswa telah mengumpulkan")
print("kemudian guru mulai mengecek")

print(f"tugas yang sudah dicek dan acc = {jumlah_tugas_sudah_dicek_acc} ")

while jumlah_tugas_sudah_dicek < tugas + 2:
    jumlah_tugas_sudah_dicek = jumlah_tugas_sudah_dicek + 1

    if jumlah_tugas_sudah_dicek_acc == 9:
        print(f"tugas ke-{jumlah_tugas_sudah_dicek_acc + 1} belum di acc")
    else:
        jumlah_tugas_sudah_dicek_acc = jumlah_tugas_sudah_dicek_acc + 1
        print(f"tugas ke-{jumlah_tugas_sudah_dicek_acc} sudah dicek dan dipahami")


if jumlah_tugas_sudah_dicek_acc == tugas:
    print("semua tugas telah di acc")
else:
    print("tidak semua tugas di acc")

print(f"total tugas yang telah cek & acc adalah : {jumlah_tugas_sudah_dicek_acc} lembar tugas")