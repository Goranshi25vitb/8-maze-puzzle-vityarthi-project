# 8-maze-puzzle-vityarthi-project
This is a puzzle solver which uses different approaches like A* search which is an informed search technique that combines actual cost and estimated cost to reach the goal state. We provide the initial state that consist of 8 numbered tiles and one empty space (represented bu a 0) after providing the initial state the solvability of the problem will be checked and if it is solvable the code will transform it in the predefined goal state with the minimum number of moves.

The algorithm begins by taking an initial puzzle configuration from the user. It first checks whether the puzzle is solvable using inversion count logic.

If the puzzle is solvable, the A* algorithm is applied. The algorithm evaluates each possible move and selects the best one based on the function:f(n)=g(n)+h(n)
 
 where, 
      
      g(n) = cost from start node to current node
     
      h(n) = estimated cost to reach the goal state

this process cstops when the goal state is reached.


Concepts used:

1.A* Search Algorithm

2.Heuristic Function (Manhattan Distance)

3.State Space Representation

4.Inversion Count (Solvability Check)


Project Location

8-puzzle-project-vityarthi-project
│
├── 8 maze puzzle problem.py
└── README.md

1.Setup Instructions (Step-by-Step)

Step 1: Install Python
Go to:
https://www.python.org/downloads/
Download Python (version 3.7 or higher)
Run the installer

Click Install Now

Step 2: Verify Installation

Open Command Prompt (Windows) or Terminal (Mac/Linux)

Type:

python --version

If installed correctly, you will see:

Python 3.x.x

Step 3: Create Project Folder

Create a folder:

8 maze puzzle problem

Step 4: Add Code File
Open any editor (eg. VS Code)

Paste your Python code
Save file as:
8 maze puzzle

take care of

File extension is .py
NOT .txt

Step 5: Open Terminal in Folder
Windows:
Open folder

Click address bar → type cmd → press Enter
Mac/Linux:

Right click → “Open Terminal”

2. Dependencies Installation:

 No external dependencies required

This project uses only built-in Python modules:

queue (PriorityQueue)

No need to install anything

3. Configuration Steps

This project works without any configuration, but you can customize:

🔹 Change Goal State 

Default:

goalstate = [[1,2,3],
              [4,5,6],
              [7,8,0]]

You can modify if required.

🔹 Set Fixed Input

Instead of typing input every time:

start_state = [[1,2,3],
               [4,0,6],
               [7,5,8]]
🔹 Change Heuristic 

Default: Manhattan Distance

You can modify the heuristic function if needed.

4. Execution Steps

Step 1: Run Program

In terminal:

python 8_puzzle.py

Step 2: Enter Input

You will be asked to enter row values:

Example:

Enter row 1: 1 2 3
Enter row 2: 4 0 6
Enter row 3: 7 5 8

it's mandotory to use space between numbers 
using 0 as a blank space

Step 3: View Output

The program will:

Check if puzzle is solvable

Show number of steps

Display step-by-step solution

Working Steps:

1.Start with the initial state.

2.Generate all possible moves.

3.Calculate f(n) for each state.

4.Select the state with the lowest f(n).

5.Repeat until the goal state is reached.

Example 

Input:
1 2 3
4 0 6
7 5 8

Output:
Solution Found!


[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

[1, 2, 3]
[4, 5, 6]
[7, 8, 0]





