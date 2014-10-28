# implementation of card game - Memory

import simplegui
import random

WIDTH = 50
HEIGHT = 100

# helper function to initialize globals
def new_game():
    
    global moves, number, exposed, state
    moves, state = 0, 0, 0
    number = range(0, 8)
    number.extend(range(0, 8))  
    random.shuffle(number)
    exposed = [False for i in range(16)]
     
# define event handlers
def mouseclick(pos):
    
    global moves, exposed, state, pre_index, next_index 
    index = pos[0] // WIDTH
    
    if not exposed[index]:
        exposed[index] = True
        if state == 0:
            pre_index = index
            state = 1
        elif state == 1:
            next_index = index
            state = 2
        elif state == 2:
            if number[pre_index] != number[next_index]:
                exposed[pre_index] = False
                exposed[next_index] = False
            pre_index = index
            state = 1
            moves += 1  
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    label.set_text("Moves = "+ str(moves))
    for index in range(0,len(number)):
        if(exposed[index]==0):
            canvas.draw_polygon([(WIDTH*index,0), (WIDTH*(index+1), 0), (WIDTH*(index+1), 100),(WIDTH*index,100)], 3, "White","Green")
        else:
            canvas.draw_text(str(number[index]), [WIDTH*index+10,HEIGHT-25], 60, "White")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric