"""
Guru sedang mengecek tugas dari siswanya yang berjumlah 50 orang.
"""
jumlah_tugas = 20
print(f"{jumlah_tugas} siswa telah mengumpulkan tugas")
print("kemudian guru mulai mengecek")

jumlah_tugas_sudah_dicek = 0
for jumlah_tugas_sudah_dicek in range (1, jumlah_tugas+1):
    print(f"tugas ke-{jumlah_tugas_sudah_dicek} telah di cek")

print(f"guru telah mengecek {jumlah_tugas_sudah_dicek} tugas siswa")