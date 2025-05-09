from talon import Module, actions, noise
import time

mod = Module()

# left-click adaptive thresholds: first, second, third+ hiss
thresholds_left: list[float] = [0.8, 0.62, 0.45]
# right-click adaptive thresholds: first, second, third+ hiss (last two equal)
thresholds_right: list[float] = [1.3, 1.0, 0.8]

# decay timings (seconds)
decay_mid: float = 30.0           # decay from stage 2→1 after this many seconds
decay_long: float = 30.0 * 30.0   # decay from stage 1→0 after this many seconds

# state
hiss_stage: int = 0
last_action_time: float = 0.0
hiss_start_time: float = 0.0

@mod.action_class
class Actions:
    def noise_hiss_start() -> None:
        """
        Record the start time of a hiss noise.
        """
        global hiss_start_time
        hiss_start_time = time.monotonic()
        print(f"[hiss] start at {hiss_start_time:.3f}")

    def noise_hiss_stop() -> None:
        """
        On hiss end, measure duration and:
        - If >= current right threshold: perform a right click,
          reset hiss_stage to the shortest level, and update time.
        - Else if >= current left threshold: perform a left click,
          advance hiss_stage by one and update time.
        Apply decay to hiss_stage after silence intervals.
        """
        global hiss_stage, last_action_time

        now: float = time.monotonic()
        hiss_length: float = now - hiss_start_time
        since: float = now - last_action_time

        print(f"[hiss] stop at {now:.3f}, length={hiss_length:.3f}, "
              f"since_last={since:.3f}, stage={hiss_stage}")

        # decay stage
        if since > decay_long:
            hiss_stage = 0
            print("[hiss] decay to stage 0")
        elif since > decay_mid:
            hiss_stage = 1
            print("[hiss] decay to stage 1")

        left_thresh: float = thresholds_left[hiss_stage]
        right_thresh: float = thresholds_right[hiss_stage]
        print(f"[hiss] thresholds: left={left_thresh:.3f}, right={right_thresh:.3f}")

        if hiss_length >= right_thresh:
            print(f"[hiss] hiss_length {hiss_length:.3f} >= right_thresh, right click!")
            actions.mouse_click(1)
            hiss_stage = len(thresholds_left) - 1
            last_action_time = now
            print(f"[hiss] reset stage to {hiss_stage}")
        elif hiss_length >= left_thresh:
            print(f"[hiss] hiss_length {hiss_length:.3f} >= left_thresh, left click!")
            actions.mouse_click(0)
            hiss_stage = min(hiss_stage + 1, len(thresholds_left) - 1)
            last_action_time = now
            print(f"[hiss] advance stage to {hiss_stage}")
        else:
            print("[hiss] hiss too short, no click")

def hiss_handler(active: bool) -> None:
    """
    Talon noise event handler: dispatch hiss start/stop.
    """
    if active:
        actions.user.noise_hiss_start()
    else:
        actions.user.noise_hiss_stop()

noise.register("hiss", hiss_handler)

