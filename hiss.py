from talon import Module, actions, ctrl, noise, cron, Context, ui, settings
import time


mod = Module()
ctx = Context()


start = 0
noise_length = 0.2


# global last_activity_at


hiss_start_time = 0
hiss_end_time   = 0


# short: Single Click
min_dot_time = 0.2
# Medium: Double Click
max_dot_time = 1.0
ludicrous_time = 2.0


@mod.action_class
#@ctx.action_class('user')
class UserActions:
    def noise_hiss_start():
        """Invoked when the user starts hissing (potentially while speaking)"""
        global hiss_start_time
        hiss_start_time = time.monotonic()
        pass

    def noise_hiss_stop():
        """Invoked when the user finishes hissing (potentially while speaking)"""
        global hiss_start_time
        global hiss_end_time

        hiss_end_time = time.monotonic()

        global last_activity_at
        last_activity_at= time.monotonic()

        hiss_length_in_seconds =  hiss_end_time - hiss_start_time
        #print("Length of hiss:" + str(hiss_length_in_seconds))

        # if hiss_length_in_seconds < min_dot_time:
        #     print("I'm not doing anything.")

        if hiss_length_in_seconds >= max_dot_time and hiss_length_in_seconds < ludicrous_time:
            print("I'm a DOUBLE click from Noises/hiss__short_and_long.py")
            actions.mouse_click(0)
            actions.mouse_click(0)

        elif hiss_length_in_seconds >= min_dot_time and hiss_length_in_seconds < max_dot_time:
            print("I'm a Single click from Noises/hiss__short_and_long")
            #print("nothing")
            #actions.mouse_click(0)
            #
            # ALL OF THESE ACTIONS NEEDED FOR CLICK TO WORK IN SLACK
            # sleep needed so that Scroll down works in Slack
            actions.mouse_drag(0)
            actions.sleep("150ms")
            actions.mouse_release(0)

        pass



def hiss_handler(active):
    if active:
        actions.user.noise_hiss_start()
    else:
        actions.user.noise_hiss_stop()


# function
noise.register("hiss", hiss_handler)
