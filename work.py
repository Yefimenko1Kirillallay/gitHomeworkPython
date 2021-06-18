import pygame
import sys

# Переменные для установки ширины и высоты окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
mainSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
# Подключение фото для заднего фона
# Здесь лишь создание переменной, вывод заднего фона ниже в коде
bg = pygame.image.load('nugno/fon.jpg')


pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
f = pygame.mixer.Sound('nugno/фоновая музика.mp3')


# Класс, описывающий поведение главного игрока
class Player(pygame.sprite.Sprite) :
    # Изначально игрок смотрит вправо, поэтому эта переменная True
    right = True

    # Методы
    def __init__(self) :
        # Стандартный конструктор класса
        # Нужно ещё вызывать конструктор родительского класса
        super().__init__()

        # Создаем изображение для игрока
        # Изображение находится в этой же папке проекта


        self.image = pygame.image.load('nugno/plaer.png')

        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()
        global change_x
        global change_y
        # Задаем вектор скорости игрока
        self.change_x = 0
        self.change_y = 0

    def update(self) :
        # В этой функции мы передвигаем игрока
        # Сперва устанавливаем для него гравитацию
        self.calc_grav()

        # Передвигаем его на право/лево
        # change_x будет меняться позже при нажатии на стрелочки клавиатуры
        self.rect.x += self.change_x

        # Следим ударяем ли мы какой-то другой объект, платформы, например
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        # Перебираем все возможные объекты, с которыми могли бы столкнуться
        for block in block_hit_list :
            # Если мы идем направо,
            # устанавливает нашу правую сторону на левой стороне предмета, которого мы ударили
            if self.change_x > 0 :
                self.rect.right = block.rect.left
            elif self.change_x < 0 :
                # В противном случае, если мы движемся влево, то делаем наоборот
                self.rect.left = block.rect.right

        # Передвигаемся вверх/вниз
        self.rect.y += self.change_y

        # То же самое, вот только уже для вверх/вниз
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list :
            # Устанавливаем нашу позицию на основе верхней / нижней части объекта, на который мы попали
            if self.change_y > 0 :
                self.rect.bottom = block.rect.top
            elif self.change_y < 0 :
                self.rect.top = block.rect.bottom

            # Останавливаем вертикальное движение
            self.change_y = 0

        blockP_hit_list = pygame.sprite.spritecollide(self, self.levelP.portal_list, False)
        for block in blockP_hit_list :
            if self.change_x > 0  :
                self.rect.right = block.rect.left
                NewLevel()
            elif self.change_x < 0:
                self.rect.left = block.rect.right
                NewLevel()
            elif self.change_y > 0 :
                self.rect.bottom = block.rect.top
                NewLevel()
            elif self.change_y < 0 :
                self.rect.top = block.rect.bottom
                NewLevel()


    def calc_grav(self) :
        # Здесь мы вычисляем как быстро объект будет
        # падать на землю под действием гравитации
        if self.change_y == 0 :
            self.change_y = 1
        else :
            self.change_y += 0.95

        # Если уже на земле, то ставим позицию Y как 0
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0 :
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self) :
        # Обработка прыжка
        # Нам нужно проверять здесь, контактируем ли мы с чем-либо
        # или другими словами, не находимся ли мы в полете.
        # Для этого опускаемся на 10 единиц, проверем соприкосновение и далее поднимаемся обратно
        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 10

        # Если все в порядке, прыгаем вверх
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT :
            self.change_y = -16

    # Передвижение игрока
    def go_left(self) :
        # Сами функции будут вызваны позже из основного цикла
        self.change_x = -10  # Двигаем игрока по Х
        if (self.right) :  # Проверяем куда он смотрит и если что, то переворачиваем его
            self.flip()
            self.right = False

    def go_right(self) :
        # то же самое, но вправо
        self.change_x = 10
        if (not self.right) :
            self.flip()
            self.right = True

    def stop(self) :
        # вызываем этот метод, когда не нажимаем на клавиши
        self.change_x = 0

    def flip(self) :
        # переворот игрока (зеркальное отражение)
        self.image = pygame.transform.flip(self.image, True, False)


#*------------------------------------------*-----------------------------*------------------------*--------------------*-------------------*

# Класс для описания платформы
class Platform(pygame.sprite.Sprite) :
    def __init__(self, width, height) :
        # Конструктор платформ
        super().__init__()
        # Также указываем фото платформы
        self.image = pygame.image.load('nugno/platform.png')
        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()

# Класс для расстановки платформ на сцене
class Level(object) :
    def __init__(self, player) :

        # Создаем группу спрайтов (поместим платформы различные сюда)
        self.platform_list = pygame.sprite.Group()

        # Ссылка на основного игрока

        self.player = player

    # Чтобы все рисовалось, то нужно обновлять экран
    # При вызове этого метода обновление будет происходить
    def update(self) :
        self.platform_list.update()

    # Метод для рисования объектов на сцене
    def draw(self, screen,current) :
        # Рисуем задний фон
        screen.blit(bg, (0, 0))
        # Рисуем все платформы из группы спрайтов
        self.platform_list.draw(screen)


class Level_00(Level) :
    def __init__(self, player) :
        # Вызываем родительский конструктор
        Level.__init__(self, player)

# Класс, что описывает где будут находится все платформы
# на определенном уровне игры
class Level_01(Level) :
    def __init__(self, player) :
        # Вызываем родительский конструктор
        Level.__init__(self, player)
        # Массив с данными про платформы. Данные в таком формате:
        # ширина, высота, x и y позиция
        level = [[210, 32, 300, 500],]
        # Перебираем массив и добавляем каждую платформу в группу спрайтов - platform_list
        for platform in level :
            block = Platform(platform [0], platform [1])
            block.rect.x = platform [2]
            block.rect.y = platform [3]
            block.player = self.player
            self.platform_list.add(block)


class Level_02(Level) :
    def __init__(self, player) :
        # Вызываем родительский конструктор
        Level.__init__(self, player)
        # Массив с данными про платформы. Данные в таком формате:
        # ширина, высота, x и y позиция
        level = [
            [210, 32, 500, 500],
            [210, 32, 500, 400],
            [210, 32, 500, 300],
            [210, 32, 500, 200],
            [210, 32, 500, 100],
            [210, 32, 200, 500],
            [210, 32, 0, 390],
            [210, 32, 300, 270],
            [210, 32, 90, 150],
            ]
        # Перебираем массив и добавляем каждую платформу в группу спрайтов - platform_list
        for platform in level :
            block = Platform(platform [0], platform [1])
            block.rect.x = platform [2]
            block.rect.y = platform [3]
            block.player = self.player
            self.platform_list.add(block)


#*------------------------------------------*-----------------------------*------------------------*--------------------*-------------------*

class Portals(pygame.sprite.Sprite):
    def __init__(self, width, height) :
        # Конструктор платформ
        super().__init__()
        # Также указываем фото платформы
        self.image = pygame.image.load('nugno/portal.png')
        # Установите ссылку на изображение прямоугольника
        self.rect = self.image.get_rect()


class LevelP(object) :
    def __init__(self, player) :

        # Создаем группу спрайтов (поместим платформы различные сюда)
        self.image = pygame.image.load('nugno/portal.png')
        self.portal_list = pygame.sprite.Group()
        # Ссылка на основного игрока
        self.player = player

    # Чтобы все рисовалось, то нужно обновлять экран
    # При вызове этого метода обновление будет происходить
    def update(self) :
        self.portal_list.update()

    # Метод для рисования объектов на сцене
    def draw(self, blockP) :
        global mainSurface
        mainSurface.blit(self.image, (blockP[0], blockP[1]))

class LevelP_00(LevelP) :
    def __init__(self, player) :
        LevelP.__init__(self, player)
        self.portals = [
            [28, 70, SCREEN_WIDTH-28, SCREEN_HEIGHT-70],  ]
        for portal in self.portals :
            blockP = Portals(portal [0], portal [1])
            blockP.rect.x = portal [2]
            blockP.rect.y = portal [3]
            blockP.player = self.player
            self.portal_list.add(blockP)

class LevelP_01(LevelP) :
    def __init__(self, player) :
        LevelP.__init__(self, player)
        self.portals2 = [
            [28, 70, SCREEN_WIDTH-28, SCREEN_HEIGHT-70],  ]
        for portal in self.portals2 :
            blockP = Portals(portal [0], portal [1])
            blockP.rect.x = portal [2]
            blockP.rect.y = portal [3]
            blockP.player = self.player
            self.portal_list.add(blockP)

class LevelP_02(LevelP) :
    def __init__(self, player) :
        LevelP.__init__(self, player)
        self.portals3 = [
            [28, 70, SCREEN_WIDTH-28, SCREEN_HEIGHT-70],]
        for portal in self.portals3 :
            block = Portals(portal [0], portal [1])
            block.rect.x = portal [2]
            block.rect.y = portal [3]
            block.player = self.player
            self.portal_list.add(block)



#*------------------------------------------*-----------------------------*------------------------*--------------------*-------------------*
# Основная функция прогарммы
def main() :
    # Инициализация
    pygame.init()

    # Установка высоты и ширины
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    # Создаем игрока
    global player, xy
    player = Player()
    # Создаем все уровни

    global current_level_no
    current_level_no = 0


    global level_list
    global portal_list
    level_list = [Level_00(player), Level_01(player), Level_02(player)]
    portal_list = [LevelP_00(player),LevelP_01(player),LevelP_02(player)]




    # Устанавливаем текущий уровень

    global active_sprite_list
    global level


    current_level =level_list [current_level_no]
    current_levelP = portal_list [current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    player.levelP = current_levelP



    player.rect.x = 0
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Цикл будет до тех пор, пока пользователь не нажмет кнопку закрытия
    done = False

    # Используется для управления скоростью обновления экрана
    clock = pygame.time.Clock()

    # Основной цикл программы
    while not done :


        f.play(loops=0, maxtime=0, fade_ms=0)

        level=LevelP(player)

        # Название игры
        pygame.display.set_caption("Платформер                                                                                                                                                          Level " + str(current_level_no + 1))

        # Отслеживание действий
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :  # Если закрыл программу, то останавливаем цикл
                done = True

            # Если нажали на стрелки клавиатуры, то двигаем объект
            if event.type == pygame.KEYDOWN  :
                if event.key == pygame.K_LEFT or event.key == pygame.K_a :
                    player.go_left()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                    player.go_right()
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w :
                    player.jump()

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_LEFT and player.change_x < 0 or event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0 or event.key == pygame.K_d and player.change_x > 0 :
                    player.stop()

        # Обновляем игрока
        active_sprite_list.update()

        # Обновляем объекты на сцене
#        current_levelP.update()
        current_level.update()
        current_levelP.update()
        # Если игрок приблизится к правой стороне, то дальше его не двигаем
        if player.rect.right > SCREEN_WIDTH :
            player.rect.right = SCREEN_WIDTH

        # Если игрок приблизится к левой стороне, то дальше его не двигаем
        if player.rect.left < 0 :
            player.rect.left = 0


        xy=[SCREEN_WIDTH-28, SCREEN_HEIGHT-70]
        current_level = level_list [current_level_no]
        current_levelP = portal_list [current_level_no]

        # Рисуем объекты на окне
#        current_levelP.draw(screen)
        current_level.draw(screen,current_level_no)
        current_levelP.draw(xy)
        active_sprite_list.draw(screen)
        # Устанавливаем количество фреймов
        clock.tick(30)

        # Обновляем экран после рисования объектов
        pygame.display.flip()

    # Корректное закртытие программы
    pygame.quit()



def NewLevel():
    global current_level_no
    if current_level_no<2:
        current_level_no += 1
    current_level = level_list [current_level_no]
    current_levelP = level_list [current_level_no]
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    player.rect.x = 0
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
