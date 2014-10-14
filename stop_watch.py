# template for "Stopwatch: The Game"
import simplegui

# define global variables
timer_counter = 0
timer_status = False
stop_count = 0
stop_success = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minute = t  // 600
    ten_second = (t - minute*600)// 100
    second = (t - minute*600 - ten_second*100) //10
    mini_second = t % 10
    return str(minute) + ":" + str(ten_second) + str(second) + "." + str(mini_second)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global timer_status
    if timer_status == False:
        timer.start()
        timer_status = True

def stop_handler():
    global timer_status, timer_counter, stop_count, stop_success
    if timer_status == True:
        timer.stop()
        timer_status = False
        stop_count += 1
        if timer_counter % 10 ==0:
            stop_success += 1

def reset_handler():
    global timer_status, timer_counter, stop_count, stop_success
    timer.stop()
    timer_counter = 0
    stop_count = 0
    stop_success = 0
    timer_status = False
    

# define event handler for timer with 0.1 sec interval
def timer_event():
    global timer_counter
    timer_counter += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(timer_counter), (50, 110), 80, "#fff", "sans-serif")
    canvas.draw_text(str(stop_success)+"/"+str(stop_count), (300, 20), 18, "#fff", "monospace")

timer = simplegui.create_timer(100, timer_event)
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 350, 150)
start_btn = frame.add_button("Start", start_handler, 100)
stop_btn = frame.add_button("Stop", stop_handler, 100)
reset_btn = frame.add_button("Reset", reset_handler, 100)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
# Please remember to review the grading rubric