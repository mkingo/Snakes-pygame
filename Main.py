import pygame
import random
import os
#music player initialization
pygame.mixer.init()



x = pygame.init()
screen_width = 900
screen_height = 600
#colors
white = (255,255,255)
color1 = (180,90,0)
black = (0,0,0)
color = (0,190,0)
red=(255,0,0)
exit_game = False
game_over = False




#Creating game window
gamewindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.update()
pygame.display.set_caption("Snakes and Life ")
pygame.display.update()

#background image
bgimg=pygame.image.load("background.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

#background image for gameover
bgimgGo=pygame.image.load("background.png")
bgimgGo=pygame.transform.scale(bgimgGo,(screen_width,screen_height)).convert_alpha()



clock = pygame.time.Clock()
fps=30
font=pygame.font.SysFont("Gout",35,bold=True,italic=True)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow,colors,snk_list,snake_size):
    for x,y in snk_list:

        pygame.draw.rect(gamewindow, black, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill((120,200,25))
        text_screen("Welcome to Snakes ",black,310,240)
        text_screen("Press spacebar to play the Game! ", black, 210, 280)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('Background.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(30)


#Creating a game loop
def gameloop():

    # Game specific variables
    exit_game = False
    game_over = False

    score = 0
    snake_x = 140
    snake_y = 60
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt","r") as f:
        highscore = f.read()


    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gamewindow.blit(bgimgGo, (0, 0))
            text_screen("Game Over! Press Enter to Restart",(255, 255, 255),250,250)
            text_screen("your Score is : " + str(score) , (255, 255, 255), 340, 300)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score+=5



            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score += 10

                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length+=3




            gamewindow.fill(color)
            gamewindow.blit(bgimg,(0,0))
            text_screen("Score : " + str(score),(0,0,190), 8, 8)
            if score>int(highscore):

                highscore=score
            text_screen("highScore : " + str(highscore),(0,0,190),670, 8)



            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:


                pygame.mixer.music.load('explosion.wav')
                pygame.mixer.music.play()
                game_over=True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:

                pygame.mixer.music.load('explosion.wav')
                pygame.mixer.music.play()
                game_over=True



            pygame.draw.rect(gamewindow, (3,111,70), [food_x, food_y, snake_size, snake_size])




            plot_snake(gamewindow,black,snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()