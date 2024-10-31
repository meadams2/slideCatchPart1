"""Marianne Adams
CS120
Slide and Catch Part 1"""
import pygame, simpleGE
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("FallScene.png")
        
        self.sprites = []

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()