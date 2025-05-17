from random import*
from pygame import *

class GameSprite(sprite.Sprite):

    def __init__(self, player_image,  player_x, player_y, size_x, size_y,player_speed):
        super().__init__()
        self.im=player_image
        self.image = transform.scale(image.load(self.im), (size_x, size_y))
        self.speed = player_speed

        self.size_x=size_x
        self.size_y=size_y
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

        if self.rect.y<400:
            self.cppium()
            self.kill()
   
    

   

            
    def cppium(self):
        t9 = BLOCK(self.im, self.rect.x,self.rect.y, self.size_x, self.size_y, 0,0,0)
        cop.add(t9)

class deleter(GameSprite):
    def __init__(self,player_image,  player_x, player_y, size_x, size_y,player_speed,sdig_x,sdig_y):
        super().__init__( player_image,  player_x, player_y, size_x, size_y,player_speed)
        self.delete=True
    def update1(self):
        
        for j in range(6):
            count=0
            for i in range(6):
                self.rect.x=110+i*50
                #print(self.rect.x,self.rect.y,sprite.spritecollide(self, cop, False))
                if not sprite.spritecollide(self, cop, False):
                    self.delete=False
            if self.delete:
                count+=1
                for i in range(11):
                    self.rect.x=110+i*50
                    if sprite.spritecollide(self, cop, True):
                        pass
            self.delete=True
            self.rect.y=60+j*50
        return count

    def update2(self):
        
        for j in range(6):
            count=0
            for i in range(6):
                self.rect.y=60+i*50
                #print(self.rect.x,self.rect.y,sprite.spritecollide(self, cop, False))
                if not sprite.spritecollide(self, cop, False):
                    self.delete=False
            if self.delete:
                count+=1
                for i in range(9):
                    self.rect.y=60+i*50
                    if sprite.spritecollide(self, cop, True):
                        pass
            self.delete=True
            self.rect.x=110+j*50
        return count
        

        



        
cop=sprite.Group()

win_widht = 500
win_height = 500
kof=5
display.set_caption('Блок баст')
window = display.set_mode((win_widht, win_height))
background = transform.scale(image.load("New Piskel (9).png"), (500, 500))


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
    tt = GameSprite("New Piskel (10).png",100+50*i,50, 2, 300, 1)
    lini.add(tt)
for i in range(7):
    tt = GameSprite("New Piskel (10).png",100,50+50*i, 300, 2, 1)
    lini.add(tt)
t1 = BLOCK('bgqwe.jpg', 100,500, 50, 50 ,0,0,0)
delet = deleter('bgqwe.jpg', 0,0, 5, 30 ,0,0,0)
blocks = sprite.Group()
def create_ge(blocks):
    global t1
    t1 = BLOCK('bgqwe.jpg', 100,400, 50, 50 ,0,0,0)
    blocks.add(t1)
    t2 = BLOCK('New Piskel (8).png', t1.rect.x,t1.rect.y, 50, 50, 0,50,0)
    blocks.add(t2)
    t3 = BLOCK('New Piskel (8).png', t1.rect.x,t1.rect.y, 50, 50, 0,100,0)
    blocks.add(t3)
    t4 = BLOCK('New Piskel (8).png', t1.rect.x,t1.rect.y, 50, 50, 0,100,50)
    blocks.add(t4)
    blocks.update(t1)
create_ge(blocks)

def create_palki(blocks):
    global t1
    t1 = BLOCK('bgqwe.jpg', 100,400, 50, 50 ,0,0,0)
    blocks.add(t1)
    t2 = BLOCK('New Piskel (11).png', t1.rect.x,t1.rect.y, 50, 50, 0,50,0)
    blocks.add(t2)
    blocks.update(t1)

def create_yy(blocks):
    global t1
    t1 = BLOCK('bgqwe.jpg', 100,400, 50, 50 ,0,0,0)
    blocks.add(t1)
    t2 = BLOCK('New Piskel (12).png', t1.rect.x,t1.rect.y, 50, 50, 0,50,0)
    blocks.add(t2)
    t3 = BLOCK('New Piskel (12).png', t1.rect.x,t1.rect.y, 50, 50, 0,100,0)
    blocks.add(t3)
    t4 = BLOCK('New Piskel (12).png', t1.rect.x,t1.rect.y, 50, 50, 0,100,50)
    blocks.add(t4)
    t5 = BLOCK('New Piskel (12).png', t1.rect.x,t1.rect.y, 50, 50, 0,100,100)
    blocks.add(t5)
    blocks.update(t1)

count=0
u=1
back = (80, 80, 80)
run = True
FPS = 60
finish=False
def drug(t1,x,y):
    global blocks
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
                    blocks.update(t1)
                    
                    k=randint(0,2)
                    if k==0:
                        create_ge(blocks)
                    elif k==1:
                        create_palki(blocks)
                    elif k==2:
                        create_yy(blocks)

while run:
    window.fill(back)
    window.blit(background,(0,0))
    lini.draw(window)
    blocks.draw(window)
    cop.draw(window)
    
    for e in event.get():
        keys = key.get_pressed()
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            
            print(count)
            
            x, y = e.pos
            drug(t1,x,y)
            count+=delet.update1()
            count+=delet.update2()

                
                    
    display.update()