from PIL import Image

# Adam görselini yeniden boyutlandır
img = Image.open("man.gif")  # Mevcut görsel dosyasının adı
resized_img = img.resize((int(img.width * 0.3), int(img.height * 0.3)))
resized_img.save("man_resized.gif")
print("Görsel yeniden boyutlandırıldı ve 'man_resized.gif' olarak kaydedildi.")

# Ortak boyutlandırma oranı
resize_factor = 1

# Red
red_car_img = Image.open("redcar.gif")
resized_red_car_img = red_car_img.resize((int(red_car_img.width * resize_factor), int(red_car_img.height * resize_factor)))
resized_red_car_img.save("redcar_resized.gif")

# Blue
blue_car_img = Image.open("bluecar.gif")
resized_blue_car_img = blue_car_img.resize((int(blue_car_img.width * resize_factor), int(blue_car_img.height * resize_factor)))
resized_blue_car_img.save("bluecar_resized.gif")

# Green
green_car_img = Image.open("greencar.gif")
resized_green_car_img = green_car_img.resize((int(green_car_img.width * resize_factor), int(green_car_img.height * resize_factor)))
resized_green_car_img.save("greencar_resized.gif")

# Black
black_car_img = Image.open("blackcar.gif")
resized_black_car_img = black_car_img.resize((int(black_car_img.width * resize_factor), int(black_car_img.height * resize_factor)))
resized_black_car_img.save("blackcar_resized.gif")


# Yellow
yellow_car_img = Image.open("yellowcar.gif")
resized_yellow_car_img = yellow_car_img.resize((int(yellow_car_img.width * resize_factor), int(yellow_car_img.height * resize_factor)))
resized_yellow_car_img.save("yellowcar_resized.gif")