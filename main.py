import pygame,sys

pygame.init()

#------COLORS-------
red = (255,0,0)
blue = (0,0,255)
white = (255, 255, 255)
black = (0,0,0)

#----SCREEN SET UP-------
sw, sh = (800, 600) # Resolution
scr = pygame.display.set_mode((sw, sh))

#----FPS----
FPS = pygame.time.Clock()

#---DRAW SOME TEXTS ONTO THE SCREEN----    
def draw_text(txt, font_size, x, y):
    text = pygame.font.SysFont(None, font_size).render(txt, True, (white))
    scr.blit(text,(x,y))

#----DRAW BUTTON AND ADD TEXT INTO IT----  
def draw_button(color, x, y, w, h, txt=None): # YOU CAN CHOOSE TO ADD TEXT OR NOT
    pygame.draw.rect(scr, color, (x,y,w,h))
    if txt != None:
        draw_text(txt, 20, x+w//2-15, y+h//2-10)


#----------MAIN MENU---------
def main_menu():
    button_x, button_y, button_w, button_h = 25, 80, 140, 40
    while True:
        scr.fill(black)
        draw_text('Main Menu', 40, 20, 20)
        mouse_x, mouse_y = pygame.mouse.get_pos()  
        button1 = pygame.Rect(button_x, button_y, button_w, button_h)
        button2 = pygame.Rect(button_x, button_y + 60, button_w, button_h)
        button3 = pygame.Rect(button_x, button_y + 120, button_w, button_h)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint((mouse_x, mouse_y)): 
                    start()
                if button2.collidepoint((mouse_x, mouse_y)): 
                    help()
                if button3.collidepoint((mouse_x, mouse_y)): 
                    quit()
        
        draw_button(red, button_x, button_y, button_w, button_h, 'Start')
        draw_button(red, button_x, button_y + 60, button_w, button_h, 'Help')
        draw_button(red, button_x, button_y + 120, button_w, button_h, 'Quit')
        pygame.display.update()
        FPS.tick(60)

def start():
    running = True
    blck_x, blck_y = sw//2, sh//2
    scr.fill(black)
    while running:
        draw_text("GAME ON!!!", 40, 20, 20)
        draw_text("PRESS ESCAPE TO VISIT MAIN MENU", 20, 20, sh-20)
        clean_button = pygame.Rect(20, sh-80, 140, 40)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if clean_button.collidepoint((mouse_x, mouse_y)):
                    scr.fill(black)
                    blck_x, blck_y = sw//2, sh//2

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            blck_y -= 10
        if keys[pygame.K_DOWN]:
            blck_y += 10
        if keys[pygame.K_LEFT]:
            blck_x -= 10
        if keys[pygame.K_RIGHT]:
            blck_x += 10

        draw_button(blue, 20, sh-80, 140, 40, 'CLEAN')
        pygame.draw.rect(scr, red, (blck_x, blck_y, 20, 20))
        pygame.display.update()
        FPS.tick(60)

def help():
    running = True
    while running:
        scr.fill(black)
        draw_text("PRESS ESCAPE TO VISIT MAIN MENU", 20, 20, sh-20)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        draw_text("This is a drawing game.", 40, 50, 100)
        draw_text("You can click 'CLEAN' button to clear the screen.", 40, 50, 150)

        pygame.display.update()
        FPS.tick(60)

def quit():
    pygame.quit()
    sys.exit()
                
if __name__ == "__main__":
    main_menu()
