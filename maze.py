#створи гру "Лабіринт"!
from pygame import * #імпортування бібліотеки пайгейм


init()
mixer.init()
mixer.music.load("nagets.mp3")
# mixer.music.load("kick.ogg")
# mixer.music.load("money.ogg")

mixer.music.play()
mixer.music.set_volume(0.5)
#створи вікно гри
MAP_WIDTH , MAP_HEIGHT = 25,20 #ширина і висота карти
TILESIZE = 40 #розмір квадратика карти
WIDTH, HEIGHT = MAP_WIDTH*TILESIZE, MAP_HEIGHT*TILESIZE 



WIDTH, HEIGHT = 1100,750

window = display.set_mode((WIDTH, HEIGHT)) #створення дисплею 
FPS = 90 #змінна,яка відровідає за частоту кадрів
clock= time.Clock() #змінна часу


bg = image.load("background.jpg")
bg= transform.scale(bg ,(WIDTH, HEIGHT))
cyborg = image.load('cyborg.png')  #імпортування другого спрайту
hero = image.load('hero.png')  #імпортування другого спрайту
wall= image.load('wall.png')  #імпортування другого спрайту
treasure= image.load('treasure.png')  #імпортування другого спрайту



all_sprites= sprite.Group()

class Sprite(sprite.Sprite): #назва класу
    def __init__(self,sprite_img,width,height,x,y): #властивості 
        super().__init__()
        self.image = transform.scale(sprite_img,(width,height)) #розширення спрайтів
        self.rect = self.image.get_rect() #отримання значення
        self.rect.x = x #присвоєння значення x
        self.rect.y = y #присвоєння значення y
        all_sprites.add(self)
        

class Player(Sprite):
    def __init__(self, sprite_img,width,height,x,y):
        super().__init__(sprite_img,width,height,x,y)
        self.hp = 100
        self.speed = 2
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if key_pressed[K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if key_pressed[K_a] and self.rect.x >0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.right < WIDTH :
            self.rect.x += self.speed

player = Player(hero,TILESIZE,TILESIZE,300,300)
walls = sprite.Group()

with open("map.txt", "r") as f:
    map = f.readlines()
    x = 0
    y = 0
    for line in map:
        for symbol in line:
            if symbol == "w":
                walls.add(Sprite(wall,TILESIZE,TILESIZE,x,y))
            if symbol == "p":
                player.rect.x = x
                player.rect.y = y
            if symbol == "t":
                treasure = Sprite(treasure,70.70,x,y)
            
                x += TILESIZE
        y += TILESIZE
        x = 0
        
run = True

while run: #поки відбувається цикл
    for e in event.get(): #отримання значення 
        if e.type == QUIT: #якщо відбувається вихід
            run = False #цикл закінчується


    
    window.blit(bg,(0,0)) #загрузка заднього фону
    all_sprites.draw(window)
    all_sprites.update()


    
    display.update() #обновлення події дисплею
    clock.tick(FPS) #встановлення частоти кадрів