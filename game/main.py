# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#         	           ~Snake Game~
#  		        Adi Goldstein
#        		Firas Sawaed
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Import the required modules
import pygame
import button
from pygame.locals import *
import random

# Set the size of each cell in pixels
SIZE = 40

# Set the background color of the game screen
BACKGROUND_COLOR = (110, 110, 5)

# Create a clock object to control the game's frames per second (FPS)
clock = pygame.time.Clock()

# Set the desired FPS for the game
FPS = 60

# Set the initial speed of the game elements (change by each level)
SPEED = 8


class Button:
    # Initialize button properties
    def __init__(self, x, y, image, scale):
        # Get the width and height of the image
        width = image.get_width()
        height = image.get_height()

        # Scale the image
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        # Get the rectangular shape of the image
        self.rect = self.image.get_rect()

        # Set the top left corner of the rectangular shape to the specified x and y position
        self.rect.topleft = (x, y)

        # Set the clicked attribute to False (indicating the button has not been clicked yet)
        self.clicked = False

    # Draw the button on the screen and check if it has been clicked
    def draw(self, surface):
        # Set action to False (indicating the button has not been clicked)
        action = False

        # Get the mouse position
        pos = pygame.mouse.get_pos()

        # Check if mouse is over the button and if the left mouse button is pressed
        if self.rect.collidepoint(pos):
            # Check if the button has not been clicked yet
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                # Set the clicked attribute to True (indicating the button has been clicked)
                self.clicked = True

                # Set action to True (indicating the button has been clicked)
                action = True

        # Check if the left mouse button is released
        if pygame.mouse.get_pressed()[0] == 0:
            # Set the clicked attribute to False (indicating the button is not being clicked anymore)
            self.clicked = False

        # Draw the button on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        # Return the action (indicating whether the button has been clicked or not)
        return action


class Apple:
    # Initialize the apple properties
    def __init__(self, parent_screen):
        # Set the parent screen that the apple will be drawn on
        self.parent_screen = parent_screen

        # Load the apple image
        self.image = pygame.image.load("resources/apple.png")

        # Set the initial x and y position of the apple
        self.x = 120
        self.y = 120

    # Draw the apple on the screen
    def draw(self):
        # Blit (or draw) the apple image onto the parent screen at the specified x and y position
        self.parent_screen.blit(self.image, (self.x, self.y))

    # Move the apple to a new random location on the screen
    def move(self):
        # Set a new random x and y position for the apple within the specified range
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE


class PoisonApple:
    # Initialize the poison apple properties
    def __init__(self, parent_screen):
        # Set the parent screen that the poison apple will be drawn on
        self.parent_screen = parent_screen

        # Load the poison apple image
        self.image = pygame.image.load("resources/posionapple.png")

        # Set the initial x and y position of the poison apple
        self.x = 320
        self.y = 320

    # Draw the poison apple on the screen
    def draw(self):
        # Blit (or draw) the poison apple image onto the parent screen at the specified x and y position
        self.parent_screen.blit(self.image, (self.x, self.y))

    # Move the poison apple to a new random location on the screen
    def move(self):
        # Set a new random x and y position for the poison apple within the specified range
        self.x = random.randint(1, 22) * SIZE
        self.y = random.randint(1, 19) * SIZE

class GoldenApple:
    # Initialize the golden apple properties
    def __init__(self, parent_screen):
        # Set the parent screen that the golden apple will be drawn on
        self.parent_screen = parent_screen

        # Load the golden apple image
        self.image = pygame.image.load("resources/goldenapple.png")

        # Set the initial x and y position of the golden apple
        self.x = 320
        self.y = 240

    # Draw the golden apple on the screen
    def draw(self):
        # Blit (or draw) the golden apple image onto the parent screen at the specified x and y position
        self.parent_screen.blit(self.image, (self.x, self.y))

    # Move the golden apple to a new random location on the screen
    def move(self):
        # Set a new random x and y position for the golden apple within the specified range
        self.x = random.randint(1, 22) * SIZE
        self.y = random.randint(1, 15) * SIZE


class Snake1:
    def __init__(self, parent_screen):
        # Set the parent screen
        self.parent_screen = parent_screen

        # Load the snake body image
        self.image = pygame.image.load("resources/block.jpg").convert()

        # Set the initial direction of the snake
        self.direction = "down"

        # Set the initial length and position of the snake
        self.length = 1
        self.x = [40]
        self.y = [40]

    # Function to move the snake to the left
    def move_left(self):
        self.direction = "left"

    # Function to move the snake to the right
    def move_right(self):
        self.direction = "right"

    # Function to move the snake up
    def move_up(self):
        self.direction = "up"

    # Function to move the snake down
    def move_down(self):
        self.direction = "down"

    # Function to update the position of the snake based on its direction
    def walk(self):
        # Update the position of the body
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # Update the position of the head
        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE
        if self.direction == "up":
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE

        # Draw the updated snake
        self.draw()

    # Function to draw the snake
    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

    # Function to increase the length of the snake
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Snake2:
    def __init__(self, parent_screen):
        # Store the reference to the parent screen
        self.parent_screen = parent_screen

        # Load the image for the snake block and store it
        self.image = pygame.image.load("resources/block2.jpg").convert()

        # Set the default direction of the snake
        self.direction = "down"

        # Initialize the length and position of the snake
        self.length = 1
        self.x = [40]
        self.y = [160]

    def move_left(self):
        # Set the direction of the snake to left
        self.direction = "left"

    def move_right(self):
        # Set the direction of the snake to right
        self.direction = "right"

    def move_up(self):
        # Set the direction of the snake to up
        self.direction = "up"

    def move_down(self):
        # Set the direction of the snake to down
        self.direction = "down"

    def walk(self):
        # Update the body of the snake
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # Update the head of the snake
        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE
        if self.direction == "up":
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE

        # Draw the snake on the screen
        self.draw()

    def draw(self):
        # Draw the blocks of the snake on the screen
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

    def increase_length(self):
        # Increase the length of the snake by 1 block
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


def is_collision(x1, y1, x2, y2):
    # Check if two objects have collided, given their x and y coordinates.
    # param x1: x-coordinate of first object
    # param y1: y-coordinate of first object
    # param x2: x-coordinate of second object
    # param y2: y-coordinate of second object
    # return: True if objects have collided, False otherwise.

    if (x1 <= x2) and (x1 + SIZE > x2):
        if (y1 <= y2) and (y1 + SIZE > y2):
            return True
    return False

def play_sound(sound_name):
    # Play a sound effect, given the sound name.
    #sound_name: name of the sound effect (crash, ding, or click)
    global sound
    if sound_name == "crash":
        sound = pygame.mixer.Sound("resources/crash.mp3")
    elif sound_name == "ding":
        sound = pygame.mixer.Sound("resources/ding.mp3")
    if sound_name == "click":
        sound = pygame.mixer.Sound("resources/click.wav")

    pygame.mixer.Sound.play(sound)
    pygame.mixer.music.stop()

def play_background_music():
    #Play the background music.
    pygame.mixer.music.load("resources/bg_music_1.mp3")
    pygame.mixer.music.play(-1, 0)


class EasyGame:
    def __init__(self):
        self.WHITE = None
        self.font_name = None
        self.curr_menu = None
        self.BLACK = None
        self.display = None
        pygame.init()
        pygame.display.set_caption("Snake GAME")
        pygame_icon = pygame.image.load("resources/snakeicon.png")
        pygame.display.set_icon(pygame_icon)

        pygame.mixer.init()
        play_background_music()

        self.surface = pygame.display.set_mode((1000, 800))

        self.player1 = Snake1(self.surface)
        self.player1.draw()
        self.player2 = Snake2(self.surface)
        self.player2.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.poisonapple = PoisonApple(self.surface)
        self.poisonapple.draw()
        self.goldenapple = GoldenApple(self.surface)
        self.goldenapple.draw()

    def reset(self):
        self.player1 = Snake1(self.surface)
        self.player2 = Snake2(self.surface)
        self.apple = Apple(self.surface)
        self.poisonapple = PoisonApple(self.surface)
        self.goldenapple = GoldenApple(self.surface)

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        self.player1.walk()
        self.player2.walk()
        self.apple.draw()
        # self.poisonapple.draw()
        # self.goldenapple.draw()
        self.display_score()
        pygame.display.update()

        # snake1 eating apple scenario
        for i in range(self.player1.length):
            if is_collision(
                self.player1.x[0], self.player1.y[0], self.apple.x, self.apple.y
            ):
                play_sound("ding")
                self.player1.increase_length()
                self.apple.move()
                self.poisonapple.move()

        # snake1 eating poison apple scenario
        for i in range(self.player1.length):
            if is_collision(
                self.player1.x[0],
                self.player1.y[0],
                self.poisonapple.x,
                self.poisonapple.y,):
                play_sound("crash")
                raise RuntimeError("Collision Occurred")

        # snake1 eating golden apple scenario
        for i in range(self.player1.length):
            if is_collision(
                self.player1.x[0],
                self.player1.y[0],
                self.goldenapple.x,
                self.goldenapple.y,
            ):
                play_sound("ding")
                self.player1.increase_length()
                self.apple.move()
                self.poisonapple.move()
                self.goldenapple.move()

        # player1 colliding with the boundaries of the window
        if not (0 <= self.player1.x[0] <= 1000 and 0 <= self.player1.y[0] <= 800):
            play_sound("crash")
            raise RuntimeError("Hit the boundary error")

        # snake2 eating apple scenario
        for i in range(self.player2.length):
            if is_collision(
                self.player2.x[i], self.player2.y[i], self.apple.x, self.apple.y
            ):
                play_sound("ding")
                self.player2.increase_length()
                self.apple.move()
                self.poisonapple.move()

        # snake2 eating poison apple scenario
        for i in range(self.player2.length):
            if is_collision(
                self.player2.x[i],
                self.player2.y[i],
                self.poisonapple.x,
                self.poisonapple.y,
            ):
                play_sound("crash")
                raise RuntimeError("Collision Occurred")

        # snake2 eating golden apple scenario
        for i in range(self.player2.length):
            if is_collision(
                self.player2.x[0],
                self.player2.y[0],
                self.goldenapple.x,
                self.goldenapple.y,
            ):
                play_sound("ding")
                self.player2.increase_length()
                self.apple.move()
                self.poisonapple.move()
                self.goldenapple.move()

        # player2 colliding with the boundaries of the window
        if not (0 <= self.player2.x[0] <= 1000 and 0 <= self.player2.y[0] <= 800):
            play_sound("crash")
            raise RuntimeError("Hit the boundary error")

    def display_score(self):
        self.font_name = None
        font = pygame.font.Font(self.font_name, 70)
        score1 = font.render(f"Score1:  {self.player1.length}", True, (255, 153, 51))
        self.surface.blit(score1, (20, 10))
        score2 = font.render(f"Score2:  {self.player2.length}", True, (102, 0, 102))
        self.surface.blit(score2, (700, 10))

    def show_game_over(self):
        self.render_background()
        self.font0_name = None
        font0 = pygame.font.Font(self.font0_name, 160)
        line0 = font0.render(f"Game is over!", True, (0, 1, 2))
        self.surface.blit(line0, (60, 100))

        self.font_name = None
        font1 = pygame.font.Font(self.font_name, 70)
        line1 = font1.render(f"Score1 is  [{self.player1.length}]", True, (25, 25, 112))
        self.surface.blit(line1, (320, 320))
        line2 = font1.render(f"Score2 is  [{self.player2.length}]", True, (128, 0, 128))
        self.surface.blit(line2, (320, 400))

        self.font2_name = None
        font2 = pygame.font.Font(self.font2_name, 80)
        line3 = font2.render("To play again press Enter.", True, (128, 0, 0))
        self.surface.blit(line3, (30, 540))
        line4 = font2.render("To change level press Escape!", True, (87, 0, 0))
        self.surface.blit(line4, (30, 620))

        pygame.mixer.music.pause()
        pygame.display.update()

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            game = EasyGame()
            game.run()
            # pygame.display.update()
            # self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = (
            False,
            False,
            False,
            False,
        )

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def run(self):
        FPS = 60
        SPEED = 9
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.player1.move_left()

                        if event.key == K_RIGHT:
                            self.player1.move_right()

                        if event.key == K_UP:
                            self.player1.move_up()

                        if event.key == K_DOWN:
                            self.player1.move_down()

                        if event.key == K_a:
                            self.player2.move_left()

                        if event.key == K_d:
                            self.player2.move_right()

                        if event.key == K_w:
                            self.player2.move_up()

                        if event.key == K_s:
                            self.player2.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception:
                self.show_game_over()
                print("Panic!!!")
                pause = True
                self.reset()

            # time.sleep(.1)
            clock.tick(FPS / SPEED)


class MediumGame:
    def __init__(self):
        self.WHITE = None
        self.font_name = None
        self.curr_menu = None
        self.BLACK = None
        self.display = None

        pygame.init()
        pygame.display.set_caption("Snake GAME")
        pygame_icon = pygame.image.load("resources/snakeicon.png")
        pygame.display.set_icon(pygame_icon)

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((1000, 800))

        self.player1 = Snake1(self.surface)
        self.player1.draw()
        self.player2 = Snake2(self.surface)
        self.player2.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.poisonapple = PoisonApple(self.surface)
        self.poisonapple.draw()
        self.goldenapple = GoldenApple(self.surface)
        self.goldenapple.draw()

    def play_background_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        global sound
        if sound_name == "crash":
            sound = pygame.mixer.Sound("resources/crash.mp3")
        elif sound_name == "ding":
            sound = pygame.mixer.Sound("resources/ding.mp3")

        pygame.mixer.Sound.play(sound)
        pygame.mixer.music.stop()

    def reset(self):
        self.player1 = Snake1(self.surface)
        self.player2 = Snake2(self.surface)
        self.apple = Apple(self.surface)
        self.poisonapple = PoisonApple(self.surface)
        self.goldenapple = GoldenApple(self.surface)

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        self.player1.walk()
        self.player2.walk()
        self.apple.draw()
        self.poisonapple.draw()
        # self.goldenapple.draw()
        self.display_score()
        pygame.display.update()

        # snake1 eating apple scenario
        for i in range(self.player1.length):
            if is_collision(
                self.player1.x[0], self.player1.y[0], self.apple.x, self.apple.y
            ):
                self.play_sound("ding")
                self.player1.increase_length()
                self.apple.move()
                self.poisonapple.move()

        # snake1 eating poison apple scenario
        for i in range(self.player1.length):
            if is_collision(
                self.player1.x[0],
                self.player1.y[0],
                self.poisonapple.x,
                self.poisonapple.y,
            ):
                self.play_sound("crash")
                raise RuntimeError("Collision Occurred")

        # snake1 eating golden apple scenario
        for i in range(self.player1.length):
            if is_collision(
                self.player1.x[0],
                self.player1.y[0],
                self.goldenapple.x,
                self.goldenapple.y,
            ):
                self.play_sound("ding")
                self.player1.increase_length()
                self.apple.move()
                self.poisonapple.move()
                self.goldenapple.move()

        # player1 colliding with the boundaries of the window
        if not (0 <= self.player1.x[0] <= 1000 and 0 <= self.player1.y[0] <= 800):
            self.play_sound("crash")
            raise RuntimeError("Hit the boundary error")

        # # player1 colliding with itself
        # for i in range(3, self.player1.length):
        #     if self.is_collision(self.player1.x[0], self.player1.y[0], self.player1.x[i], self.player1.y[i]):
        #         self.play_sound('crash')
        #         raise RuntimeError("Collision Occurred")

        # snake2 eating apple scenario
        for i in range(self.player2.length):
            if is_collision(
                self.player2.x[i], self.player2.y[i], self.apple.x, self.apple.y
            ):
                self.play_sound("ding")
                self.player2.increase_length()
                self.apple.move()
                self.poisonapple.move()

        # snake2 eating poison apple scenario
        for i in range(self.player2.length):
            if is_collision(
                self.player2.x[i],
                self.player2.y[i],
                self.poisonapple.x,
                self.poisonapple.y,
            ):
                self.play_sound("crash")
                raise RuntimeError("Collision Occurred")

        # snake2 eating golden apple scenario
        for i in range(self.player2.length):
            if is_collision(
                self.player2.x[0],
                self.player2.y[0],
                self.goldenapple.x,
                self.goldenapple.y,
            ):
                self.play_sound("ding")
                self.player2.increase_length()
                self.apple.move()
                self.poisonapple.move()
                self.goldenapple.move()

        # # player2 colliding with itself
        # for i in range(3, self.player2.length):
        #     if self.is_collision(self.player2.x[0], self.player2.y[0], self.player2.x[i], self.player2.y[i]):
        #         self.play_sound('crash')
        #         raise RuntimeError("Collision Occurred")

        # player2 colliding with the boundaries of the window
        if not (0 <= self.player2.x[0] <= 1000 and 0 <= self.player2.y[0] <= 800):
            self.play_sound("crash")
            raise RuntimeError("Hit the boundary error")

    def display_score(self):
        self.font_name = None
        font = pygame.font.Font(self.font_name, 70)
        score1 = font.render(f"Score1:  {self.player1.length}", True, (255, 153, 51))
        self.surface.blit(score1, (20, 10))
        score2 = font.render(f"Score2:  {self.player2.length}", True, (102, 0, 102))
        self.surface.blit(score2, (700, 10))

    def show_game_over(self):
        self.render_background()
        self.font0_name = None
        font0 = pygame.font.Font(self.font0_name, 160)
        line0 = font0.render(f"Game is over!", True, (0, 1, 2))
        self.surface.blit(line0, (60, 100))

        self.font_name = None
        font1 = pygame.font.Font(self.font_name, 70)
        line1 = font1.render(f"Score1 is  [{self.player1.length}]", True, (25, 25, 112))
        self.surface.blit(line1, (320, 320))
        line2 = font1.render(f"Score2 is  [{self.player2.length}]", True, (128, 0, 128))
        self.surface.blit(line2, (320, 400))

        self.font2_name = None
        font2 = pygame.font.Font(self.font2_name, 80)
        line3 = font2.render("To play again press Enter.", True, (128, 0, 0))
        self.surface.blit(line3, (30, 540))
        line4 = font2.render("To change level press Escape!", True, (87, 0, 0))
        self.surface.blit(line4, (30, 620))

        pygame.mixer.music.pause()
        pygame.display.update()

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            game = EasyGame()
            game.run()
            # pygame.display.update()
            # self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = (
            False,
            False,
            False,
            False,
        )

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def run(self):
        FPS = 60
        SPEED = 7
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.player1.move_left()

                        if event.key == K_RIGHT:
                            self.player1.move_right()

                        if event.key == K_UP:
                            self.player1.move_up()

                        if event.key == K_DOWN:
                            self.player1.move_down()

                        if event.key == K_a:
                            self.player2.move_left()

                        if event.key == K_d:
                            self.player2.move_right()

                        if event.key == K_w:
                            self.player2.move_up()

                        if event.key == K_s:
                            self.player2.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception:
                self.show_game_over()
                print("Panic!!!")
                pause = True
                self.reset()

            # time.sleep(.1)
            clock.tick(FPS / SPEED)


class HardGame:
    def __init__(self):
        self.WHITE = None
        self.curr_menu = None
        self.BLACK = None
        self.display = None
        self.font_name = None
        pygame.init()
        pygame.display.set_caption("Snake GAME")
        pygame_icon = pygame.image.load("resources/snakeicon.png")
        pygame.display.set_icon(pygame_icon)

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((1000, 800))

        self.player1 = Snake1(self.surface)
        self.player1.draw()
        self.player2 = Snake2(self.surface)
        self.player2.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.poisonapple = PoisonApple(self.surface)
        self.poisonapple.draw()
        self.goldenapple = GoldenApple(self.surface)
        self.goldenapple.draw()

    def play_background_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play(-1, 0)

    def play_sound(self, sound_name):
        global sound
        if sound_name == "crash":
            sound = pygame.mixer.Sound("resources/crash.mp3")
        elif sound_name == "ding":
            sound = pygame.mixer.Sound("resources/ding.mp3")

        pygame.mixer.Sound.play(sound)
        pygame.mixer.music.stop()

    def reset(self):
        self.player1 = Snake1(self.surface)
        self.player2 = Snake2(self.surface)
        self.apple = Apple(self.surface)
        self.poisonapple = PoisonApple(self.surface)
        self.goldenapple = GoldenApple(self.surface)

    def render_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        self.player1.walk()
        self.player2.walk()
        self.apple.draw()
        self.poisonapple.draw()
        self.goldenapple.draw()
        self.display_score()
        pygame.display.update()

        # snake1 eating apple scenario
        for i in range(self.player1.length):
            if is_collision(
                self.player1.x[0], self.player1.y[0], self.apple.x, self.apple.y
            ):
                self.play_sound("ding")
                self.player1.increase_length()
                self.apple.move()
                self.poisonapple.move()

        # snake1 eating poison apple scenario
        for i in range(self.player1.length):
            if is_collision(
                self.player1.x[0],
                self.player1.y[0],
                self.poisonapple.x,
                self.poisonapple.y,
            ):
                self.play_sound("crash")
                raise RuntimeError("Collision Occurred")

        # snake1 eating golden apple scenario
        for i in range(self.player1.length):
            if is_collision(
                self.player1.x[0],
                self.player1.y[0],
                self.goldenapple.x,
                self.goldenapple.y,
            ):
                self.play_sound("ding")
                self.player1.increase_length()
                self.apple.move()
                self.poisonapple.move()
                self.goldenapple.move()

        # Snake1 colliding with the boundaries of the window
        if not (0 <= self.player1.x[0] <= 1000 and 0 <= self.player1.y[0] <= 800):
            self.play_sound("crash")
            raise RuntimeError("Hit the boundary error")

        # Snake2 eating apple scenario
        for i in range(self.player2.length):
            if is_collision(
                self.player2.x[i], self.player2.y[i], self.apple.x, self.apple.y
            ):
                self.play_sound("ding")
                self.player2.increase_length()
                self.apple.move()
                self.poisonapple.move()

        # snake2 eating poison apple scenario
        for i in range(self.player2.length):
            if is_collision(
                self.player2.x[i],
                self.player2.y[i],
                self.poisonapple.x,
                self.poisonapple.y,
            ):
                self.play_sound("crash")
                raise RuntimeError("Collision Occurred")

        # Snake2 eating golden apple scenario
        for i in range(self.player2.length):
            if is_collision(
                self.player2.x[0],
                self.player2.y[0],
                self.goldenapple.x,
                self.goldenapple.y,
            ):
                self.play_sound("ding")
                self.player2.increase_length()
                self.apple.move()
                self.poisonapple.move()
                self.goldenapple.move()

        # Snake2 colliding with the boundaries of the window
        if not (0 <= self.player2.x[0] <= 1000 and 0 <= self.player2.y[0] <= 800):
            self.play_sound("crash")
            raise RuntimeError("Hit the boundary error")

    def display_score(self):
        self.font_name = None
        font = pygame.font.Font(self.font_name, 70)
        score1 = font.render(f"Score1:  {self.player1.length}", True, (255, 153, 51))
        self.surface.blit(score1, (20, 10))
        score2 = font.render(f"Score2:  {self.player2.length}", True, (102, 0, 102))
        self.surface.blit(score2, (700, 10))

    def show_game_over(self):
        self.render_background()
        self.font0_name = None
        font0 = pygame.font.Font(self.font0_name, 160)
        line0 = font0.render(f"Game is over!", True, (0, 1, 2))
        self.surface.blit(line0, (60, 100))

        self.font_name = None
        font1 = pygame.font.Font(self.font_name, 70)
        line1 = font1.render(f"Score1 is  [{self.player1.length}]", True, (25, 25, 112))
        self.surface.blit(line1, (320, 320))
        line2 = font1.render(f"Score2 is  [{self.player2.length}]", True, (128, 0, 128))
        self.surface.blit(line2, (320, 400))

        self.font2_name = None
        font2 = pygame.font.Font(self.font2_name, 80)
        line3 = font2.render("To play again press Enter.", True, (128, 0, 0))
        self.surface.blit(line3, (30, 540))
        line4 = font2.render("To change level press Escape!", True, (87, 0, 0))
        self.surface.blit(line4, (30, 620))

        pygame.mixer.music.pause()
        pygame.display.update()

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            game = EasyGame()
            game.run()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = (
            False,
            False,
            False,
            False,
        )

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def run(self):
        FPS = 60
        SPEED = 6
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.player1.move_left()

                        if event.key == K_RIGHT:
                            self.player1.move_right()

                        if event.key == K_UP:
                            self.player1.move_up()

                        if event.key == K_DOWN:
                            self.player1.move_down()

                        if event.key == K_a:
                            self.player2.move_left()

                        if event.key == K_d:
                            self.player2.move_right()

                        if event.key == K_w:
                            self.player2.move_up()

                        if event.key == K_s:
                            self.player2.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception:
                self.show_game_over()
                print("Panic!!!")
                pause = True
                self.reset()

            # time.sleep(.1)
            clock.tick(FPS / SPEED)


class Menu:
    pygame.init()
    play_background_music()
    pygame.display.set_caption("Snake GAME")
    pygame_icon = pygame.image.load("resources/snakeicon.png")
    pygame.display.set_icon(pygame_icon)
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_paused = False
    menu_state = "main"

    # define fonts
    font = pygame.font.SysFont("arialblack", 40)

    # define colours
    TEXT_COL = (255, 255, 255)

    # load button images
    start_img = pygame.image.load("images/button_start.png").convert_alpha()
    credits_img = pygame.image.load("images/button_options.png").convert_alpha()
    quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
    easy_img = pygame.image.load("images/button_easy.png").convert_alpha()
    medium_img = pygame.image.load("images/button_medium.png").convert_alpha()
    hard_img = pygame.image.load("images/button_hard.png").convert_alpha()
    back_img = pygame.image.load("images/button_back.png").convert_alpha()
    adifirazsnake_img = pygame.image.load("images/adifiraz.png").convert_alpha()
    main_image = pygame.image.load("images/main.jpg").convert_alpha()

    # create button instances
    main_button = button.Button(0, 0, main_image, 1)
    start_button = button.Button(400, 300, start_img, 1)
    credits_button = button.Button(390, 400, credits_img, 1)
    quit_button = button.Button(430, 500, quit_img, 1)

    easy_button = button.Button(400, 300, easy_img, 1)
    medium_button = button.Button(400, 400, medium_img, 1)
    hard_button = button.Button(400, 500, hard_img, 1)
    back_button = button.Button(800, 600, back_img, 1)

    credit_button = button.Button(0, 100, adifirazsnake_img, 1)

    run = True
    while run:
        screen.fill((52, 70, 91))
        if not game_paused:
            main_button.draw(screen)
            if menu_state == "main":
                # draw pause screen buttons
                if start_button.draw(screen):
                    play_sound("click")
                    menu_state = "start"
                elif credits_button.draw(screen):
                    play_sound("click")
                    menu_state = "credits"
                elif quit_button.draw(screen):
                    play_sound("click")
                    play_sound("click")
                    play_sound("click")
                    run = False

            if menu_state == "start":
                if easy_button.draw(screen):
                    play_sound("click")
                    game = EasyGame()
                    game.run()
                    print("easy")
                elif medium_button.draw(screen):
                    play_sound("click")
                    game = MediumGame()
                    game.run()
                    print("medium")
                elif hard_button.draw(screen):
                    play_sound("click")
                    game = HardGame()
                    game.run()
                    print("hard")
                elif back_button.draw(screen):
                    play_sound("click")
                    menu_state = "main"

                if menu_state == "credits":
                    play_sound("click")
                    if back_button.draw(screen):
                        play_sound("click")
                        menu_state = "main"
            if menu_state == "credits":
                credit_button.draw(screen)
                if back_button.draw(screen):
                    play_sound("click")
                    menu_state = "main"

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = True
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


# The following code checks if the script is being run as the main program
# If the script is being run as the main program, the value of __name__ is set to "__main__"
if __name__ == "__main__":
    # If the script is being run as the main program, the Menu() function is called
    Menu()

\n