import tkinter as tk
import random

class SnakeGame(tk.Canvas):
    def __init__(self, master, width=400, height=400, block=20):
        super().__init__(master, width=width, height=height, bg="black", highlightthickness=0)
        self.block = block
        self.width = width
        self.height = height
        self.snake = [(width // 2, height // 2)]
        self.direction = "Right"
        self.apple = None
        self.spawn_apple()
        self.bind_all("<Key>", self.on_key)
        self.after_id = None
        self.running = True
        self.draw()
        self.tick()

    def spawn_apple(self):
        while True:
            x = random.randrange(0, self.width, self.block)
            y = random.randrange(0, self.height, self.block)
            if (x, y) not in self.snake:
                self.apple = (x, y)
                break

    def on_key(self, event):
        key = event.keysym
        if key in ("Up", "Down", "Left", "Right"):
            opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if key != opposites.get(self.direction):
                self.direction = key

    def tick(self):
        if not self.running:
            return
        head_x, head_y = self.snake[0]
        delta = {
            "Up": (0, -self.block),
            "Down": (0, self.block),
            "Left": (-self.block, 0),
            "Right": (self.block, 0),
        }
        dx, dy = delta[self.direction]
        new_head = ((head_x + dx) % self.width, (head_y + dy) % self.height)
        if new_head in self.snake:
            self.running = False
            return
        self.snake = [new_head] + self.snake
        if new_head == self.apple:
            self.spawn_apple()
        else:
            self.snake.pop()
        self.draw()
        self.after_id = self.after(100, self.tick)

    def draw(self):
        self.delete("all")
        for (x, y) in self.snake:
            self.create_rectangle(x, y, x + self.block, y + self.block, fill="green")
        ax, ay = self.apple
        self.create_oval(ax, ay, ax + self.block, ay + self.block, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Snake")
    game = SnakeGame(root)
    game.pack()
    root.mainloop()
