#Создай собственный Шутер!

from pygame import *

font.init()

font = font.Font(None, 50)
check = font.render("Счёт:", True, (255, 255, 255))
miss = font.render("Пропущено:", True, (255, 255, 255))

win = font.render("YOU WIN", True, (255, 215, 0))
lose = font.render("YOU LOSE", True, (255, 0, 0))

window = display.set_mode((700, 500))

win_width = 700
win_heath = 500

display.set_caption("Шутёр")
background = transform.scale(image.load("galaxy.jpg"), (700,500))


number = 0


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):  
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed

rocket = Player("rocket.png", 350, 400, 5)

class Enemy(GameSprite):
    def update(self):
        number = 0
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y -= win_heath
            number += 1

e1 = Enemy("ufo.png", 100, 0, 0)
e2 = Enemy("ufo.png", 200, 0, 0)
e3 = Enemy("ufo.png", 300, 0, 0)
e4 = Enemy("ufo.png", 400, 0, 0)
e5 = Enemy("ufo.png", 500, 0, 0)
monsters = sprite.Group()
monsters.add(e1,e2,e3,e4,e5)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        """keys = key.get_pressed()
        if keys[K_SPACE]:        
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y += win_heath"""


#b1 = Bullet("bullet.png", rocket.rect.centerx, rocket.rect.top, 2)
bullets = sprite.Group()
#bullets.add(b1)

game = True
finish = False

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:

        window.blit(background,(0, 0))
        window.blit(check, (0, 50))
        window.blit(miss, (0, 100))

        rocket.reset()
        rocket.update()
        monsters.draw(window)
        monsters.update()
        bullets.draw(window)
        bullets.update()

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                bullet = Bullet("bullet.png", rocket.rect.centerx, rocket.rect.top, 2)
                bullets.add(bullet)

        sprites_list = sprite.spritecollide(rocket, monsters, False) 
        if sprites_list or number == 3:
            window.blit(lose, (250, 250))
            finish = True
        
        sprites_list1 = sprite.groupcollide(monsters, bullets, True, True)
        a = 0
        if sprites_list1:
            a += 1
            if a == 5:
                window.blit(win, (250, 250))
                finish = True

        display.update()

clock = time.Clock()
FPS = 60
clock.tick(FPS)
