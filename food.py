"""Inportando la libreria turtle y random que contiene una serie de funciones relacionadas con los valores aleatorios"""
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
# Le esta diciendo que aparesca aleatoriamente en eje x y y no saliendose de los parametros de 200 y - 200 para que no se salga de la interfaz grafica 
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)