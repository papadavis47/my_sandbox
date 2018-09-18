
# This is a code challenge re: the dungeon game in Python Collections.
# I passed the challenge with this solution. I had to use Google for some help. ( But I learned something anyway)

def move(player, direction):
    x, y, hp = player
    xdir, ydir = direction
    if x+xdir < 0 or x+xdir > 9:
        hp -= 5
    else:
        x += xdir
    if y+ydir < 0 or y+ydir > 9:
        hp -= 5
    else:
        y += ydir
    return x, y, hp
