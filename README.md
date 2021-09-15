# line-ui
This is a small Python package to provide an API to a one-line user interface (like that in a calculator) for Python learners.

![a sample line UI app](https://github.com/freemant2000/line-ui/raw/main/images/lineui.png)

It provides the following features:
* output in the line (left, right or middle aligned).
* output in the console (the lower box), mainly for debugging.
* keyboard input.
* timer input (every second or every 0.05 seconds).
* schedule a call to a function a certain seconds later.
* make a beep.

With these a Python learner can make apps like: digital clock, 
the classic digit invaders game, slapjack, etc.

## How to use
Here is a sample program using line UI that displays a counter, which
is incremented every second or when the user presses the up arrow key.

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
        draw_r(str(n), False) # False tells the UI not to erase
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
            draw_r(str(n), False)
        elif k==" ":
            draw_l("X", False) # draw a left-aligned string
            schedule(1, hide_x)# hide X in one second
        elif k == "q":
            stop()  # use this to tell the app to quit

    def hide_x():
        draw_l(" ", False)

    start(globals())  # must do this to kick start the app with the UI
