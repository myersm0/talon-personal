from talon import Module, actions, cron

# adapted from https://github.com/AndreasArvidsson/andreas-talon/blob/2772b176f2c5679d8da4ffeba75db1eda20b711a/core/keys/key_hold.py

mod = Module()
repeated_key_jobs = {}

@mod.action_class
class Actions:
    def key_hold(key: str, repeat_rate: str = "16ms", repeat_delay: str = "256ms"):
        """Simulate holding a key with repeated key presses"""
        actions.key(key)
        def add_interval():
            repeated_key_jobs[key] = cron.interval(
                repeat_rate,
                lambda: actions.key(key),
            )
        repeated_key_jobs[key] = cron.after(repeat_delay, add_interval)

    def key_release(key: str):
        """Stop repeating key"""
        job = repeated_key_jobs[key]
        if job is not None:
            cron.cancel(job)
            repeated_key_jobs[key] = None
