Python Tkinter Snake Game

Project Description

This project is a classic Snake game implemented in Python using the Tkinter library. The game provides a graphical user interface where the player controls a snake to move around the board, eat food, grow in length, and avoid collisions.

The snake moves continuously at a fixed speed. The player controls its direction using the keyboard. Food appears randomly on the game board, and the snake grows after eating food. The goal is to eat as much food as possible and reach a higher score before the game ends.

This version includes two types of food, different length increases, collision detection, score tracking, maximum length limitation, and a game-over display.

Features

Snake Movement

The snake moves continuously on the game board at a fixed speed.

The player can control the snake’s direction using the keyboard:

* Up
* Down
* Left
* Right

The snake keeps moving in the current direction until the player changes it.

Food Generation

Food items appear randomly on the game board.

When the snake eats a food item:

* The snake grows longer
* The score increases
* A new food item appears at another random location

The food will be displayed in a different color from the snake and the background so that the player can easily identify it.

Two Types of Food

The game includes two different types of food.

Each food type increases the snake’s length by a different amount:

* Type 1 food: increases the snake length by 1 unit
* Type 2 food: increases the snake length by 2 units

This adds more variety to the gameplay and affects how quickly the snake reaches its maximum length.

Score and Length Tracking

The game tracks the player’s score based on the food eaten by the snake.

The game also tracks the current length of the snake.

The snake can grow until it reaches the maximum length.

Maximum Length Limit

The maximum length of the snake is 8 units.

The game ends when the snake reaches this maximum length.

Collision Detection

The game ends when one of the following conditions occurs:

1. The snake collides with the boundary of the game area.
2. The snake collides with its own body.
3. The snake reaches the maximum length of 8 units.

Tkinter Graphical User Interface

The game interface is implemented using Python Tkinter.

The Tkinter Canvas component is used to draw game elements, including:

* Game board
* Snake
* Food
* Background

The snake, food, and background use different colors to make the interface clear and easy to understand.

Game Over Message

When the game ends, a game-over message is displayed.

The message includes:

* Final length of the snake
* Total game time in seconds
* Final score

Example:

Game Over
Final Length: 8
Total Time: 35 seconds
Score: 6

Direct Keyboard Control

The game supports direct keyboard control.

The player can use keyboard events to control the snake’s direction.

Example controls:

Up Arrow    - Move Up
Down Arrow  - Move Down
Left Arrow  - Move Left
Right Arrow - Move Right

The control system prevents invalid direction changes when necessary, such as immediately reversing into the snake’s own body.

Technologies Used

* Python
* Tkinter
* Canvas Drawing
* Keyboard Event Handling
* Random Food Generation
* Game Loop Logic

Project Structure

project-folder/
│
├── main.py
├── snake.py
├── food.py
├── game.py
└── README.md

File descriptions:

* main.py: Starts the game application.
* game.py: Manages the main game loop, GUI updates, timer, score, and game-over logic.
* snake.py: Defines the snake’s movement, growth, and collision behavior.
* food.py: Handles food generation and food type logic.

The actual file names may vary depending on the implementation.

How to Run

1. Install Python

Make sure Python is installed on your computer.

Check the Python version:

python --version

or:

python3 --version

2. Check Tkinter

Tkinter is usually included with standard Python installations.

You can check whether Tkinter is available by running:

python -m tkinter

or:

python3 -m tkinter

If a small Tkinter window appears, Tkinter is installed correctly.

3. Run the Game

Open a terminal in the project directory and run:

python main.py

or:

python3 main.py

If your main file has a different name, replace main.py with the correct file name.

How to Play

1. Start the game.
2. Use the arrow keys to control the snake.
3. Move the snake toward food items.
4. Eat food to increase the snake’s length and score.
5. Avoid hitting the walls.
6. Avoid hitting the snake’s own body.
7. Try to reach the maximum length of 8 units.

Game Rules

The basic game rules are:

* The snake moves forward continuously.
* The player controls the snake’s direction using the keyboard.
* Food appears randomly on the board.
* Eating food increases the snake’s length.
* Different food types increase the snake’s length by different amounts.
* The game ends when the snake hits the wall.
* The game ends when the snake hits itself.
* The game ends when the snake reaches the maximum length of 8 units.

Example Gameplay Flow

Game starts.
Snake length: 1
Score: 0
Snake eats Type 1 food.
Snake length: 2
Score increases.
Snake eats Type 2 food.
Snake length: 4
Score increases.
Snake continues moving.
Snake reaches length 8.
Game Over.

Core Game Logic

The game uses a grid-based board.

The snake is represented as a list of body segments. Each segment has a position on the board.

Example:

[(5, 5), (5, 4), (5, 3)]

The first position represents the snake’s head, and the remaining positions represent its body.

At each game update:

1. A new head position is calculated based on the current direction.
2. The program checks whether the new head position causes a collision.
3. If there is no collision, the snake moves forward.
4. If the snake eats food, its length increases.
5. A new food item is generated at a random empty position.
6. The canvas is updated to display the new game state.

Food Logic

There are two types of food in the game.

Example:

Food Type 1: length +1
Food Type 2: length +2

When food is generated, the program randomly selects a food type and places it at an empty location on the board.

Food should not appear on the snake’s body.

Game Over Conditions

The game ends when any of the following conditions is met:

1. Wall Collision

The snake moves outside the game board.

Example:

The snake moves beyond the left, right, top, or bottom boundary.

2. Self Collision

The snake’s head moves into its own body.

Example:

The snake runs into one of its body segments.

3. Maximum Length Reached

The snake reaches the maximum length of 8 units.

Example:

Current Length: 8
Game Over

Keyboard Controls

Arrow Up    - Move Up
Arrow Down  - Move Down
Arrow Left  - Move Left
Arrow Right - Move Right

Alternative controls may also be supported:

W - Move Up
S - Move Down
A - Move Left
D - Move Right

Possible Improvements

Possible future improvements include:

* Different difficulty levels
* Adjustable snake speed
* More food types
* Obstacles on the board
* Pause and resume function
* Restart button
* Sound effects
* High score record
* More advanced visual design
