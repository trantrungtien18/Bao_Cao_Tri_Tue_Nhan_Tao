import pygame

# Pygame sound init
pygame.mixer.pre_init(44100, -16, 2, 2)
pygame.mixer.init()
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 2)

swimmingSound = pygame.mixer.Sound("./audio/Swimming.mp3")
themeSound = pygame.mixer.Sound("./audio/Theme.mp3")
winSound = pygame.mixer.Sound("./audio/Win.wav")