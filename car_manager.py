import turtle
from turtle import Turtle
import random

# Ekrandaki gereksiz kaplamayı gizleme


# Sabitler
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

CAR_GIFS = [
    "redcar_resized.gif",
    "bluecar_resized.gif",
    "greencar_resized.gif",
    "yellowcar_resized.gif",
    "blackcar_resized.gif"
]

LANE_POSITIONS = [-170, -130, -110, -60, -15, 35, 85, 135]  # Arabalar için tam ortalanmış şeritler

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

        # GIF'leri ekrana yükleme
        for gif in CAR_GIFS:
            turtle.getscreen().addshape(gif)

        turtle.hideturtle()




    def create_car(self):
        """Rastgele bir şeritte araba oluşturur."""
        chance = random.randint(1, 10)
        if chance == 1:  # Arabalar daha az sıklıkla oluşturuluyor
            random_y = random.choice(LANE_POSITIONS)

            # Aynı şeritte yakın bir araba varsa araba oluşturma
            for car in self.all_cars:
                if car.ycor() == random_y and car.xcor() > 200:
                    return  # Aynı şeritte yakın bir araba var, araba oluşturma

            # Yeni araba oluştur ve listeye ekle
            new_car = Turtle(random.choice(CAR_GIFS))
            new_car.penup()
            new_car.goto(300, random_y)  # Sağdan ekrana giriş yapıyor
            self.all_cars.append(new_car)

    def move_cars(self):
        """Arabaları ekranda sola doğru hareket ettirir."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Seviyeyi yükseltir ve arabaların hızını artırır."""
        self.car_speed += MOVE_INCREMENT
