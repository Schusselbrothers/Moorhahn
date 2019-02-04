import pygame, sys                                                         
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([640,480])
mein_rect = pygame.Rect(1, 350, 750, 200)
hintergrund = pygame.Surface(screen.get_size())                             
hintergrund.fill([255, 255, 255])                                           
uhr = pygame.time.Clock()                                           
pygame.mouse.set_cursor(*pygame.cursors.diamond)
GETROFFEN = pygame.mixer.Sound("sfx_big_chicken_shot.wav")
shoot_sound = pygame.mixer.Sound("shoot.wav")
reload_sound = pygame.mixer.Sound("reload2.wav")
reload2_sound = pygame.mixer.Sound("reload.wav")
pygame.display.set_caption("Moorhahn")
class Ball(pygame.sprite.Sprite):                                          
   def __init__(self, bild_datei, geschwindigkeit, ort):                        
        pygame.sprite.Sprite.__init__(self) # ruft Sprite-Initialisierer auf       
        self.image = pygame.image.load(bild_datei)                         
        self.rect = self.image.get_rect()                                  
        self.rect.left, self.rect.top = ort                           
        self.geschwindigkeit = geschwindigkeit                                                 
 
   def bewegen(self):                                                         
        if self.rect.left <= screen.get_rect().left or \
                 self.rect.right >= screen.get_rect().right:               
            self.geschwindigkeit[0] = - self.geschwindigkeit[0]                                
        neue_position = self.rect.move(self.geschwindigkeit)                                
        self.rect = neue_position


      
 
mein_ball = Ball('moorhahn2.png', [15,0], [20, 20])  
background = pygame.image.load("bg.jpeg")                       
group = pygame.sprite.Group(mein_ball)
pygame.time.set_timer(pygame.USEREVENT, 1000)                              
richtung = 1   
punkte = 0
point_font = pygame.font.Font(None,70)
point_font2 = pygame.font.Font(None,30)
point_font3 = pygame.font.Font(None,30)
pfont = point_font.render(str(punkte),1,(255,0,0))
ammof = point_font2.render(str(12)+"/12",1,(255,0,0))
timef = point_font2.render(str("Countdown: 60"),1,(255,0,0))
aktiv = True     
ammo = 40
ammo_range  = 40
run_sound = False  
hold = False    
passiv_delay = 0    
mode = "semi"
clock = pygame.time.Clock()
timer = 60
thetime = 60
dt = 0
mode_font = point_font2.render("Mode: "+mode,1,(255,0,0)) 
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)             
the_alert = False      
countpuls = False
puls = 30
reload_font = point_font2.render("Reloading...",1,(255,0,0))
while aktiv:                                                                   
    for ereignis in pygame.event.get():                                       
        if ereignis.type == pygame.QUIT:                                      
            aktiv = False                                                   
        elif ereignis.type == pygame.USEREVENT:                               
            mein_ball.rect.centery = mein_ball.rect.centery + (30 * richtung) 
            if mein_ball.rect.top <= 0 or  \
                    mein_ball.rect.bottom >= screen.get_rect().bottom:               
                richtung = -richtung 
	elif ereignis.type == pygame.MOUSEBUTTONDOWN:
		mouse = ereignis.pos
		if not run_sound:
			
			if ammo != 0:
				ammo -= 1
			else:
				run_sound = True
				reload_sound.play()
				continue
			shoot_sound.play()
			#if screen.get_at(mouse) != (255,255,255) and screen.get_at(mouse) != (0,255,0):
			if mein_ball.rect.collidepoint(mouse) and screen.get_at(mouse) != (255,255,255) and screen.get_at(mouse) != (0,255,0):
				GETROFFEN.play() 
				punkte += 1
				pfont = point_font.render(str(punkte),1,(255,0,0))
			pygame.draw.circle(screen,(255,0,0),mouse,20)    
			pygame.display.flip()
			ammof = point_font2.render(str(str(ammo)+"/"+str(ammo_range)),1,(255,0,0))
			if mode == "auto":
				hold = True
	elif ereignis.type == pygame.MOUSEBUTTONUP:
		hold = False
	elif ereignis.type == pygame.KEYDOWN:
		if ereignis.key == pygame.K_SPACE:
			if mode == "semi":
				mode = "auto"
			else:
				mode = "semi"
			mode_font = point_font2.render("Mode: "+mode,1,(255,0,0))
	if hold:
			passiv_delay += 1
			if passiv_delay == 5:
				try:
					mouse = ereignis.pos
				except:
					pass
				if not run_sound:
					
					if ammo != 0:
						ammo -= 1
					else:
						run_sound = True
						reload_sound.play()
						continue
					shoot_sound.play()
					#if screen.get_at(mouse) != (255,255,255) and screen.get_at(mouse) != (0,255,0):
					if mein_ball.rect.collidepoint(mouse) and screen.get_at(mouse) != (255,255,255) and screen.get_at(mouse) != (0,255,0):
						GETROFFEN.play() 
						punkte += 1
						pfont = point_font.render(str(punkte),1,(255,0,0))
					pygame.draw.circle(screen,(255,0,0),mouse,20)    
					pygame.display.flip()
					ammof = point_font2.render(str(str(ammo)+"/"+str(ammo_range)),1,(255,0,0))
					passiv_delay = 0
    if hold:
			passiv_delay += 1
			if passiv_delay == 5:
				try:
					mouse = ereignis.pos
				except:
					pass
				if not run_sound:
					
					if ammo != 0:
						ammo -= 1
					else:
						run_sound = True
						reload_sound.play()
						continue
					shoot_sound.play()
					#if screen.get_at(mouse) != (255,255,255) and screen.get_at(mouse) != (0,255,0):
					if mein_ball.rect.collidepoint(mouse) and screen.get_at(mouse) != (255,255,255) and screen.get_at(mouse) != (0,255,0):
						GETROFFEN.play() 
						punkte += 1
						pfont = point_font.render(str(punkte),1,(255,0,0))
					pygame.draw.circle(screen,(255,0,0),mouse,20)    
					pygame.display.flip()
					ammof = point_font2.render(str(str(ammo)+"/"+str(ammo_range)),1,(255,0,0))
					passiv_delay = 0
    if run_sound:
	if not pygame.mixer.get_busy():
		reload2_sound.play()
		run_sound = False
		ammo = ammo_range
		ammof = point_font2.render(str(str(ammo)+"/"+str(ammo_range)),1,(255,0,0))
		passiv_delay = 0

    if ammo == 0 and not run_sound:
		run_sound = True
	        reload_sound.play()
    if countpuls:
	if puls >=  50:
		puls = 30
	else:
		puls += 1
	point_font3 = pygame.font.Font(None,puls)
    timer -= dt
    dt = round(clock.tick(30),2)/10
    uhr.tick(30)      
    thetime -= int(timer - timer - timer / 100)
    timef = point_font3.render(str("Countdown: ")+str(thetime),1,(255,0,0))
    if thetime == 5 and not the_alert:
	the_alert = True
	countpuls = True
    if thetime == 0:
        if punkte >= 600:
		end_font = point_font.render("You win",1,(0,255,0))
	else:
		end_font = point_font.render("You loose",1,(255,0,0))
	while True:
		screen.blit(end_font,[20,180])
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
    thetime = 60                                          
    screen.blit(hintergrund, (0, 0))
    screen.blit(background,[0,0])
    screen.blit(mein_ball.image, mein_ball.rect)
    screen.blit(timef,[230,430])
    screen.blit(pfont,[10,10])    
    screen.blit(ammof,[500,10])                 
    screen.blit(mode_font,[250,10])   
    if run_sound:
	screen.blit(reload_font,(250,400))                
    mein_ball.bewegen()                                                         
    #pygame.draw.rect(screen, [0,255,0], mein_rect, 0)
    pygame.display.flip() 
    
pygame.quit()    

