"""path in array
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(target, arr, visited, x, y):
    if not target:
        return True
    
    if x < 0 or x >= len(arr) or \
            y < 0 or y >= len(arr[0]) or \
                visited[x][y] == True:
                return False
    if target[0] != arr[x][y]:
        return False
    visited[x][y] = True

    for i in range(0,4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if solution(target[1:], arr, visited, next_x, next_y):
            return True
    visited[x][y] = False
    return False
    


if __name__ == "__main__":
    arr = [list('abtg'), list('cfcs'), list('jdeh')]
    visited = [[False for i in range(len(arr[0]))] for j in range(len(arr))]
    target = 'tcfdeh'
    for k1, v1 in enumerate(arr):
        for k2, v2 in enumerate(v1):
            if solution(target, arr, visited, k1, k2):
                print("find one!!!!!!!!!!!, index is {}{}".format(k1, k2))
"""


