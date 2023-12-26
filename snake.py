from turtle import Turtle
import sys
import random


STARTING_POS: list[tuple] = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake(Turtle):

    def __init__(self, username: str):
        super().__init__()
        
        print(f"Created snake {username}")
        self.segments: list[Turtle] = []
        for pos in STARTING_POS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)
        self.head: Turtle = self.segments[0]
        self.head.setheading([LEFT, RIGHT, DOWN, RIGHT][random.randint(0, 4)])
        self.tail: Turtle = self.segments[len(self.segments) - 1]
        self.username: str = username
        self.counter = 0
        
        
    def increase(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        if self.tail.heading() == 0:
            new_segment.goto(self.tail.xcor() - 20, self.tail.ycor())
        elif self.tail.heading() == 90:
            new_segment.goto(self.tail.xcor(), self.tail.ycor() - 20)
        elif self.tail.heading() == 180:
            new_segment.goto(self.tail.xcor() + 20, self.tail.ycor())
        elif self.tail.heading() == 270:
            new_segment.goto(self.tail.xcor(), self.tail.ycor() + 20)
        self.segments.append(new_segment)
        self.counter += 1
    
    def get_counter(self):
        return self.counter

    def get_username(self, username):
        self.username = username

    def get_head(self):
        return self.head


    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].pos())
        self.detect_colision()
        self.detect_wall_colision()
        self.head.forward(MOVE_DISTANCE)


    def detect_colision(self):
        index = 0
        for seg in self.segments:
            if index < 2:
                index += 1
                continue
            if self.head.distance(seg) == 0:
                sys.exit()
                
    def detect_wall_colision(self):
        if self.get_head().xcor() > 280 or self.get_head().xcor() < -280:
            sys.exit()
        if self.get_head().ycor() > 280 or self.get_head().ycor() < -280:
            sys.exit()
            

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        