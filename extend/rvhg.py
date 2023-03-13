file = open("hogwarts_legacy_reviews.csv", mode="r", encoding="utf-8-sig")
filenew = open("checktime.csv", mode='w', encoding="utf-8-sig")
head = file.readline()
filenew.write(head.strip()+",Rate\n")
row = file.readline()
while row != "":
    row_list = row.split(",") 
    
    play = int(row_list[1])
    rate=""
    if play >= 50:
        rate ="Perfect"
    elif play >= 30:
        rate = "Great"
    else:
        rate = "Good"
    row_new = row.strip() + "," + rate
    filenew.write(row_new +"\n")

    row = file.readline()
