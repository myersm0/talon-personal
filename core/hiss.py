from talon import Module, actions, noise, ctrl
import time

# an adaptive twist on using the hiss noise

mod = Module()

# define your custom actions
def hiss_action():
    print("[hiss] left click")
    actions.mouse_click(0)

# arbitrary-length lists of thresholds to apply to your hiss action:
thresholds  = [0.6, 0.45, 0.3, 0.18, 0.1]

# anything longer than this will be rejected:
max_hiss_dur = 1.2

# require that the mouse moved between actions?
require_mouse_move = True

# decay times, in seconds, for dropping from level i to level i-1
# (expected to match length of threshold list above)
# (index 0 will be unused because there is no dropping down from the 0th level)
decay_times = [None, 60, 30, 15, 3]

# state
hiss_stage = 0
last_action_time = 0.0
hiss_start_time = 0.0
last_mouse_pos = ctrl.mouse_pos()

# sanity checks
if not isinstance(thresholds, list) or not thresholds:
    raise ValueError("`thresholds` must be a non-empty list of positive numbers")
if not all(isinstance(t, (int, float)) and t > 0 for t in thresholds):
    raise ValueError("all entries in `thresholds` must be positive numbers")
if not isinstance(max_hiss_dur, (int, float)) or max_hiss_dur <= max(thresholds):
    raise ValueError("`max_hiss_dur` must be a number greater than the largest threshold")
if not isinstance(decay_times, list) or len(decay_times) != len(thresholds):
    raise ValueError("`decay_times` must be a list the same length as `thresholds`")
for i, dt in enumerate(decay_times[1:], start=1):
    if not isinstance(dt, (int, float)) or dt <= 0:
        raise ValueError(f"`decay_times[{i}]` must be a positive number")

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

        current_mouse_pos = ctrl.mouse_pos()
        if hiss_length > max_hiss_dur:
            print(f"[hiss] action rejected (hiss was too long)")
        elif hiss_length > threshold:
            if require_mouse_move and current_mouse_pos == last_mouse_pos:
                print(f"[hiss] action rejected (the mouse has not moved)")
                return
            hiss_action()
            hiss_stage = min(hiss_stage + 1, len(thresholds) - 1)
            print(f"[hiss] advance stage to {hiss_stage}")
            last_action_time = now
        else:
            print("[hiss] no click (too short)")
        last_mouse_pos = ctrl.mouse_pos()

def hiss_handler(active: bool) -> None:
    """
    Handler for Talon noise events: dispatch hiss start/stop.
    """
    if active:
        actions.user.noise_hiss_start()
    else:
        actions.user.noise_hiss_stop()

noise.register("hiss", hiss_handler)

