from turtle import Turtle
import random
from snake import Snake


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.objects: list[Snake] = []
        self.counter = 0
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    
    def subscribe(self, obj: Turtle):
        self.objects.append(obj)

    def listen(self):
        for obj in self.objects:
            if (obj.get_head().distance(self) < 15):
                self.counter += 1
                self.refresh()
                obj.increase()
                

    def refresh(self):
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        
    
