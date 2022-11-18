"""Aca esta inportando la libreria turtle dandole parametros para donde inisializa la culebrita """
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
"""aca es como inportando se podria decir las para,etros para mover la culebrita mediante macros"""
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

"""Este metodo se estara viendo la creacion de la serpiente """
# este metodo se utliza para actulizar score mediante la culebra vaya colisionando con la comida 
"""esta es la clase snake"""
class Snake:
    # esta es la clave costructura que incializa las propiedades del meotodo, crea una tuppla que inciiliza el metodo create_snake 
    def __init__(self):
        self.segments = [] # la tupla cumple la funcion del segmento
        self.create_snake()
        self.head = self.segments[0]
        # con esta defnidad por el metodo __init__ simeopre inciara automaticamente 
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        # ya con el for que recorre la tupla definitida como starting_positions 
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        # la funcion extend esta diseñada para definir la posicion de los segmentos 
    def extend(self):
        
        self.add_segment(self.segments[-1].position())
        # la funcion move tine dentro de si un blucle for que recorre la tupla de los segmentos y les asigna una ocrdenada 
    def move(self):
        for seg_num in range(len(self.segments) 
- 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()

            new_y = self.segments[seg_num -1].ycor()

            self.segments[seg_num].goto(new_x,new_y)

        self.head.forward(MOVE_DISTANCE)
       # a continuacion se presentan 4 metodos que indican la tarea de los controles 
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
