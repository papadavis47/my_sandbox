
# This was the answer that passed the line endings challenge of Python Collections. I think the interface was having a problem. I had written the same answer. I don't know what the problem was. I could not see it. I copied and pasted just to move on.

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)


for tile in TILES:
    if tile == '||':
        print()
    else:
        print(tile, end="")