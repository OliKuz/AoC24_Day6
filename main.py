

# track the guiardian withturns 90 every time it reaches #


import time


def main():

    with open("input_xs.txt", 'r') as file:
        lines = file.readlines()

    map_grid = [list(line.strip()) for line in lines]

    show_grid(map_grid)

    # find the starting point
    for i in range(len(map_grid)):
        for j in range(len(map_grid[i])):
            if map_grid[i][j] == '^':
                start = (i, j)
                break

    print("Start: ", start)
    print()

    in_room = True  

    while in_room:
        direction = find_direction(map_grid, start)

        if direction == "up":

            # cover all of the up steps until we reach the #
            for i in range(start[0], -1, -1):
                if map_grid[i][start[1]] == "#":
                    map_grid[i+1][start[1]] = ">"
                    start = (i+1, start[1])
                    break
                map_grid[i][start[1]] = "X"
            
        elif direction == "down":
       
            for i in range(start[0], len(map_grid)):
                if map_grid[i][start[1]] == "#":
                    map_grid[i-1][start[1]] = "<"
                    start = (i-1, start[1])
                    break
                map_grid[i][start[1]] = "X"

        elif direction == "right":

            for i in range(start[1], len(map_grid[start[0]])):
                if map_grid[start[0]][i] == "#":
                    map_grid[start[0]][i-1] = "v"
                    start = (start[0], i-1)
                    break
                map_grid[start[0]][i] = "X"
        
        elif direction == "left":

            for i in range(start[1], -1, -1):
                if map_grid[start[0]][i] == "#":
                    map_grid[start[0]][i+1] = "^"
                    start = (start[0], i+1)
                    break
                map_grid[start[0]][i] = "X"
            
        elif direction == "gone":
            in_room = False

        print("start: ", start)
        show_grid(map_grid)
        # sleep for 1 second
        time.sleep(0.5)

    print("Guardian has left the room")

    # count all the Xs

    count = 0
    for i in range(len(map_grid)):
        for j in range(len(map_grid[i])):
            if map_grid[i][j] == "X":
                count += 1

    print("Total steps: ", count)





def find_direction(map_grid, pos):
    if map_grid[pos[0]][pos[1]] == '^':
        return "up"
    elif map_grid[pos[0]][pos[1]] == '>':
        return "right"
    elif map_grid[pos[0]][pos[1]] == 'v':
        return "down"
    elif map_grid[pos[0]][pos[1]] == '<':
        return "left"
    else:
        return "gone"

def show_grid(map_grid):
    print("    |[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]|")
    for i in range(len(map_grid)):
        print(f"[{i}]", map_grid[i])
    print()


if __name__ == "__main__":
    main()