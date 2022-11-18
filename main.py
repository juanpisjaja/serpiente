"""En las lineas 2-6 esta inportando dos librerias 
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

# Esta definiendo la distacia para que detecte la colicion con el alimento
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# Esta definiendo la distacia para que detecte la colicion con Lla pared
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

# Esta definiendo la distacia para que detecte la colicion con el mismo
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
# Esto sirve para que la interfaz no se cierre antes de que inicie el juego 
screen.exitonclick()
