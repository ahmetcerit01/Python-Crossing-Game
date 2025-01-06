import turtle
from turtle import Turtle

# Adamın görselini ekleyin
turtle.addshape('man_resized.gif')
# Sabitler
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player:
    def __init__(self):
        """Oyuncuyu başlatır ve başlangıç konumuna yerleştirir."""
        self.player = Turtle()
        self.player.penup()
        self.player.shape('man_resized.gif')  # Adamın görselini ekler
        self.reset_position()
        self.player.setheading(90)  # Yukarı doğru bakacak şekilde ayarlanır

    def move(self):
        """Adamı yukarı doğru hareket ettirir."""
        self.player.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Adamı başlangıç konumuna geri koyar."""
        self.player.goto(STARTING_POSITION)

    def has_crossed_finish_line(self):
        """Adamın bitiş çizgisine ulaşıp ulaşmadığını kontrol eder."""
        return self.player.ycor() > FINISH_LINE_Y
