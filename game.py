import pygame, logging

import bullet, player, textures
from bullet import Bullet
from player import Shooter
from textures import Textures
from target import Target


PLAYING_GAME = False
WINDOW_SIZE = (640,480)
FPS = 120

def rounding(x, base): return int(base * round(float(x)/base))


def initialise(menu, options):
	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.init()
	window = pygame.display.set_mode(WINDOW_SIZE)

	exit_code = play(window) # Run main game loop
	if exit_code = 
	pygame.quit()
	# Reshow the main menu


def generate_targets():
    group = pygame.sprite.Group()
    target_object = Target()
    for i in range(10,150,50):
        for j in range(10, 150, 50):
            temp = Target()
            logging.debug("Target generated with position ({},{})".format(j,i))
            temp.set_position(j,i)
            group.add(temp)
            del temp
    return group
        

def play(window):
	window_rect = window.get_rect()

	player = Shooter(window=window)
	player.set_position(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]*0.93)
	player_group = pygame.sprite.Group()
	player_group.add(player)
	player_group.draw(window)

	target_group = generate_targets()
	bullet_group = pygame.sprite.Group()

	clock = pygame.time.Clock()
	PLAYING_GAME = True

	while PLAYING_GAME:
		window.fill((0,0,0))
		player_group.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				logging.critical("Exiting Game...")
				PLAYING_GAME = False
				return "QUIT"

			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				temp = Bullet(player)
				bullet_group.add(temp)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			player.move(player.speed)

		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			player.move(-player.speed)

		if keys[pygame.K_KP4] and keys[pygame.K_KP5] and keys[pygame.K_KP6]:
			temp = Bullet(player)
			bullet_group.add(temp)

		for sprite in bullet_group:
			if not sprite.at_top():
				sprite.update()
			if sprite.rect.y < 0:
				bullet_group.remove(sprite)

		for bullet in bullet_group:
			hit_list = pygame.sprite.spritecollide(bullet, target_group, True)
			for target in hit_list:
				target_group.remove(target)
				bullet_group.remove(bullet)
				logging.info("Hit Target!")

		player_group.update()
		bullet_group.draw(window)
		target_group.draw(window)
		player_group.draw(window)
		pygame.display.update()
		clock.tick(FPS)


if __name__ == "__main__":
	initialise(None, None)
