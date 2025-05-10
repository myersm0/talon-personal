from talon import Module, actions, noise
import time

mod = Module()

# define your custom actions
def short_hiss_action():
    print("[hiss] left click")
    actions.mouse_click(0)

def long_hiss_action():
    print("[hiss] right click")
    actions.mouse_click(1)

# arbitrary-length lists of thresholds to apply to your short and long actions
# (lists should be of matched length)
thresholds_short  = [0.8, 0.62, 0.45, 0.27, 0.15]
thresholds_long = [1.3, 1.0 , 1.0 , 1.0 , 1.0 ]

# decay times, in seconds, for dropping from level i to level i-1
# (expected to match length of threshold lists above)
# (index 0 will be unused, so put a dummy 0.0 at start)
decay_times = [0.0, 300.0, 30.0, 10.0, 3.0]

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
        global hiss_stage, last_action_time

        now: float = time.monotonic()
        hiss_length: float = now - hiss_start_time
        since: float = now - last_action_time

        print(f"[hiss] stop at {now:.3f}, length={hiss_length:.3f}, "
              f"since_last={since:.3f}, stage={hiss_stage}")

        # decrement logic: if in stage i and since > decay_times[i], drop to i-1
        for i in range(len(thresholds_short) - 1, 0, -1):
            if hiss_stage == i and since > decay_times[i]:
                hiss_stage = i - 1
                print(f"[hiss] decrement to stage {hiss_stage}")
                break

        threshold1 = thresholds_short[hiss_stage]
        threshold2 = thresholds_long[hiss_stage]
        print(f"[hiss] threshold_short = {threshold1:.3f}, theshold_long = {threshold2:.3f}")

        if hiss_length >= threshold2:
            long_hiss_action()
            hiss_stage = len(thresholds_long) - 1
            print(f"[hiss] reset stage to {hiss_stage}")
            last_action_time = now
        elif hiss_length >= threshold1:
            short_hiss_action()
            hiss_stage = min(hiss_stage + 1, len(thresholds_short) - 1)
            print(f"[hiss] advance stage to {hiss_stage}")
            last_action_time = now
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

