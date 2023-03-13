file = open("excelfile.csv", mode="r", encoding="utf-8-sig")
file_new = open("exceldata.csv", mode="w", encoding="utf-8-sig")
head = file.readline()
file_new.write(head.strip() + ", Điểm Trung Bình, Học Lực\n")
row = file.readline()
while row != "":

    row_list = row.split(",")

    match = float(row_list[2])
    lit = float(row_list[3])

    ave = (match + lit)/2
    ave = round(ave, 1)

    rank = ""
    if ave >= 8.0:
        rank = "Giỏi"
    elif ave >= 7.0:
        rank = "Khá"
    else:
        rank = "Trung Bình"

    row_new = row.strip() + "," + str(ave) + "," + rank
    file_new.write(row_new + "\n")
    row = file.readline()
