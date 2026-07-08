import tkinter as tk
import random
import time


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Snake Game")

        # Basic game settings
        self.CELL_SIZE = 30
        self.COLS = 20
        self.ROWS = 20
        self.WIDTH = self.COLS * self.CELL_SIZE
        self.HEIGHT = self.ROWS * self.CELL_SIZE

        self.SPEED = 150  # milliseconds
        self.MAX_LENGTH = 8

        # Colors
        self.BG_COLOR = "black"
        self.SNAKE_COLOR = "lime green"
        self.SNAKE_HEAD_COLOR = "green yellow"
        self.FOOD_1_COLOR = "red"      # grow by 1
        self.FOOD_2_COLOR = "orange"   # grow by 2
        self.TEXT_COLOR = "white"

        # GUI components
        self.info_label = tk.Label(
            root,
            text="Score: 0 | Length: 3",
            font=("Arial", 14),
            bg="gray20",
            fg="white"
        )
        self.info_label.pack(fill=tk.X)

        self.canvas = tk.Canvas(
            root,
            width=self.WIDTH,
            height=self.HEIGHT,
            bg=self.BG_COLOR
        )
        self.canvas.pack()
        self.canvas.focus_set()

        # Keyboard control
        self.root.bind("<Up>", self.change_direction)
        self.root.bind("<Down>", self.change_direction)
        self.root.bind("<Left>", self.change_direction)
        self.root.bind("<Right>", self.change_direction)

        self.reset_game()

    def reset_game(self):
        """Initialize or reset the game state."""

        self.snake = [
            (5, 10),
            (4, 10),
            (3, 10)
        ]

        self.direction = "Right"
        self.next_direction = "Right"

        self.score = 0
        self.pending_growth = 0
        self.game_over = False
        self.start_time = time.time()

        self.food = None
        self.food_type = None
        self.create_food()

        self.draw_game()
        self.move_snake()

    def create_food(self):
        """
        Randomly generate food.
        Type 1: snake length increases by 1.
        Type 2: snake length increases by 2.
        """

        empty_cells = []

        for x in range(self.COLS):
            for y in range(self.ROWS):
                if (x, y) not in self.snake:
                    empty_cells.append((x, y))

        if not empty_cells:
            return

        self.food = random.choice(empty_cells)
        self.food_type = random.choice([1, 2])

    def change_direction(self, event):
        """Change snake direction by arrow keys."""

        key = event.keysym

        # Prevent direct reverse movement
        if key == "Up" and self.direction != "Down":
            self.next_direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.next_direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.next_direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.next_direction = "Right"

    def move_snake(self):
        """Main game loop."""

        if self.game_over:
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        else:
            new_head = (head_x + 1, head_y)

        # Game over condition 1: hit wall
        if self.hit_wall(new_head):
            self.end_game("The snake hit the wall!")
            return

        # Game over condition 2: hit itself
        if new_head in self.snake:
            self.end_game("The snake hit itself!")
            return

        # Move snake by adding the new head
        self.snake.insert(0, new_head)

        # Check whether the snake eats food
        if new_head == self.food:
            grow_units = self.food_type
            self.score += grow_units

            # The new head already increases the length by 1.
            # If the food gives 2 units, one extra unit will be kept in the next move.
            self.pending_growth += grow_units - 1

            self.create_food()
        else:
            # If there is pending growth, keep the tail for this move.
            # Otherwise, remove the tail as normal movement.
            if self.pending_growth > 0:
                self.pending_growth -= 1
            else:
                self.snake.pop()

        # Game over condition 3: reach maximum length
        if len(self.snake) >= self.MAX_LENGTH:
            self.snake = self.snake[:self.MAX_LENGTH]
            self.end_game("The snake reached the maximum length!")
            return

        self.draw_game()
        self.root.after(self.SPEED, self.move_snake)

    def hit_wall(self, position):
        """Check whether the snake hits the boundary."""

        x, y = position
        return x < 0 or x >= self.COLS or y < 0 or y >= self.ROWS

    def draw_game(self):
        """Draw snake, food, and information."""

        self.canvas.delete("all")

        # Draw food
        food_x, food_y = self.food
        food_color = self.FOOD_1_COLOR if self.food_type == 1 else self.FOOD_2_COLOR

        self.canvas.create_oval(
            food_x * self.CELL_SIZE + 5,
            food_y * self.CELL_SIZE + 5,
            (food_x + 1) * self.CELL_SIZE - 5,
            (food_y + 1) * self.CELL_SIZE - 5,
            fill=food_color
        )

        # Draw snake
        for index, (x, y) in enumerate(self.snake):
            color = self.SNAKE_HEAD_COLOR if index == 0 else self.SNAKE_COLOR

            self.canvas.create_rectangle(
                x * self.CELL_SIZE,
                y * self.CELL_SIZE,
                (x + 1) * self.CELL_SIZE,
                (y + 1) * self.CELL_SIZE,
                fill=color,
                outline="dark green"
            )

        self.info_label.config(
            text=f"Score: {self.score} | Length: {len(self.snake)}"
        )

    def end_game(self, reason):
        """End the game and display game over message."""

        self.game_over = True
        total_time = int(time.time() - self.start_time)

        self.info_label.config(
            text=f"Score: {self.score} | Length: {len(self.snake)}"
        )

        self.canvas.delete("all")

        message = (
            "Game Over\n\n"
            f"Reason: {reason}\n"
            f"Current Length: {len(self.snake)}\n"
            f"Score: {self.score}\n"
            f"Total Game Time: {total_time} seconds\n\n"
            "Press R to restart or ESC to exit."
        )

        self.canvas.create_text(
            self.WIDTH / 2,
            self.HEIGHT / 2,
            text=message,
            fill=self.TEXT_COLOR,
            font=("Arial", 18),
            justify="center"
        )

        self.root.bind("r", self.restart)
        self.root.bind("R", self.restart)
        self.root.bind("<Escape>", self.exit_game)

    def restart(self, event):
        """Restart the game."""

        self.root.unbind("r")
        self.root.unbind("R")
        self.root.unbind("<Escape>")
        self.reset_game()

    def exit_game(self, event):
        """Exit the game."""

        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()