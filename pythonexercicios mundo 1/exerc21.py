import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Maid with the Flaxen Hair.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
