import random
WALL = "▓" #wall
OPEN_SPACE = "◌" #free path
START = "S" #Start Point
END = "E" # endpoint
PATH = "o"

# Function to generate a random maze
def generate_maze(size, wall_percentage):
    maze = [[WALL if random.random() < wall_percentage else OPEN_SPACE for _ in range(size)] for _ in range(size)]
    maze[0][0] = START
    maze[size - 1][size - 1] = END
    return maze

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(" ".join(row))

def find_path(maze, x, y):
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] in [WALL, PATH]:
        return False

    if maze[x][y] == END:
        return True

    maze[x][y] = PATH

    if find_path(maze,x+1,y ) or find_path(maze,x, y+1 ) or find_path(maze,x,y-1) or find_path(maze, x-1, y):
        return True

    maze[x][y] = OPEN_SPACE
    return False

# Function to mark the path in the maze
def mark_path(maze):
    if not find_path(maze, 0, 0):
        print("No path found")

# Main function
def main():
    print("Terminal-Based Maze Solver")
    size = int(input("Enter the size of the maze (n x n): "))
    wall_percentage = 0.3
    maze = generate_maze(size, wall_percentage)

    while True:
        print("Generated Maze:")
        print_maze(maze)

        print("\n1. Print the path")
        print("2. Generate another puzzle")
        print("3. Exit the Game")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            mark_path(maze)
            print("Maze with Path:")
            print_maze(maze)
        elif choice == "2":
            maze = generate_maze(size, wall_percentage)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
