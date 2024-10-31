# CS120 Slide and Catch Part 1

The goal of this project is to use a simple game engine to create a slide and catch game. The idea of the game is to create a game where Wednesday (my cat) catches leaves in a fall scene. To score, Wednesday needs to move to collide with the leaves. A sound will play when Wednesday collides with the leaf.

# Milestone 1: Scene 

Define a new class called Game. Game takes simpleGE.Scene. Add the "FallScene.png" image. Background image is a picture taken while I was hiking on October 24, 2022 in Legion Park. 

# Milestone 2: Wednesday 

Define a new class called Wednesday. Wednesday takes simpleGE.Sprite. Add the "Wednesday.png" image. Image is of my cat, and was taken December 2023. Set size to 75 x 75 and set position to 320 x 400. Define movement speed to be 5 pixels per frame. 

Define a new process to check if the left or right arrow keys are pressed. If the left arrow key is pressed, the x value is the previous x value minus the movement speed. If the right arrow key is pressed, the x value is the previous x value added to the movement speed. 

Update Game class and add Wednesday to the Game schema. Add Wednesday to the list of sprites. 

# Milestone 3: Leaf

Define a new class called Leaf. Leaf takes simpleGE.Sprite. Add the "FallLeaf.png" image. Image is from https://openclipart.org/detail/257622/leaf by NicholasJudy456. Set size to 30 x 30. Define minimum speed as 3 pixels per frame. Define maximum speed as 8 pixels per frame. 

Define new method called reset. Reset takes self. The x position of the leaf gets a random integer from 0 to the screen width. The y position of the leaf gets 0. The leaf speed (self.dy) gets a random integer between the minimum speed and the maximum speed. Add reset method to __init__().

Define a new method called checkBounds. checkBounds takes self. If the bottom is greater than the screen height, reset(). 

Update Game class and add Leaf to Game schema. Add leaf to the list of sprites. 

# Milestone 4: Collision
