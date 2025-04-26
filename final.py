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


        


win_widht = 500
win_height = 500
kof=5
display.set_caption('Блок баст')
window = display.set_mode((win_widht, win_height))
#gamer = Player("unnamed.jpg",win_widht//2,win_height//2, 50, 50, 5)

#gamer.cvtyf(konmate,0)
#enemutt.cvtyf(komnate,0)
mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
#finish_sound = mixer.Sound('povezlo-povezlo.ogg')
#finish_sound.play()

u=1
back = (80, 80, 80)
run = True
while run:
    window.fill(back)

    for e in event.get():
        if e.type == QUIT:
            run = False



    display.update()