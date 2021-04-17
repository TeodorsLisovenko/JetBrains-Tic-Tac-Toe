 numeric_Matrix = [[1, 1, "_"], [1, 2, "_"], [1, 3, "_"],
                  [2, 1, "_"], [2, 2, "_"], [2, 3, "_"],
                  [3, 1, "_"], [3, 2, "_"], [3, 3, "_"]]


def visualization():
    print("---------")
    print(" ".join("|" + numeric_Matrix[0][2] + numeric_Matrix[1][2] + numeric_Matrix[2][2] + "|"))
    print(" ".join("|" + numeric_Matrix[3][2] + numeric_Matrix[4][2] + numeric_Matrix[5][2] + "|"))
    print(" ".join("|" + numeric_Matrix[6][2] + numeric_Matrix[7][2] + numeric_Matrix[8][2] + "|"))
    print("---------")


visualization()

game_is_running = True


def rules():
    global game_is_running

    rows_horizontal = [[numeric_Matrix[0][2] + numeric_Matrix[1][2] + numeric_Matrix[2][2]],
                       [numeric_Matrix[3][2] + numeric_Matrix[4][2] + numeric_Matrix[5][2]],
                       [numeric_Matrix[6][2] + numeric_Matrix[7][2] + numeric_Matrix[8][2]]]

    rows_vertical = [[numeric_Matrix[0][2] + numeric_Matrix[3][2] + numeric_Matrix[6][2]],
                     [numeric_Matrix[1][2] + numeric_Matrix[4][2] + numeric_Matrix[7][2]],
                     [numeric_Matrix[2][2] + numeric_Matrix[5][2] + numeric_Matrix[8][2]]]

    rows_diagonals = [[numeric_Matrix[0][2] + numeric_Matrix[4][2] + numeric_Matrix[8][2]],
                      [numeric_Matrix[2][2] + numeric_Matrix[4][2] + numeric_Matrix[6][2]]]

    rows_directions = [rows_horizontal, rows_vertical, rows_diagonals]

    chars = ["X", "O"]
    have_X_won = False
    have_O_won = False

    # Checking in every direction

    for char in chars:
        for direction in rows_directions:
            for row in direction:
                if row[0][0] == row[0][1] == row[0][2] == char:
                    if char == "X":
                        have_X_won = True
                    if char == "O":
                        have_O_won = True

    # Endgame

    if have_X_won is True and have_O_won is True:
        print("Impossible")
        game_is_running = False
    elif have_X_won is True and have_O_won is False:
        print("X wins")
        game_is_running = False
    elif have_X_won is False and have_O_won is True:
        print("O wins")
        game_is_running = False
    else:
        leftover = [char[2] for char in numeric_Matrix]
        if "_" not in leftover:
            print("Draw")
            game_is_running = False


x_turn = True

while game_is_running:
    coord_one, coord_two = input("Enter the coordinates: ").split()

    x = int(coord_one)
    y = int(coord_two)

    if not isinstance(x, int) and not isinstance(y, int):
        print("You should enter numbers")
    elif x not in range(0, 4) or y not in range(0, 4):
        print("Coordinates should be from 1 to 3!")
    else:
        for section in numeric_Matrix:
            if section[0] == x and section[1] == y and (section[2] == "X" or section[2] == "O"):
                print("This cell is occupied! Choose another one!")
            elif section[0] == x and section[1] == y:
                if x_turn:
                    section[2] = "X"
                    x_turn = False
                    visualization()
                    rules()
                else:
                    section[2] = "O"
                    x_turn = True
                    visualization()
                    rules()
