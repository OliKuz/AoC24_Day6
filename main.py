

# track the guiardian withturns 90 every time it reaches #

# task 2 --> trap guardian in  aloop by placing 1 O "Obstacle" in the room


import time
from copy import deepcopy


def main():

    with open("input_xs.txt", 'r') as file:
        lines = file.readlines()

    map_grid = [list(line.strip()) for line in lines]

    show_grid(map_grid)
    initial_grid = deepcopy(map_grid)

    # find the starting point
    for i in range(len(map_grid)):
        for j in range(len(map_grid[i])):
            if map_grid[i][j] == '^':
                start = (i, j)
                break

    print("Start: ", start)
    print()
    initial_start = start

    visited = []
    track_guardian(map_grid, start, visited)

    # count all the Xs
    count = 0
    for i in range(len(map_grid)):
        for j in range(len(map_grid[i])):
            if map_grid[i][j] == "X":
                count += 1

    print("Total steps: ", count)

    trap_guardian(initial_grid, initial_start, visited)



def trap_guardian(map, start, visited):

    # find the points where the guardian can be trapped by checking positions he revisted

    revisted = []
    for i in range(len(visited)):
        if visited.count(visited[i]) > 1 and visited[i] != start:
            if visited[i] not in revisted:
                revisted.append(visited[i])

    count = 0;

    # add every possible position
    positions = []
    for i in range (len(map)):
        for j in range(len(map[i])):
            if map[i][j] != "#":
                positions.append((i, j))
    

    for i in range(len(positions)):
        
        with open("input_xs.txt", 'r') as file:
            lines = file.readlines()

        map = [list(line.strip()) for line in lines]

        map[positions[i][0]][positions[i][1]] = "O"
        if test_O(map, start):
            count += 1


    #  do the same loop but for every map position


    # go through every position in the map and if it is not a # try out the test_O function

    print("Total traps: ", count)

   

def test_O(map_grid, start):
    visited = []


    while True:
        direction = find_direction(map_grid, start)

        if direction == "up":
            for i in range(start[0], -1, -1):
                if map_grid[i][start[1]] == "#" or map_grid[i][start[1]] == "O":
                    map_grid[i+1][start[1]] = ">"
                    start = (i+1, start[1])
                    break
                visited.append((i, start[1]))
                map_grid[i][start[1]] = "X"

        elif direction == "down":
            for i in range(start[0], len(map_grid)):
                if map_grid[i][start[1]] == "#" or map_grid[i][start[1]] == "O":
                    map_grid[i-1][start[1]] = "<"
                    start = (i-1, start[1])
                    break
                visited.append((i, start[1]))
                map_grid[i][start[1]] = "X"

        elif direction == "right":
            for i in range(start[1], len(map_grid[start[0]])):
                if map_grid[start[0]][i] == "#" or map_grid[start[0]][i] == "O": 
                    map_grid[start[0]][i-1] = "v"
                    start = (start[0], i-1)
                    break
                visited.append((start[0], i))
                map_grid[start[0]][i] = "X"

        elif direction == "left":
            for i in range(start[1], -1, -1):
                if map_grid[start[0]][i] == "#" or map_grid[start[0]][i] == "O":
                    map_grid[start[0]][i+1] = "^"
                    start = (start[0], i+1)
                    break
                visited.append((start[0], i))
                map_grid[start[0]][i] = "X"

        elif direction == "gone":
            print("Guardian has left the room")
            return False

    # if at some point visited has been coming back to same point throught the same journey return true
        for k in range(len(visited)):
            if visited.count(visited[k]) > 10 and visited[k] != start:
                show_grid(map_grid)
                return True
        
    

    

def track_guardian(map_grid, start, visited):
    in_room = True  

    while in_room:
        direction = find_direction(map_grid, start)

        if direction == "up":
            for i in range(start[0], -1, -1):
                if map_grid[i][start[1]] == "#":
                    map_grid[i+1][start[1]] = ">"
                    start = (i+1, start[1])
                    break
                visited.append((i, start[1]))
                map_grid[i][start[1]] = "X"

        elif direction == "down":
            for i in range(start[0], len(map_grid)):
                if map_grid[i][start[1]] == "#":
                    map_grid[i-1][start[1]] = "<"
                    start = (i-1, start[1])
                    break
                visited.append((i, start[1]))
                map_grid[i][start[1]] = "X"

        elif direction == "right":
            for i in range(start[1], len(map_grid[start[0]])):
                if map_grid[start[0]][i] == "#":
                    map_grid[start[0]][i-1] = "v"
                    start = (start[0], i-1)
                    break
                visited.append((start[0], i))
                map_grid[start[0]][i] = "X"

        elif direction == "left":
            for i in range(start[1], -1, -1):
                if map_grid[start[0]][i] == "#":
                    map_grid[start[0]][i+1] = "^"
                    start = (start[0], i+1)
                    break
                visited.append((start[0], i))
                map_grid[start[0]][i] = "X"

        elif direction == "gone":
            print("Guardian has left the room")
            in_room = False

        # show_grid(map_grid)


        # print("start: ", start)
        # show_grid(map_grid)
        # # sleep for 1 second
        # time.sleep(0.5)


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