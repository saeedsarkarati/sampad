import pygame
from pygame.locals import *
pygame.init()
s1 = pygame.image.load('Ejei.jpg')
lx, ly = (400, 500)
ll = 20
np = ll * ll
nx, ny = (lx // ll , ly // ll)
s2 = pygame.Surface((lx, ly))
s2.blit (s1, (0, 0), (200,0,lx, ly) )
pygame.image.save(s2, 'Ej1.png')
# ~ ---------------------
s3 = pygame.Surface((lx, ly))
s4 = pygame.Surface((lx, ly))
for i in range(nx):
	for j in range (ny):
		x1 = i * nx
		y1 = j * nx
		x2 = x1 + ll
		y2 = y1 + ll
		rt = gt = bt = zt =0
		for ix in range (ll):
			for iy in range (ll):
				x = x1 + ix
				y = y1 + iy
				r, g, b, z = s2.get_at ((x, y))
				rt += r; gt += g; bt += b
		rt //= np; gt //= np; bt //= np; 
		print (rt, gt, bt)
		pygame.draw.rect(s3, (rt, gt, bt), (x1, y1, ll, ll) )
		pygame.draw.circle(s4, (rt, gt, bt), (x1 + ll // 2, y1 + ll // 2) , ll//2 )
pygame.image.save(s3, 'Ej2.png')
pygame.image.save(s4, 'Ej3.png')
