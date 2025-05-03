from random import*
from pygame import *

class GameSprite(sprite.Sprite):

    def __init__(self, player_image,  player_x, player_y, size_x, size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.side = 'right'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT] :
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] :
            self.rect.x -= self.speed
        if keys_pressed[K_UP] :
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] :
            self.rect.y += self.speed
class BLOCK(GameSprite):
    def __init__(self,player_image,  player_x, player_y, size_x, size_y,player_speed,sdig_x,sdig_y):
        super().__init__( player_image,  player_x, player_y, size_x, size_y,player_speed)
        self.grug=False
        self.sdig_x=sdig_x
        self.sdig_y=sdig_y

    def update(self,t1):
        self.rect.x= t1.rect.x+self.sdig_x
        self.rect.y= t1.rect.y+self.sdig_y



        


win_widht = 500
win_height = 500
kof=5
display.set_caption('Блок баст')
window = display.set_mode((win_widht, win_height))
background = transform.scale(image.load("New Piskel.png"), (500, 500))
t1 = BLOCK("New Piskel (8).png",350,400, 50, 50, 1)

    #gamer = Player("unnamed.jpg",win_widht//2,win_height//2, 50, 50, 5)

#gamer.cvtyf(konmate,0)
#enemutt.cvtyf(komnate,0)
mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
#finish_sound = mixer.Sound('povezlo-povezlo.ogg')
#finish_sound.play()
lini=sprite.Group()
for i in range(7):
    tt = BLOCK("New Piskel (10).png",100+50*i,50, 2, 300, 1)
    lini.add(tt)
for i in range(7):
    tt = BLOCK("New Piskel (10).png",100,50+50*i, 300, 2, 1)
    lini.add(tt)

u=1
back = (80, 80, 80)
run = True
while run:
    window.fill(back)
    window.blit(background,(0,0))
    lini.draw(window)
    t1.reset()
    for e in event.get():
        keys = key.get_pressed()
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            
            x, y = e.pos
            print(x,y,'lj')
            if t1.rect.collidepoint(x,y):
                if t1.grug==False:
                    t1.grug=True
            elif t1.grug==True:
                    t1.grug=False
                    if x%50<=45:
                        x-=x%50
                    else:
                        x+=50-x%50
                    if y%50<=45:
                        y-=y%50
                    else:
                        y+=50-y%50
                    print(x,y,'gckt')
                    t1.rect.x=x
                    t1.rect.y=y
                
                    
    display.update()