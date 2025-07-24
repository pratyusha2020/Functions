import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT= 500,500

display_surface= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding image and background image")

background_image= pygame.transform.scale(pygame.image.load('Bac.jpg').convert(),(SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image= pygame.transform.scale(pygame.image.load('aang.jpg').convert_alpha(), (300,300))

penguin_rect= penguin_image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2-30))

text= pygame.font.Font(None, 36).render('My second game screen # Pygame', True, pygame.Color('white'))
text_rect= text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+150))
def game_loop():
    clock= pygame.time.Clock()
    running= True
    while running:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                running= False

        display_surface.blit(background_image,(0,0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__== '__main__':
    game_loop()

#I wanted to branch out from the hw instructions, and experiment w/ different things