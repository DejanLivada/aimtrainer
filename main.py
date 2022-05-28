import pygame
import sys
import random
from pygame.math import Vector2
pygame.init()
prozor = pygame.display.set_mode((600,600))
sat = pygame.time.Clock()
score = 0


class Button():
    def __init__(self , slika , pozicija):
        self.slika = slika
        self.pozicija = pozicija
    def draw(self):
        prozor.blit(self.slika , self.pozicija)


play_again_dugme = Button(pygame.image.load("play_again.png") , (150 , 400))


class Tacka():
    def __init__(self  , slika : pygame.Surface , pozicija):
        self.slika = slika
        self.pozicija = pozicija
    def draw(self):
        self.slika = pygame.transform.scale(self.slika , (100,100))
        prozor.blit(self.slika , self.pozicija)
    def changepos(self):
        self.pozicija = Vector2 (random.randint(0 , 500) , random.randint(0 , 500))
        global score
        score += 1



tacka = Tacka(pygame.image.load("target.png") , (random.randint(0 , 500) , random.randint(0 , 500)))


timer = 10
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont("Consolas" , 30)
gameoverfont = pygame.font.SysFont("Consolas" , 60)
game_over_text = gameoverfont.render("Gameover" , True , (255,255,255))

def play():

    global timer
    program_radi = True
    while program_radi:
        counter_text = font.render(f"Time left : {timer}", True, (255, 255, 255))
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if tacka.slika.get_rect().move(tacka.pozicija).collidepoint(dogadjaj.pos):
                    tacka.changepos()
                    global score

                    score += 1
            if dogadjaj.type == pygame.USEREVENT:
                timer -= 1

        prozor.fill((55, 255, 0))
        prozor.blit(counter_text , (10,10))

        tacka.draw()
        if timer <= 0:
            game_over()

        pygame.display.flip()
        sat.tick(30)

    pygame.quit()
def game_over():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if play_again_dugme.slika.get_rect().move(play_again_dugme.pozicija).collidepoint(dogadjaj.pos):
                    play()
        score_text = gameoverfont.render(f"Score: {score}", True, (255, 255, 255))
        prozor.fill((55, 255, 0))
        prozor.blit(game_over_text , (200 , 50))
        prozor.blit(score_text , (200 , 200))
        play_again_dugme.draw()

        pygame.display.flip()
        sat.tick(30)

    pygame.quit()
play()