from talon import Module, actions, noise, ctrl
import time

# an adaptive twist on using the hiss noise

mod = Module()

# define your custom actions
def hiss_action():
    print("[hiss] left click")
    actions.mouse_click(0)

# arbitrary-length lists of thresholds to apply to your hiss action
thresholds  = [0.8, 0.62, 0.45, 0.27, 0.15]

max_hiss_dur = 1.5

# decay times, in seconds, for dropping from level i to level i-1
# (expected to match length of threshold list above)
# (index 0 will be unused)
decay_times = [None, 300.0, 30.0, 10.0, 3.0]

last_mouse_pos = ctrl.mouse_pos()

# state
hiss_stage = 0
last_action_time = 0.0
hiss_start_time = 0.0

@mod.action_class
class Actions:
    def noise_hiss_start() -> None:
        """
        Record the monotonic timestamp when a hiss noise begins.
        """
        global hiss_start_time
        hiss_start_time = time.monotonic()
        print(f"[hiss] start at {hiss_start_time:.3f}")

    def noise_hiss_stop() -> None:
        """
        On hiss end:
        - decrement hiss_stage if enough time has passed
        - measure hiss_length and act accordingly
        """
        global hiss_stage, last_action_time, last_mouse_pos

        now: float = time.monotonic()
        hiss_length: float = now - hiss_start_time
        since: float = now - last_action_time

        print(f"[hiss] stop at {now:.3f}, length={hiss_length:.3f}, "
              f"since_last={since:.3f}, stage={hiss_stage}")

        # decrement logic: if in stage i and since > decay_times[i], drop to i-1
        for i in range(len(thresholds) - 1, 0, -1):
            if hiss_stage == i and since > decay_times[i]:
                hiss_stage = i - 1
                print(f"[hiss] decrement to stage {hiss_stage}")
                break

        threshold = thresholds[hiss_stage]
        print(f"[hiss] threshold = {threshold:.3f}")

        if hiss_length > max_hiss_dur:
            print(f"[hiss] action rejected (hiss was too long)")
        elif hiss_length > threshold:
            current_mouse_pos = ctrl.mouse_pos()
            if current_mouse_pos == last_mouse_pos:
                print(f"[hiss] action rejected (the mouse has not moved)")
                return
            hiss_action()
            hiss_stage = min(hiss_stage + 1, len(thresholds) - 1)
            print(f"[hiss] advance stage to {hiss_stage}")
            last_action_time = now
            last_mouse_pos = ctrl.mouse_pos()
        else:
            print("[hiss] no click (too short)")

def hiss_handler(active: bool) -> None:
    """
    Handler for Talon noise events: dispatch hiss start/stop.
    """
    if active:
        actions.user.noise_hiss_start()
    else:
        actions.user.noise_hiss_stop()

noise.register("hiss", hiss_handler)

