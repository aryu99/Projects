# program template for Spaceship
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random

# globals for user interface 
WIDTH = 800 
HEIGHT = 600 
score = 0 
lives = 3 
time = 0 
started = False 
high_score = 0

def restart():
    global started, rock_group, missile_group, score, lives
    lives = 3
    score = 0
    rock_group = set()
    missile_group = set()
    # started = False
    soundtrack.rewind()



def group_group_collide(group_1, group_2):
    for sprite in set(group_1):
        if group_collide(sprite, group_2):
            group_1.remove(sprite)
            return True



def group_collide(other_object, group):
    for sprite in set(group):
        if sprite.collision(other_object):
            group.remove(sprite)
            return True
        


# go through set and draw + update each sprite element
def process_sprite_group(canvas, sprite_set):
    for sprite in set(sprite_set):
        # sprite.update()
        if sprite.update():
            sprite_set.remove(sprite)
        sprite.draw(canvas)
    # for sprite in set(sprite_set):

        # sprite.collision(my_ship)


class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
   
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.shoot = False  
        
    def draw(self,canvas):
        if self.thrust == False:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, (130, 45), self.image_size, self.pos, self.image_size, self.angle)


    def angle_velinc(self):
            self.angle_vel += 0.1
    def angle_veldec(self):
            self.angle_vel -= (0.1)

    def update(self):
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH 
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.angle += self.angle_vel
        self.vel[0] *= (1-0.008)
        self.vel[1] *= (1-0.008)
        if self.thrust == True:
            self.vel[0] += (0.1*(angle_to_vector(self.angle))[0])
            self.vel[1] += (0.1*(angle_to_vector(self.angle))[1])
            



    def thrust_val(self):
        if self.thrust == False:
            self.thrust = True
            ship_thrust_sound.play()
            
        else:
            self.thrust = False
            ship_thrust_sound.rewind()
            

        # print (self.thrust)

    def missile(self):
        global missile_group
        a_missile = Sprite([self.pos[0] + ((angle_to_vector(self.angle))[0]*self.radius), self.pos[1] + ((angle_to_vector(self.angle))[1]*self.radius)],
                            [((angle_to_vector(self.angle))[0])*6 + self.vel[0],((angle_to_vector(self.angle))[1])*6 + self.vel[1]], 
                            self.angle, self.angle_vel, missile_image, missile_info, missile_sound)

        if self.shoot == False:
            self.shoot = True
            missile_sound.play()
            missile_group.add(a_missile)

        else:
            self.shoot = False  
            missile_sound.rewind()
        
   
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        # if my_ship.shoot:
        #     canvas.draw_image(asteroid_image, self.image_center, self.image_size, self.pos, self.image_center, self.angle)

    
    def update(self):
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH 
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT 
        self.angle += self.angle_vel
        self.age += 1
        if self.age >= self.lifespan:
            return True
        else:
            return False

    #method to determine collision between sprite and other object
    def collision(self, other_object):
        global lives
        min_dist = self.radius + other_object.radius
        if dist(self.pos, other_object.pos) < min_dist:
            # print ("Collision True")
            return True

        else:
            # print ("collision False")
            return False
            



def click(pos):
    global started
    started = True
    restart()
    soundtrack.play()

           
def draw(canvas):
    global time, lives, score, started, high_score
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    # a_rock.draw(canvas)
    # a_missile.draw(canvas)
    process_sprite_group(canvas, rock_group)
    process_sprite_group(canvas, missile_group)
    if group_collide(my_ship, rock_group):
        if lives >= 1:
            lives -= 1

    if lives < 1:
        # restart()
        started = False

    if group_group_collide(rock_group, missile_group):
        score += 1

    if score > high_score:
        high_score = score


    
    # update ship and sprites
    my_ship.update()
    # a_rock.update()
    # a_missile.update()

    # Draw lives and score text
    canvas.draw_text('Lives: '+ str(lives), (50, 50), 36, "cyan")
    canvas.draw_text('Score: '+ str(score), (625, 50), 36, "cyan")
    canvas.draw_text('High score: '+ str(high_score), (625, 550), 28, "cyan")

    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group

    a_rock = Sprite([random.randrange(WIDTH), random.randrange(HEIGHT)],
            [(random.random()*(2.5-0.5) + 0.5)*random.choice([-1, 1]), (random.random()*(2.5-0.5) + 0.5)*random.choice([-1, 1])],
            0,(random.random()*(0.21-0.01) + 0.01)*random.choice([-1, 1]),asteroid_image, asteroid_info)
    if len(rock_group) <= 12 and started == True and dist(a_rock.pos, my_ship.pos) > 60:
        rock_group.add(a_rock)

    # print (len(rock_group))
    

def keydown(key):
    if key == simplegui.KEY_MAP["right"]:
        my_ship.angle_velinc()
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.angle_veldec() 
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust_val()
    elif key == simplegui.KEY_MAP["space"]:
        my_ship.missile()

def keyup(key):
    if key == simplegui.KEY_MAP["right"]:
        my_ship.angle_veldec()
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.angle_velinc() 
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust_val()
    

    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
# a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.1, asteroid_image, asteroid_info)
rock_group = set()
# a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
missile_group = set()

# register handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()