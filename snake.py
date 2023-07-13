from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 13
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.ed_segment(position)


    def ed_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("pink")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def extend(self):
        self.ed_segment(self.segments[-1].position())



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            self.head.setheading(DOWN)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        else:
            self.head.setheading(RIGHT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
        else:
            self.head.setheading(LEFT)

