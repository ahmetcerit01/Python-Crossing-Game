import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Ekran ayarları
screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("way.gif")
screen.tracer(0)

# Oyun objeleri
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Klavye kontrolleri
screen.listen()
screen.onkey(player.move, "Up")

# Oyun döngüsü
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Arabaları hareket ettir
    car_manager.create_car()
    car_manager.move_cars()

    # Çarpma kontrolü
    for car in car_manager.all_cars:
        if car.distance(player.player) < 67:  # Arabayla oyuncu çarpışırsa
            game_is_on = False
            scoreboard.game_over()

    # Bitiş çizgisine ulaşma kontrolü
    if player.has_crossed_finish_line():
        player.reset_position()  # Oyuncuyu başlangıca döndür
        car_manager.level_up()  # Arabaların hızını artır
        scoreboard.update_scoreboard() # Skoru artır
        scoreboard.increase_level()  # Seviyeyi artır


screen.exitonclick()