import curses
import random

# Initialize screen
screen = curses.initscr()
curses.curs_set(0)
height, width = screen.getmaxyx()
win = curses.newwin(height, width, 0, 0)
win.keypad(1)
win.timeout(100)

# Initial snake position and food placement
snk_x = width//4
snk_y = height//2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]
food = [random.randint(1, height-2), random.randint(1, width-2)]
win.addch(food[0], food[1], curses.ACS_PI)

# Initial movement direction
key = curses.KEY_RIGHT

while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    # Calculate new head of the snake
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    elif key == curses.KEY_UP:
        y -= 1
    elif key == curses.KEY_LEFT:
        x -= 1
    elif key == curses.KEY_RIGHT:
        x += 1
    new_head = [y, x]

    # Check for collisions
    if y in [0, height] or x in [0, width] or new_head in snake:
        curses.endwin()
        quit()

    snake.insert(0, new_head)

    # Check if food is eaten
    if snake[0] == food:
        food = None
        while food is None:
            nf = [random.randint(1, height-2), random.randint(1, width-2)]
            food = nf if nf not in snake else None
        win.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    win.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

