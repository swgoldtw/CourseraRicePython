# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [random.randrange(120, 240)/60, random.randrange(60, 180)/60]
    if direction == RIGHT:
        ball_vel[1] = -ball_vel[1]
    elif direction == LEFT:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = -ball_vel[1]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT / random.randrange(2, 7)
    paddle2_pos = HEIGHT / random.randrange(2, 7)
    score1, score2 = 0, 0
    spawn_ball(random.choice([LEFT, RIGHT]))
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel
     
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "Green")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "Green")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "Green")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # check left and right
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) or (ball_pos[0]>= WIDTH- BALL_RADIUS - PAD_WIDTH):
        ball_vel[0] = -ball_vel[0]
        
        if ball_pos[0] < (WIDTH/2):
            if (ball_pos[1] < paddle1_pos) or (ball_pos[1] > paddle1_pos + PAD_HEIGHT):
                score2 += 1
                spawn_ball(RIGHT)
            else:
                ball_vel[0] = 1.1* ball_vel[0]
        if ball_pos[0] > (WIDTH/2):
            if (ball_pos[1] < paddle2_pos) or (ball_pos[1] > paddle2_pos + PAD_HEIGHT):
                score1 += 1
                spawn_ball(LEFT)
            else:
                ball_vel[0] = 1.1*ball_vel[0]
        
    # check top and down bound
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT-BALL_RADIUS):  
        ball_vel[1] = -ball_vel[1]  
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Yellow", "White")        
    
    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos],[PAD_WIDTH, (paddle1_pos) + PAD_HEIGHT ],[0, (paddle1_pos) + PAD_HEIGHT]],1, "green", "white") 
    canvas.draw_polygon([[WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT], [WIDTH, paddle2_pos + PAD_HEIGHT]],1, "green", "white")
   
    # draw scores
    canvas.draw_text(str(score1), [220, 50], 60, "White")    
    canvas.draw_text(str(score2), [355, 50], 60, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    step = 4
    
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = -step
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = step
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -step
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = step
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if (key == simplegui.KEY_MAP['s'] or key == simplegui.KEY_MAP['w']):    
        paddle1_vel = 0     
    if (key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']):    
        paddle2_vel = 0 

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("RESRAT", new_game, 100)

# start frame
new_game()
frame.start()