import pygame

from dino_runner.utils.constants import (
    FND,
    BG,
    ICON,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,
    FPS,
    DEFAULT_TYPE,
    RUNNING,
)
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

FONT_STYLE = "freesansbold.ttf"


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.score = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def template_text(self, text_data, color, position):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(text_data, True, color)
        text_rect = text.get_rect()
        text_rect.center = position
        self.screen.blit(text, text_rect)

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        pygame.mixer.music.play(-1)
        self.score = 0
        self.game_speed = 20
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()

        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.blit(FND, (0, 0))
        # fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        self.template_text(f"Score: {self.score}", (0, 0, 0), (1000, 50))

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round(
                (self.player.power_up_time - pygame.time.get_ticks()) / 1000, 1
            )
            if time_to_show >= 0:
                self.template_text(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    (0, 0, 0),
                    (500, 40),
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def show_menu(self):
        pygame.mixer.music.stop()
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.template_text(
                "Press any key to start",
                (0, 0, 0),
                (half_screen_width, half_screen_height),
            )

        else:  ## tela de restart      #    x                              y
            self.screen.blit(ICON, (half_screen_width - 40, half_screen_height - 110))
            if self.death_count == 1:
                self.template_text(
                    'You were from "F"',
                    (0, 0, 0),
                    (half_screen_width, half_screen_height + 60),
                )
                self.template_text(
                    "Press any key to restart",
                    (0, 0, 0),
                    (half_screen_width, half_screen_height),
                )
                self.template_text(
                    f"Score achieved: {self.score}",
                    (225, 0, 0),
                    (half_screen_width, half_screen_height - 150),
                )
            elif self.death_count == 2:
                self.template_text(
                    'You were from "F" twice',
                    (0, 0, 0),
                    (half_screen_width, half_screen_height + 60),
                )
                self.template_text(
                    f"Score achieved: {self.score}",
                    (225, 0, 60),
                    (half_screen_width, half_screen_height - 150),
                )
                self.template_text(
                    "Press any key to restart",
                    (0, 0, 0),
                    (half_screen_width, half_screen_height),
                )
            else:
                self.template_text(
                    f'You were from "F" {self.death_count} times',
                    (0, 0, 0),
                    (half_screen_width, half_screen_height + 60),
                )
                self.template_text(
                    f"Score achieved: {self.score}",
                    (225, 0, 0),
                    (half_screen_width, half_screen_height - 150),
                )
                self.template_text(
                    "Press any key to restart",
                    (0, 0, 0),
                    (half_screen_width, half_screen_height),
                )
            ## mostrar mensagem de "Press any key to restart"
            ## mostrar o score atingido
            ## mostrar death_count

            ### Resetar score e game_speed quando uma nova partida for iniciada
            ### Criar método para remover a repetição de código para o texto

        pygame.display.update()
        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()
