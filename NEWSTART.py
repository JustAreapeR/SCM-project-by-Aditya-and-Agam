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

    def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return 1
