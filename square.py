import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("white")


blue=(0,0,255)
green=(0,255,0)
pygame.display.update()

class Square():
    def __init__(self,color,dimensions):
        self.rect_surface=screen
        self.rect_color=color
        self.rect_dimensions=dimensions
    def draw(self):
        self.Draw_Rect=pygame.draw.rect(self.rect_surface, self.rect_color, self.rect_dimensions)
    
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    blue_rect=Square(blue,(10,10,50,50))
    green_rect=Square(green,(90,90,150,150))
    blue_rect.draw()
    green_rect.draw()
    pygame.display.update()   

