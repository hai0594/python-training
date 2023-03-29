def points(games):
    total_point = 0
    for game in games:
        x,y = game.split(':')
        if x > y:
            total_point += 3
        elif x < y:
            pass
        else:
            total_point += 1
    return total_point
print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
