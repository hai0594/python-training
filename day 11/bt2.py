def print_show_info(x):
    return f"{x['title']} ({x['initial_release']}) - {x['seasons']} seasons"


tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

print(print_show_info(tv_show))

