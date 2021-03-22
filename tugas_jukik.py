Hari=["Senin","Selasa","Rabu","Kamis","Jum'at","Sabtu","Minggu"]
for i in range(len(Hari)):
    print(i + 1,Hari[i])
    if i==4:
        print("    Hari Masuk Kuliah")
    elif i==6:
        print("    Hari Libur Kuliah")