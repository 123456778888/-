from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, suze_x, sixe_y, player_x_speed,player_y_speed):
        GameSprite___init___(self, player_image, player_x, player_y,size_x, size_y)

        self.player_x_speed = player_x_speed
        self.player_y_speed = player_y_speed
    def update(self):
        self.rect.x += self.player_x_speed
        self.rect.y += self.player_y_speed
win_width = 700
win_height = 500
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load('images.jpg'),(win_width,win_height))
w1 = GameSprite('platform2.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
W2 = GameSprite('platform2_v.png', 370, 100, 50, 400)
packman = Plaer('hero.png', 5, win_height - 80, 80, 80, 0, 0)
run = True
while run:
    time.delay(50)
    window.blit(back, (0,0))

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.player_x_speed = - 5
            elif e.key == K_RIGHT:
                packman.player_x_speed = 5
            elif e.key == K_UP:
                packman.y_speed = -5
            elif e.key == K_DOWN:
                packman.y_speed = 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
    w1.reset()
    w2.reset()
    packman.reset()

    packman.update()

    display.update

                

            


