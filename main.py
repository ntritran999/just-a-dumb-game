import pygame,sys

class Game:
    red = (255,0,0)
    blue = (0,0,255)
    white = (255, 255, 255)
    black = (0,0,0)

    def __init__(self, width, height):
        pygame.init()
        self.sw, self.sh = width, height
        self.scr = pygame.display.set_mode((self.sw, self.sh))
        self.clock = pygame.time.Clock()
    
    def draw_text(self, txt, font_size, x, y):
        text = pygame.font.SysFont(None, font_size).render(txt, True, (self.white))
        self.scr.blit(text,(x,y))
    
    def draw_button(self, color, txt, x, y, w, h):
        pygame.draw.rect(self.scr, color, (x,y,w,h))
        self.draw_text(txt, 20, x+w//2-15, y+h//2-10)

    def main_menu(self):
        button_x, button_y, button_w, button_h = 330, 200, 140, 40
        while True:
            self.scr.fill(self.black)
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
            
            self.draw_button(self.red, 'Start', button_x, button_y, button_w, button_h)
            self.draw_button(self.red, 'Help', button_x, button_y + 60, button_w, button_h)
            self.draw_button(self.red, 'Quit', button_x, button_y + 120, button_w, button_h)
            pygame.display.update()
            self.clock.tick(60)

    def start(self):
        running = True
        blck_x, blck_y = self.sw//2, self.sh//2
        self.scr.fill(self.black)
        while running:
            self.draw_text("GAME ON!!!", 40, 20, 20)
            self.draw_text("PRESS ESCAPE TO VISIT MAIN MENU", 20, 20, self.sh-20)
            clean_button = pygame.Rect(20, self.sh-80, 140, 40)
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if clean_button.collidepoint((mouse_x, mouse_y)):
                        self.scr.fill(self.black)
                        blck_x, blck_y = self.sw//2, self.sh//2

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                blck_y -= 10
            if keys[pygame.K_DOWN]:
                blck_y += 10
            if keys[pygame.K_LEFT]:
                blck_x -= 10
            if keys[pygame.K_RIGHT]:
                blck_x += 10

            self.draw_button(self.blue, 'CLEAN', 20, self.sh-80, 140, 40)
            pygame.draw.rect(self.scr, self.red, (blck_x, blck_y, 20, 20))
            pygame.display.update()
            self.clock.tick(60)
    
    def help(self):
        running = True
        while running:
            self.scr.fill(self.black)
            self.draw_text("PRESS ESCAPE TO VISIT MAIN MENU", 20, 20, self.sh-20)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            self.draw_text("This is a drawing game.", 40, 50, 100)
            self.draw_text("You can click 'CLEAN' button to clean the screen.", 40, 50, 150)

            pygame.display.update()
            self.clock.tick(60)

    def run(self):
        self.main_menu()
                    
if __name__ == "__main__":
    game = Game(800, 600)
    game.run()
