#dict
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}
#Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
print(f"Get value album_name: {album_info['album_name']}")
print(album_info.get("album_name"))
print(f"Get value release_year: {album_info['release_year']}")
print(f"Get value release_year: {album_info.get('release_year')}")
#Thay đổi giá trị của key: release_year từ 1973 thành 1971
album_info["release_year"] = 1971
print(f"Update realease_year: 1973 to {album_info['release_year']}")
#Xóa phần tử với key là track_list
del album_info["track_list"]
print (f"Remove track list:{album_info}")
#Thêm một key mới là amount = 2000 bằng hai cách
album_info["amount"] = 2000
album_info.update(amount = 2000)
print (f"Add new amount to dict:{album_info}")
#Làm trống dict: album_info
album_info.clear()
print(album_info)