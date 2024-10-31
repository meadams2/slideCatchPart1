"""Marianne Adams
CS120
Slide and Catch Part 1"""
import pygame, simpleGE
class Wednesday(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Wednesday.png")
        self.setSize(75, 75)
        self.position = (320, 400)
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("FallScene.png")
        self.wednesday = Wednesday(self)
        self.sprites = [self.wednesday]

def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()