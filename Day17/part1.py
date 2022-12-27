from itertools import cycle
from pathlib import Path

rocks = cycle([ # top down
    [[0,3]],
    [[1,1],
     [0,2],
     [1,1]],
    [[0,2],
     [2,2],
     [2,2]],
     [[0,0]]*4,
     [[0,1]]*2
])

pattern = cycle((Path(__file__).parent / "input.txt").read_text().strip())
top = 3 # 3 units above floor

def can_move_left(h,l,r,space):
    if l == 0: return False
    for r_l, _ in r:
        if space[h][l+r_l-1]: return False
        h += 1
    return True

def can_move_right(h,l,r,space):
    for _, r_r in r:
        if l+r_r == 6: return False
        if space[h][l+r_r+1]: return False
        h += 1
    return True

def can_move_down(h,l,r,space):
    if h == 0: return False
    for r_l,r_r in r:
        if any(space[h-1][l+r_l:l+r_r+1]): return False
        h += 1
    return True

def try_push(left):
    if push == '<':
        if can_move_left(height,left,rock,space):
            left -= 1
            # print("moved left")
        else:
            # print("can't move left")
            ...
    elif push == '>':
        if can_move_right(height,left,rock,space):
            left += 1
            # print("moved right")
        else:
            # print("can't move right")
            ...
    return left

def is_in_rock(x,y,h,l,r):
    return h<=y< h+len(r) and l+r[y-h][0]<=x<=l+r[y-h][1]

def printout(rock=None,height=None,left=None):
    for y,row in enumerate(space[10::-1]):
        for x,v in enumerate(row):
            if v:
                print('#',end='')
            elif rock and is_in_rock(x,10-y,height,left,rock):
                print('@',end='')
            else:
                print('.',end='')
        print()
    print('-'*7)

space = [[0]*7 for _ in range(10000)]

for _ in range(2022):
    rock = next(rocks)
    height = top
    left = 2
    # sourcery skip
    for push in pattern:
        # printout(rock,height,left)
        left = try_push(left)

        if can_move_down(height,left,rock,space):
            height -= 1
            # print("moved down")
        else:
            # print("can't move down",height,left,rock)
            # print(height)
            top = max(top, height + len(rock) + 3)
            for r_l,r_r in rock:
                space[height][left+r_l:left+r_r+1] = [1]*(r_r-r_l+1)
                height += 1
            break
    # printout()
print(top-3)