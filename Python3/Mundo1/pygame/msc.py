import pygame

pygame.mixer.init()
pygame.mixer.music.load('msc.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
