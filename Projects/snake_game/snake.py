#Credit the Invent With Python book (http://inventwithpython.com)
#for doRectsOverlap and isPointInsideRect functions

#used to detect collisions in our game
def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False

#used the by the doRectsOverlap function (won't be called directly from game code)
def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False


def new_target_location():
    global food_x, food_y
    food_x = randint(40,600)
    food_y = randint(40,440)

import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]

#the game's variables
#SECTION 1 - YOUR CODE HERE FOR CREATING VARIABLES AND FUNCTIONS
snake_speed = 5
snake_y = 200
snake_x = 200
snake_radius = 10
snake_color = (0,204,102)

food_radius = 5
food_x = 320
food_y = 240
food_color = (0,0,255)


running = True
#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
        if event.type == pygame.KEYDOWN:
            print "key pressed"
            #SECTION 2 - YOUR CODE HERE FOR WHEN A KEY IS PRESSED
            if event.key == pygame.K_LEFT:
                snake_x = snake_x - snake_speed
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + snake_speed
            if event.key == pygame.K_UP:
                snake_y = snake_y - snake_speed
            if event.key == pygame.K_DOWN:
                snake_y = snake_y + snake_speed

    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely black
    screen.fill(black)

    #logic for moving everything in the game and checking collisions
    #SECTION 4 - YOUR CODE HERE FOR CHANGING VARIABLES AND CHECKING FOR COLLISIONS
    snake_rectangle = pygame.Rect(snake_x-snake_radius, snake_y-snake_radius,2*snake_radius,2*snake_radius)
    food_rectangle = pygame.Rect(food_x-food_radius, food_y-food_radius, 2*food_radius, 2*food_radius)
    if doRectsOverlap(snake_rectangle,food_rectangle):
        new_target_location()

    #circles are measured from the center, so have to subtract 1 radius from the x and y


    #draw everything on the screen
    #SECTION 5 - YOUR CODE HERE FOR DRAWING EVERYTHING
    pygame.draw.circle(screen, snake_color, [snake_x,snake_y], snake_radius)
    pygame.draw.circle(screen, food_color, [food_x,food_y], food_radius)
    #update the entire display
    pygame.display.update()


pygame.quit()