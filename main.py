from msvcrt import getch
from turtle import Turtle, Screen
import time
import sys
from config import BG_COLOR, HEIGHT, TITLE, WIDTH
from scoreboards import Scoreboard
from snake import Snake
from food import Food


class GameIsOn:
    
    def __init__(self):
        self.game_is_on = False

    def start_game(self):
        self.game_is_on = True
        
    def get_game_status(self):
        return self.game_is_on



if __name__ == "__main__":
    ammount_of_players = input("How many players? (1 or 2)  ") 
    if ammount_of_players not in ["1", "2"]:
        print("Error, you should select 1 or 2")
        sys.exit()
    
    snakes: list[Snake] = []
    
    for i in range(int(ammount_of_players)):
        while 1:
            username = input(f"Player {i} username: ")
            if len(username) < 1:
                continue
            snakes.append(Snake(username))
            break
        

    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)

    screen.bgcolor(BG_COLOR)
    screen.title(TITLE)
    screen.tracer(0)

    
    food: Food = Food()
    
    for snake in snakes:
        food.subscribe(snake)
    
    screen.listen()

    keys_list = [["Up", "Down", "Left", "Right"], ["w", "s", "a", "d"]]

    for index, snake in enumerate(snakes):
        keys = keys_list[index]
        print(keys)
        screen.onkey(snake.up, keys[0])
        screen.onkey(snake.down, keys[1])
        screen.onkey(snake.left, keys[2])
        screen.onkey(snake.right, keys[3])
    
    
    game = GameIsOn()

    screen.onkey(game.start_game, "Return")


    scoreboard = Scoreboard(snakes)
    screen.update()

    while not game.game_is_on: 
        screen.update()
        time.sleep(0.1)
    
    while 1:
        screen.update()
        time.sleep(0.1)
        food.listen()
        for snake in snakes:
            snake.move()
            snake.detect_wall_colision()
        scoreboard.write()




screen.exitonclick()



