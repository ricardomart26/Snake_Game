from turtle import Turtle
from config import WIDTH

from snake import Snake

class Scoreboard:
    
    
    
    def __init__(self, snakes: list[Snake]):
        self.snakes: list[Snake] = snakes
        self.scoreboards_list: list[Turtle] = []
        cords = []
        if len(snakes) == 1:
            cords = [(0, 250)]
        elif len(snakes) == 2:
            cords = [(-(WIDTH / 2) + 100, 250), ((WIDTH / 2) - 100, 250)]
        
        for index, snake in enumerate(snakes):
            score = self.create_scoreboard()
            self.scoreboards_list.append(score)
            score.goto(cords[index])
            
        pass
    
    
    def create_scoreboard(self):
        scoreboard = Turtle()
        scoreboard.color("white")
        scoreboard.hideturtle()
        scoreboard.penup()
        return scoreboard
    
    
    def write(self):
        for index, scoreboard in enumerate(self.scoreboards_list):
            scoreboard.clear()
            scoreboard.write(f"Score {self.snakes[index].username} : {self.snakes[index].counter}", align="center", font=("Arial", 18, "normal"))
