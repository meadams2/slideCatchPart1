"""Marianne Adams
CS120 Slide-Catch Part 1
Blackbelt"""

import pygame, simpleGE, random

class Wednesday (simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Wednesday.png")
        self.setSize(75, 75)
        self.position = (320, 400)
        self.moveSpeed = 5
    
    def process(self):
        if self.isKeyPressed(pygame.K_UP):
#             self.checkBounds()
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_DOWN):
#             self.checkBounds()
            self.y += self.moveSpeed
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            
class Leaf(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("FallLeaf.png")
        self.setSize(30, 30)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
    
    def reset(self):
        self.x = random.randint(0, self.screenWidth)
        self.y = 0
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("FallScene.png")
        self.sndLeaf = simpleGE.Sound("leafCatch.wav")
        self.wednesday = Wednesday(self)
        self.leaves = []
        for i in range(10):
            self.leaves.append(Leaf(self))
        
        self.sprites = [self.wednesday, self.leaves]
        
    def process(self):
        for leaf in self.leaves:
            if self.wednesday.collidesWith(leaf):
                self.sndLeaf.play()
                leaf.reset()
    
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
    