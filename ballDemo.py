import pygame, sys
from Ball import Ball

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

ball1 = Ball("ball.png", [4,5], [100, 125])
ball2 = Ball("ball.png", [6,5], [250, 225])
ball3 = Ball("ball.png", [5,5], [450, 225])
ball4 = Ball("ball.png", [3,5], [450, 535])

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		
	ball1.update(width, height)
	ball2.update(width, height)
	ball3.update(width, height)
	ball4.update(width, height)
	
	ball1.collideBall(ball2)
	ball1.collideBall(ball3)
	ball1.collideBall(ball4)
	
	ball2.collideBall(ball1)
	ball2.collideBall(ball3)
	ball2.collideBall(ball4)
	
	ball3.collideBall(ball1)
	ball3.collideBall(ball2)
	ball3.collideBall(ball4)
	
	ball4.collideBall(ball1)
	ball4.collideBall(ball2)
	ball4.collideBall(ball3)
	
	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(ball1.image, ball1.rect)
	screen.blit(ball2.image, ball2.rect)
	screen.blit(ball3.image, ball3.rect)
	screen.blit(ball4.image, ball4.rect)
	pygame.display.flip()
	clock.tick(60)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
