import pygame,sys

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.sw, self.sh = width, height
        self.scr = pygame.display.set_mode((self.sw, self.sh))
        self.clock = pygame.time.Clock()
    
    def draw_text(self, txt, font_size, x, y):
        text = pygame.font.SysFont(None, font_size).render(txt, True, (255,255,255))
        self.scr.blit(text,(x,y))
    
    def draw_button(self, txt, x, y, w, h):
        pygame.draw.rect(self.scr, (255,0,0), (x,y,w,h))
        self.draw_text(txt, 20, x+w//2-15, y+h//2-10)

    def main_menu(self):
        button_x, button_y, button_w, button_h = 330, 200, 140, 40
        while True:
            self.scr.fill((0,0,0))
            self.draw_text('Main Menu', 40, 20, 20)
            mouse_x, mouse_y = pygame.mouse.get_pos()  
            button1 = pygame.Rect(button_x, button_y, button_w, button_h)
            button2 = pygame.Rect(button_x, button_y + 60, button_w, button_h)
            button3 = pygame.Rect(button_x, button_y + 120, button_w, button_h)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.collidepoint((mouse_x, mouse_y)): 
                        self.start()
                    if button2.collidepoint((mouse_x, mouse_y)): 
                        self.help()
                    if button3.collidepoint((mouse_x, mouse_y)): 
                        pygame.quit()
                        sys.exit()
            
            self.draw_button('Start', button_x, button_y, button_w, button_h)
            self.draw_button('Help', button_x, button_y + 60, button_w, button_h)
            self.draw_button('Quit', button_x, button_y + 120, button_w, button_h)
            pygame.display.update()
            self.clock.tick(60)

    def start(self):
        running = True
        blck_x, blck_y = self.sw//2, self.sh//2
        while running:
            self.scr.fill((0,0,0))
            self.draw_text("GAME ON!!!", 40, 20, 20)
            self.draw_text("PRESS ESCAPE TO VISIT MAIN MENU", 20, 20, self.sh-20)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                blck_y -= 10
            if keys[pygame.K_DOWN]:
                blck_y += 10
            if keys[pygame.K_LEFT]:
                blck_x -= 10
            if keys[pygame.K_RIGHT]:
                blck_x += 10

            pygame.draw.rect(self.scr, (255,0,0), (blck_x, blck_y, 20, 20))
            pygame.display.update()
            self.clock.tick(60)
    
    def help(self):
        pass

    def run(self):
        self.main_menu()
                    
if __name__ == "__main__":
    game = Game(800, 600)
    game.run()
