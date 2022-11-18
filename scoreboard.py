"""En esta seccion del codigo estamos trabajando con el score o puntos del juego inportando la libreria turtle y aliniando el texto que vaya a escribir al centro  y el tipo de la letra con el que se va aver"""
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

# este metodo se utliza para actulizar score 
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", 
align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",
align=ALIGNMENT, font=FONT)
        
# este metodo se utliza para actulizar score mediante la culebra vaya colisionando con la comida 
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()