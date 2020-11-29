import pygame 
import random
import os
import time

pygame.init()
pygame.mixer.init()



# text function
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    display.blit(screen_text, [x,y])

def start():
    global display
    display=pygame.display.set_mode((1000,800),pygame.NOFRAME)
    running=True
    #Background Image
    bgimg = pygame.image.load("5.jpg")
    bgimg = pygame.transform.scale(bgimg, (1000, 800)).convert_alpha()
    display.blit(bgimg, (0, 0))
    pygame.display.update()
    # Color
    black=(0,0,0)
    green=(255,255,255)
    red=(255,0,0)
    
    pygame.display.set_caption("Alien Run | start")
    text_screen("Welcome to Alien Run", green, 300, 300)
    text_screen("Press Space Bar To Play", green, 270, 370)
    pygame.display.update()
    while running:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        mainloop()
                        running=False
running=True
def mainloop():
    pygame.display.set_caption("Alien Run")
# gun positions
    gun_position_y=200
    gun_position_x=20
    gun_v_y=0
# bull positions
    bull_position_x=105
    bull_position_y=gun_position_y+42
    bull_v_x=0
# boll_position
    boll_position_x=1025
    boll_v_x=15
# range
    range1=9
# Color
    black=(0,0,0)
    green=(0,255,0)
    red=(255,0,0)
# mainloop
    global score
    score=0
    live=3
    pygame.display.update()
    boll_position_y=random.randint(20,750)
    boll=True
    bull=False
    clock=pygame.time.Clock()
    while boll:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False
                    quit()
                elif event.key==pygame.K_a:
                    pygame.mixer.music.load('4.mp3')
                    pygame.mixer.music.play()
                    bull=True
                elif event.key==pygame.K_F1 :
                    range1=90
                    pygame.display.update()
                elif event.key==pygame.K_F2 :
                    range1=9
                    bull_position_x=105
                    pygame.mixer.music.load('3.mp3')
                    pygame.mixer.music.play()
                    pygame.display.update()
                elif event.key==pygame.K_UP:
                    gun_v_y=-18
                elif event.key==pygame.K_DOWN:
                    gun_v_y=18
            elif gun_position_y<1000:
                gun_v_y=0
            elif gun_position_y==0:
                gun_v_y=0
        if bull==True:
            for i in range(range1):
                if range1==90:
                    pygame.mixer.music.load('3.mp3')
                    pygame.mixer.music.play()
                pygame.draw.circle(display, red, [bull_position_x,gun_position_y+42],5,5)
                bull_v_x=25
                pygame.display.update()

                bull_position_x=bull_position_x+bull_v_x

                if bull_position_x>1000:
                    bull_v_x=0
                    bull=False
                    bull_position_x=105 

        if boll_position_x<gun_position_x:
            boll_position_y=random.randint(20,750)
            live-=1
            pygame.mixer.music.load('5.mp3')
            pygame.mixer.music.play()
            boll_position_x=1025
            time.sleep(3)
            pygame.display.update()
        if live==0:
            boll=False
            with open("hiscroe.txt","w") as f:
                f.write(str(score))
            gameover()
            f.close()
        if gun_position_x==boll_position_x and abs(gun_position_y-boll_position_y)<50:
            live-=1
            pygame.draw.rect(display, green, [gun_position_x,gun_position_y,56,5],50)
        if  (bull_position_x-boll_position_x)>=5 and abs(gun_position_y-boll_position_y)<50:
            bull_v_x=0
            boll_position_x=1050
            boll_position_y=random.randint(20,750)
            # bull_position_y=gun_position_y+42
            score+=1
            pygame.mixer.music.load('2.mp3')
            pygame.mixer.music.play()
        # if score> int(hiscore):
        #     hiscore=score
            # print(score)
        # display.fill(black)
        bgimg = pygame.image.load("4.jpg")
        bgimg = pygame.transform.scale(bgimg, (1000, 800)).convert_alpha()
        display.blit(bgimg, (0, 0))
        text_screen(f"Score:{score}", green, 0, 5)
        # text_screen("Hiscore{hiscore}", green, 180, 5)
        text_screen(f"Lives:{live}", green, 200, 5)
        clock.tick(50)

        bgimg2 = pygame.image.load('3.png')
        bgimg2 = pygame.transform.scale(bgimg2, (120, 80)).convert_alpha()
        display.blit(bgimg2, (gun_position_x,gun_position_y))

        bgimg2 = pygame.image.load('2.png')
        bgimg2 = pygame.transform.scale(bgimg2, (90, 70)).convert_alpha()
        display.blit(bgimg2, (boll_position_x,boll_position_y))

        boll_position_x=boll_position_x-boll_v_x
        gun_position_y=gun_position_y+gun_v_y
        pygame.display.update()

def gameover():
    running=True
    red=(255,0,0)
    green=(0,255,0)
    pygame.display.set_caption("Alien Run | Game_Over")
    bgimg = pygame.image.load("1.jpg")
    bgimg = pygame.transform.scale(bgimg, (1000, 800)).convert_alpha()
    display.blit(bgimg, (0, 0))
    text_screen("GameOver", red, 390, 330)
    text_screen("Press Enter To Play Again", red, 250, 400)
    text_screen(f"Your scroe {score}", red, 375, 470)
    pygame.display.update()
    while running:
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                running=False
                quit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    mainloop()
            elif score<=10:
                pygame.mixer.music.load('6.mp3')
                pygame.mixer.music.play()
            elif score>10:
                pygame.mixer.music.load('1.mp3')
                pygame.mixer.music.play()
        pygame.display.update()
        time.sleep(2)
    
            
            
if __name__ == "__main__":

    start()

