from turtle import Turtle

# Yazı tipi tanımı
FONT = ("Poppins", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """Scoreboard başlatılır ve başlangıç seviyesine ayarlanır."""
        super().__init__()
        self.level = 1
        self.hideturtle()  # Turtle göstergesini gizle
        self.penup()
        self.color("black")  # Yazının rengi (başlangıçta siyah)
        self.goto(-230, 270)  # Skor tahtasının pozisyonu
        self.update_scoreboard()

    def update_scoreboard(self):
        """Skor tahtasını günceller."""
        self.clear()  # Eski yazıyı temizle
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        """Seviyeyi bir artırır ve günceller."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Oyun bittiğinde ekrana 'GAME OVER' mesajı beyaz renkte yazar."""
        self.goto(0, 0)  # Ekranın ortasına gider
        self.clear()  # Herhangi bir çakışmayı önlemek için önce temizler
        self.color("white")  # Yazının rengini beyaz yapar
        self.write("GAME OVER", align="center", font=FONT)
        self.hideturtle()  # Turtle nesnesini tekrar gizler
