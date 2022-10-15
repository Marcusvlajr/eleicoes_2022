'''Faça um programa em python que abra e reproduza o audio de um arquivo mp3.'''
'''Pra realizar esse exercicio, sera necessario baixar uma musica mp3.( criar uma pasta pra mesma 'ex021.mp3').'''

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
