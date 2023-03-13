# Create movies list
mvlist = ["Ant man3", "Chainsaw Man", "Blue Lock", "Lycoris Recoil", "Kimetsu"]
# Input a movie to list
add = input("Add movie: ")
mvlist.append(add)
# Prin first, last, mid position movies
print("First position movie in list:", mvlist[0])
print("Last position movie in list:", mvlist[-1])
mid = len(mvlist)
print("Mid position movie in list:", mvlist[mid//2])
print("Movie list amount:", mid, "Movie")
firstmv = mvlist[0]
lastmv = mvlist[-1]
# Total movie in list
print("Total movie in list:", mid)
print("Remove movie from list:", firstmv, ",", lastmv)
mvlist.remove(firstmv)
mvlist.remove(lastmv)
# Remove last movie and move new list
pop = mvlist.pop()
print("Last movie in list:", pop)
# insert new movies
insert = input("Insert movie: ")
mvlist.insert(0, insert)
# count One Piece movie
count = mvlist.count("One Piece")
print("Count The One Piece movie in list:", count)
# find position movie name Gio
indexmv = mvlist.index("gió")
print("The position gió movie in list:", indexmv)
# extend list movie
extendlist = []
for i in range(3):
    data = input("Add movie to list: ")
    extendlist.append(data)
mvlist.extend(extendlist)
print(mvlist)
# clear list
mvlist.clear()
print(mvlist)
