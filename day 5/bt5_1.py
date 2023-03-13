# List friends
friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]

# Lấy ra 4 người bạn đầu tiên trong friends
print(friends[0:4])

# Lấy ra 4 người bạn cuối trong friends
print(friends[-4:])

# Đảo ngược danh sách friends
print(friends[::-1])

# Lấy ra những người bạn từ vị trí 1 đến hết
print(friends[1:])

# Copy danh sách ban đầu thành một danh sách mới
newfriend = friends.copy()
print(id(newfriend), id(friends))

# Lấy ra những người bạn từ vị trí 2 đến sát cuối
print(friends[2:-1])
