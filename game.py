import pygame
import sys
import random
import time
import matplotlib.pyplot as plt
import numpy as np

def inputN0(lo,lp):
#    im = Image.open('learn/'+str(lp+1)+'.jpg')
#    pix = im.getdata()
#    Apix = np.array(pix)
#    for x in range(9):
#        if Apix[x,0]>0:
#            lo[x,0] = 0
#        else:
#            lo[x,0] = 1
    return lo
def graph(y,f):
    x = np.arange(f)
    plt.plot(x, y, label='Error')
    plt.title('Graph')
    plt.legend()
    plt.show()
    return 5
def ForWards(Li,W,Lo):
    xt = W.shape[1]
    yt = W.shape[0]
    print(Lo,W,xt,yt);
    print('\n')
    for x in range(xt):
        Lo[x,0] = 0
        for y in range(yt):
            Lo[x,0] += Li[y,0]*W[y,x]
        Lo[x,0] = 1/(1+np.exp(-1*Lo[x,0]))
    return Lo
def fixOutError(ho,lo):
    xt = lo.shape[0]
    for x in range(xt):
        lo[x,1] = (ho[x]- lo[x,0]) #* lo[x,0] * (1-lo[x,0])
    return lo
def findError(Li,W,Lo):
    xt = W.shape[0]-1 # 3
    yt = W.shape[1] # 2
    for x in range(xt):
        Li[x,1] = 0
        for y in range(yt):
            Li[x,1] += Lo[y,1]*W[x,y]
        #Li[x,1] = Li[x,1]*Lo[y,0]*(1-Lo[y,0])
    return Li
def backWards(Li,W,Lo,n):
    xt = W.shape[0]
    yt = W.shape[1]
    for y in range(yt):     
        for x in range(xt):
            W[x,y] += n*Lo[y,1]*Li[x,0]*Lo[y,0]*(1-Lo[y,0])
    return W

# N - Кол-во входных данных
# Nh - Массив(кол-во нейронов на каждом скрытом слое) [4,3] - на первом 4 нейрона, на втором 3
# No - Кол-во выходных нейронов
# nr - Есть ли нейрон смещения

Nh = np.array([9,5,4,2])
nr = 1



k = len(Nh)
r = 0
if nr>0:
	r = 1
for i in range(k-1):
	exec('N'+str(i)+' = np.array(range('+str(Nh[i]+r)+'*2), float).reshape(('+str(Nh[i]+r)+', 2))')
	exec('N'+str(i)+'.fill(0)')
	if r == 1:
		exec('N'+str(i)+'['+str(Nh[i])+',0] = 1')
exec('N'+str(k-1)+' = np.array(range('+str(Nh[k-1])+'*2), float).reshape(('+str(Nh[k-1])+', 2))')
for i in range(k-1):
        
	exec('W'+str(i)+str(i+1)+' = np.array(np.random.rand('+str((Nh[i]+r)*Nh[i+1])+'), float).reshape(('+str(Nh[i]+r)+', '+str(Nh[i+1])+'))')

IDL = np.array(range(2), float).reshape((2, 1)) # Ответы к тестам
epoh = 50
ite = 16
p = 0.5
Error = np.array(range(epoh), float) 
Error.fill(0)

idl = np.array([[0.8,0.2],
               [0.8,0.2],
               [0.8,0.2],
               [0.2,0.8],
               [0.2,0.8],
               [0.2,0.8],
               [0.8,0.8],
               [0.8,0.8],
               [0.8,0.8],
               [0.8,0.8],
               [0.8,0.8],
               [0.8,0.8],
               [0.8,0.8],
               [0.8,0.8],
               [0.8,0.8],
               [0.2,0.2]
               ],float
               )
for d in range(epoh):
	for i in range(ite):
		exec('N0 = inputN0(N0,'+ str(i) +')')        
		IDL = idl[i,:]

		for j in range(k-1):
			exec('N'+str(j+1)+' = ForWards(N'+str(j)+',W'+str(j)+str(j+1)+',N'+str(j+1)+')')
        
		exec('N'+str(k-1)+' = fixOutError(IDL,N'+str(k-1)+')')
		for j in range(k-2,0,-1):
			exec('N'+str(j)+' = findError(N'+str(j)+', W'+str(j)+str(j+1)+', N'+str(j+1)+')')
            
		for j in range(k-1):
			exec('W'+str(j)+str(j+1)+' = backWards(N'+str(j)+', W'+str(j)+str(j+1)+', N'+str(j+1)+', '+str(p)+')')
        
		exec('Error[d] += 0.5*(IDL[0]-N3[0,0])*(IDL[0]-N3[0,0]) + 0.5*(IDL[1]-N3[1,0])*(IDL[1]-N3[1,0])')
            #exec('print(W01,W12,W23)')
            #exec('print(N1,N2,N3)')
    
exec('graph(Error,epoh)')






print("Выходные данные после тренировки:")



class Game():
    def __init__(self):
        # задаем размеры экрана
        self.screen_width = 720
        self.screen_height = 460

        # необходимые цвета
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)

        # Frame per second controller
        # будет задавать количество кадров в секунду
        self.fps_controller = pygame.time.Clock()

        # переменная для оторбражения результата
        # (сколько еды съели)
        self.score = 0

    def init_and_check_for_errors(self):
        """Начальная функция для инициализации и
           проверки как запустится pygame"""
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')

    def set_surface_and_title(self):
        """Задаем surface(поверхность поверх которой будет все рисоваться)
        и устанавливаем загаловок окна"""
        self.play_surface = pygame.display.set_mode((
            self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake Game')

    def event_loop(self, change_to):
        """Функция для отслеживания нажатий клавиш игроком"""

        # запускаем цикл по ивентам
        for event in pygame.event.get():
            # если нажали клавишу
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                # нажали escape
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return change_to

    def refresh_screen(self):
        """обновляем экран и задаем фпс"""
        pygame.display.flip()
        game.fps_controller.tick(23)

    def show_score(self, choice=1):
        """Отображение результата"""
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(
            'Score: {0}'.format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        # дефолтный случай отображаем результат слева сверху
        if choice == 1:
            s_rect.midtop = (80, 10)
        # при game_overe отображаем результат по центру
        # под надписью game over
        else:
            s_rect.midtop = (360, 120)
        # рисуем прямоугольник поверх surface
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self):
        """Функция для вывода надписи Game Over и результатов
        в случае завершения игры и выход из игры"""
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()


class Snake():
    def __init__(self, snake_color):
        # важные переменные - позиция головы змеи и его тела
        self.snake_head_pos = [100, 50]  # [x, y]
        # начальное тело змеи состоит из трех сегментов
        # голова змеи - первый элемент, хвост - последний
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_color = snake_color
        # направление движение змеи, изначально
        # зададимся вправо
        self.direction = "RIGHT"
        # куда будет меняться напрвление движения змеи
        # при нажатии соответствующих клавиш
        self.change_to = self.direction

    def validate_direction_and_change(self):
        """Изменияем направление движения змеи только в том случае,
        если оно не прямо противоположно текущему"""
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def change_head_position(self):
        """Изменияем положение головы змеи"""
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10

    def snake_body_mechanism(
            self, score, food_pos, screen_width, screen_height):
        # если вставлять просто snake_head_pos,
        # то на всех трех позициях в snake_body
        # окажется один и тот же список с одинаковыми координатами
        # и мы будем управлять змеей из одного квадрата
        self.snake_body.insert(0, list(self.snake_head_pos))
        # если съели еду
        if (self.snake_head_pos[0] == food_pos[0] and
                self.snake_head_pos[1] == food_pos[1]):
            # если съели еду то задаем новое положение еды случайным
            # образом и увеличивем score на один
            food_pos = [random.randrange(1, screen_width/10)*10,
                        random.randrange(1, screen_height/10)*10]
            score += 1
        else:
            # если не нашли еду, то убираем последний сегмент,
            # если этого не сделать, то змея будет постоянно расти
            self.snake_body.pop()
        return score, food_pos

    def draw_snake(self, play_surface, surface_color):
        """Отображаем все сегменты змеи"""
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            # pygame.Rect(x,y, sizex, sizey)
            pygame.draw.rect(
                play_surface, self.snake_color, pygame.Rect(
                    pos[0], pos[1], 10, 10))

    def check_for_boundaries(self, game_over, screen_width, screen_height):
        """Проверка, что столкунлись с концами экрана или сами с собой
        (змея закольцевалась)"""
        if any((
            self.snake_head_pos[0] > screen_width-10
            or self.snake_head_pos[0] < 0,
            self.snake_head_pos[1] > screen_height-10
            or self.snake_head_pos[1] < 0
                )):
            game_over()
        for block in self.snake_body[1:]:
            # проверка на то, что первый элемент(голова) врезался в
            # любой другой элемент змеи (закольцевались)
            if (block[0] == self.snake_head_pos[0] and
                    block[1] == self.snake_head_pos[1]):
                game_over()


class Food():
    def __init__(self, food_color, screen_width, screen_height):
        """Инит еды"""
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [random.randrange(1, screen_width/10)*10,
                         random.randrange(1, screen_height/10)*10]

    def draw_food(self, play_surface):
        """Отображение еды"""
        pygame.draw.rect(
            play_surface, self.food_color, pygame.Rect(
                self.food_pos[0], self.food_pos[1],
                self.food_size_x, self.food_size_y))


game = Game()
snake = Snake(game.green)
food = Food(game.brown, game.screen_width, game.screen_height)

game.init_and_check_for_errors()
game.set_surface_and_title()

while True:
    snake.change_to = game.event_loop(snake.change_to)

    snake.validate_direction_and_change()
    snake.change_head_position()
    game.score, food.food_pos = snake.snake_body_mechanism(game.score, food.food_pos, game.screen_width, game.screen_height)
    snake.draw_snake(game.play_surface, game.white)

    food.draw_food(game.play_surface)

    snake.check_for_boundaries(game.game_over, game.screen_width, game.screen_height)

    game.show_score()
    game.refresh_screen()
