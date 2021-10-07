from line_ui import *

n = 0

# called when the UI is ready for you. You can display the
# initial stuff here.
def on_ready():
    draw_r(str(n))  # draw a right-aligned string in the line

# called every frame (0.05 seconds). As it is empty, you may
# as well just delete this function.
def on_update():
    pass

# called every second
def on_second():
    global n
    n = n+1
    draw_r(str(n)) # automatically erase the previous frame
    # you can use print to print to the lower box
    print("got abcde "+str(n))
    beep() # make a beep

# called when the user presses a key
def on_key():
    global n
    # you can get the key as a str, e.g., you get "a" if A key was pressed.
    k = get_key()
    if k == "KEY_UP":
        n = n+1
        draw_r(str(n))
    elif k==" ":
        draw_l("X") # draw a left-aligned string
        schedule(1, hide_x)# hide X in one second
    elif k == "q":
        stop()  # use this to tell the app to quit

def hide_x():
    draw_l(" ")

start(globals())  # must do this to kick start the app with the UI
