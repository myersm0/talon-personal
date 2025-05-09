from talon import Module, actions, noise
import time

mod = Module()

# arbitrary-length list of left-click thresholds_left
thresholds_left: list[float] =  [0.8, 0.62, 0.45, 0.27, 0.15]
thresholds_right: list[float] = [1.3, 1.0 , 1.0 , 1.0 , 1.0 ]
# decay times for dropping from stage i to stage i-1 (seconds)
# index 0 unused, so put a dummy 0.0 at start
decay_times: list[float] = [0.0, 300.0, 30.0, 10.0, 3.0]

# state
hiss_stage: int = 0
last_action_time: float = 0.0
hiss_start_time: float = 0.0

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
        - decay hiss_stage if enough time has passed
        - measure hiss_length
        - if hiss_length >= 2×threshold: right-click, reset to fastest stage
        - elif hiss_length >= threshold: left-click, advance stage
        - else: no click
        """
        global hiss_stage, last_action_time

        now: float = time.monotonic()
        hiss_length: float = now - hiss_start_time
        since: float = now - last_action_time

        print(f"[hiss] stop at {now:.3f}, length={hiss_length:.3f}, "
              f"since_last={since:.3f}, stage={hiss_stage}")

        # decay logic: if in stage i and since > decay_times[i], drop to i-1
        for i in range(len(thresholds_left) - 1, 0, -1):
            if hiss_stage == i and since > decay_times[i]:
                hiss_stage = i - 1
                print(f"[hiss] decay to stage {hiss_stage}")
                break

        threshold: float = thresholds_left[hiss_stage]
        right_threshold: float = thresholds_right[hiss_stage]
        print(f"[hiss] threshold={threshold:.3f}, right_threshold={right_threshold:.3f}")

        if hiss_length >= right_threshold:
            print("[hiss] right click")
            actions.mouse_click(1)
            hiss_stage = len(thresholds_left) - 1
            print(f"[hiss] reset stage to {hiss_stage}")
            last_action_time = now
        elif hiss_length >= threshold:
            print("[hiss] left click")
            actions.mouse_click(0)
            hiss_stage = min(hiss_stage + 1, len(thresholds_left) - 1)
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

