#board creation
def print_Board(Player_1, Player_2):
    zero = 'X' if Player_1[0] else ('O' if Player_2[0] else 0)
    one = 'X' if Player_1[1] else ('O' if Player_2[1] else 1)
    two = 'X' if Player_1[2] else ('O' if Player_2[2] else 2)
    three = 'X' if Player_1[3] else ('O' if Player_2[3] else 3)
    four = 'X' if Player_1[4] else ('O' if Player_2[4] else 4)
    five = 'X' if Player_1[5] else ('O' if Player_2[5] else 5)
    six = 'X' if Player_1[6] else ('O' if Player_2[6] else 6)
    seven = 'X' if Player_1[7] else ('O' if Player_2[7] else 7)
    eight = 'X' if Player_1[8] else ('O' if Player_2[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")

#conditions for wining
def sum(x, y, z):
    return x + y + z

def check_for_Win(Player_1, Player_2):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(Player_1[win[0]], Player_1[win[1]], Player_1[win[2]]) == 3):
            print("P1 WINS")
            return 1 #1 for p1 and 0 for p2
        if(sum(Player_2[win[0]], Player_2[win[1]], Player_2[win[2]]) == 3):
            print("P2 WINS")
            return 0
    return - 1

#main code
Player_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
Player_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1 # 1 for X and 0 for O
while(True):
    print_Board(Player_1, Player_2)
    if(turn == 1):
        print("P1's Turn")
        a = int(input("ENTER POSITION: "))
        Player_1[a] = 1
    else:
        print("P2's Turn")
        b = int(input("ENTER POSITION: "))
        Player_2[b] = 1
    winner = check_for_Win(Player_1, Player_2)
    if(winner != -1):
        break
        
    turn = 1 - turn
