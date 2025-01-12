from talon import Module, actions, cron

mod = Module()
repeated_key_jobs = {}

@mod.action_class
class Actions:
    def key_hold(key: str, repeat_rate: str = "16ms", repeat_delay: str = "256ms"):
        """Simulate holding a key with repeated key presses"""
        if key in repeated_key_jobs:
            # If already holding the key, do nothing
            return
        actions.key(key)

        def add_interval():
            repeated_key_jobs[key] = cron.interval(
                repeat_rate,
                lambda: actions.key(key),
            )

        # Schedule the initial delay followed by repeated presses
        repeated_key_jobs[key] = cron.after(repeat_delay, add_interval)

    def key_release(key: str):
        """Stop repeating key"""
        if key in repeated_key_jobs:
            job = repeated_key_jobs.pop(key, None)
            if job is not None:
                cron.cancel(job)

    def release_all_keys():
        """Stop all repeating keys"""
        for key in list(repeated_key_jobs.keys()):
            self.key_release(key)

