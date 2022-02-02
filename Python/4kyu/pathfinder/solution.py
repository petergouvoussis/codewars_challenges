import re
def path_finder(maze):

    maze = re.split('\n', maze)
    maze = list(map(list, maze))

    #python indexing, not mathematical coordinates
    pos = [[0, 0]]
    finish = [len(maze) - 1, len(maze[0]) - 1]

    while pos:

        row, col = pos.pop()
        maze[row][col] = '0'

        if row < finish[0] and maze[row+1][col] == '.':
            pos.append([row + 1, col])

        if col < finish[1] and maze[row][col+1] == '.':
            pos.append([row, col + 1])

        if row > 0 and maze[row-1][col] == '.':
            pos.append([row - 1, col])

        if col > 0 and maze[row][col-1] == '.':
            pos.append([row, col - 1])

    return maze[finish[0]][finish[1]] == '0'
