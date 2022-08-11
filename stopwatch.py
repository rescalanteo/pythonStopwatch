# template for "Stopwatch: The Game"

# define global variables
import simplegui
counter = 0
d = 0
total_ticks = 0
point = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
    
def format(t):
    global d
    d = str(t % 10)
    c = str(((t / 10) % 60) % 10)
    b = str(((t / 10) % 60) // 10)
    a = str(t // 600)
    
    return (a) + ":" + (b) + (c) + "." + (d)
    
def tick():
    global counter
    print format(counter)
    counter += 1 
    
def score():
    global total_ticks
    return str(total_ticks)

def successes():
    global point
    return str(point)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global total_ticks
    global point
    global d
    timer.stop()
    total_ticks += 1
    
    if d == "0":
        point += 1  
    
def reset():
    global counter
    global total_ticks
    global point
    counter = 0
    point = 0
    total_ticks = 0

# define event handler for timer with 0.1 sec interval


# define draw handler  
def draw_handler(canvas):
    canvas.draw_text(format(counter), (40, 110), 50, 'White', 'sans-serif')
    canvas.draw_text(successes() + "/" + score(), (142, 20), 20, 'yellow', 'sans-serif')

# create frame
frame = simplegui.create_frame("Stopwatch Game", 200, 200)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

timer = simplegui.create_timer(100, tick)

# register event handlers

# start frame
frame.start()

# Please remember to review the grading rubric
