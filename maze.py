#створи гру "Лабіринт"!
from random import choice
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
TILESIZE = 30 #розмір квадратика карти
WIDTH, HEIGHT = MAP_WIDTH*TILESIZE, MAP_HEIGHT*TILESIZE 



WIDTH, HEIGHT =  MAP_WIDTH*TILESIZE, MAP_HEIGHT*TILESIZE

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
        self.mask = mask.from_surface(self.image)
        all_sprites.add(self)
        

class Player(Sprite):
    def __init__(self, sprite_img,width,height,x,y):
        super().__init__(sprite_img,width,height,x,y)
        self.hp = 100
        self.speed = 2
    def update(self):
        key_pressed = key.get_pressed()
        old_pos = self.rect.x,self.rect.y
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if key_pressed[K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if key_pressed[K_a] and self.rect.x >0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.right < WIDTH :
            self.rect.x += self.speed
        
        collide_list = sprite.spritecollide(self,walls,False,sprite.collide_mask)
        if len(collide_list) > 0:
            self.rect.x , self.rect.y = old_pos


class Enemy(Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__(sprite_img, width, height, x, y)
        # old_pos = self.rect.x,self.rect.y
        self.damage = 100
        self.speed = 1
        self.dir = 'right'
        self.dir_list = ['right','left','up','down']
        self.dir = choice(self.dir_list)
        # enemy_list = sprite.spritecollide(self,walls,False,sprite.collide_mask)
        # if len(enemy_list) > 0:
        #     self.rect.x , self.rect.y = old_pos

    def update(self):
        if self.dir == "right":
            self.rect.x += self.speed
        elif self.dir == "left":
            self.rect.x -= self.speed
        elif self.dir == "up":
            self.rect.y += self.speed
        elif self.dir == "down":
            self.rect.y -= self.speed


player = Player(hero,TILESIZE-5,TILESIZE-5,300,300)
walls = sprite.Group()
cyborgs = sprite.Group()


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
                treasure = Sprite(treasure,70,70,x,y)
            if symbol == "e":
                cyborgs.add(Enemy(cyborg,TILESIZE - 5 , TILESIZE -5 ,x,y))
            
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