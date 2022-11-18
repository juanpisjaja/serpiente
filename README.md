#  APLICACON DE SNAKE
## food
>"""Inportando la libreria turtle y random que contiene una serie de funciones relacionadas con los valores aleatorios"""
from turtle import Turtle
import random

"""Al declarar ña la clase food y utlizando turtle esta haciendo una especie de dibujo que va a simular la comida entonces le esta diciendo que va ser circular de color azul ayudandonse a devolver el vector de la comida para que cuelva a parecer """
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,

stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
### Le esta diciendo que aparesca aleatoriamente en eje x y y no saliendose de los parametros de 200 y - 200 para que no se salga de la interfaz grafica 
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
## main
>"""En las lineas 2-6 esta inportando dos librerias 
1.Turtle que sirve para dibujar figuras intrincadas usando programas que repiten movimientos simples. Al combinar estos comandos y otros similares, se pueden dibujar figuras intrincadas y formas. 
3. La biblioteca time contiene una serie de funciones relacionadas con la medición del tiempo.
ademas d ela dos libreias contiene 3 archvios punto py donde se organiza el codigo por secciones como lo es un para la serpiente otro para los puntos otro para la pantalla"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
"""En esta parte del codigo esta poniendo el tamaña y color a la interfaz grafica y ponioendole un nombre a esa interfaz """ 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

"""crea los nombres de los objetos que van dentro de la interfaz"""
snake = Snake()
food = Food()
scoreboard = Scoreboard()

"""declara las teclas para mover la serpiente en la interfaz haciendolo por  medio de la funcion macro(onkey)"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

"""esta haciendo una funcion ayudando a definir la velocidad de la serpiente"""
game_is_on = True
while game_is_on:
    screen.update()

    time.sleep(0.1)
    snake.move()

### Esta definiendo la distacia para que detecte la colicion con el alimento
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

### Esta definiendo la distacia para que detecte la colicion con Lla pared
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

### Esta definiendo la distacia para que detecte la colicion con el mismo
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
### Esto sirve para que la interfaz no se cierre antes de que inicie el juego 
screen.exitonclick()


## snake
>"""Aca esta inportando la libreria turtle dandole parametros para donde inisializa la culebrita """
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
"""aca es como inportando se podria decir las para,etros para mover la culebrita mediante macros"""
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

"""Este metodo se estara viendo la creacion de la serpiente """
### este metodo se utliza para actulizar score mediante la culebra vaya colisionando con la comida 
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
       ### a continuacion se presentan 4 metodos que indican la tarea de los controles 
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


## scoreboard
>"""En esta seccion del codigo estamos trabajando con el score o puntos del juego inportando la libreria turtle y aliniando el texto que vaya a escribir al centro  y el tipo de la letra con el que se va aver"""
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

"""la clase scoreboard tiene un init que lo que hace es inicializar los atributos del objeto, colocandole oarametros como el color que tan inclinado va a estar, el valor predeterminado, para que el cursor se esconda y el programa inicie mas rapido"""
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

### este metodo se utliza para actulizar score 
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", 
align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",
align=ALIGNMENT, font=FONT)
        
### este metodo se utliza para actulizar score mediante la culebra vaya colisionando con la comida 
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()