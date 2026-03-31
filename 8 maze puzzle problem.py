from queue import PriorityQueue

goalstate = [[1,2,3],
              [4,5,6],
              [7,8,0]]

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def findblank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                x = (value - 1) // 3
                y = (value - 1) % 3
                distance += abs(i - x) + abs(j - y)
    return distance

# Convert to tuple
def totuple(state):
    return tuple(tuple(row) for row in state)

def print_stack(state):
    for row in state:
        print(row)
    print()

def solvable(state):
    flat = [num for row in state for num in row if num != 0]
    inversions = 0
    for i in range(len(flat)):
        for j in range(i+1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
    return inversions % 2 == 0

# A* Solver
def solvepuzzle(start):
    pq = PriorityQueue()
    pq.put((0, start, 0, []))  # (f, state, g, path)
    
    visited = set()
    
    while not pq.empty():
        f, state, g, path = pq.get()
        
        if state == goalstate:
            print("Solution Found!")
            print("Steps:", g)
            print("\nPath:\n")
            for step in path + [state]:
                print_stack(step)
            return
        
        visited.add(totuple(state))
        
        x, y = findblank(state)
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                
                if totuple(new_state) not in visited:
                    h = heuristic(new_state)
                    pq.put((g + 1 + h, new_state, g + 1, path + [state]))

    print("No solution found")

# TAKE INPUT FROM USER
print("Enter the 8-puzzle (use 0 for blank):")

start_state = []
for i in range(3):
    row = list(map(int, input(f"Enter row {i+1} (space separated): ").split()))
    start_state.append(row)

print("\nInitial State:")
print_stack(start_state)

# Check solvability
if solvable(start_state):
    solvepuzzle(start_state)
else:
    print("This puzzle is NOT SOLVABLE")
