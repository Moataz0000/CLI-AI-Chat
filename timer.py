import sys
import time
import threading
from termcolor import colored

# Small utility that shows a live timer on one terminal line
class ThinkingTimer:
    def __init__(self, label="Thinking"):
        self.label = label
        self._stop = threading.Event()
        self._thread = None
        self._start = None
        self._frames = ["⠋","⠙","⠸","⠴","⠦","⠇"]  # simple spinner

    def __enter__(self):
        self._start = time.perf_counter()
        self._thread = threading.Thread(target=self._run, daemon=True)
        # Hide cursor
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.stop()

    def stop(self):
        if not self._stop.is_set():
            self._stop.set()
            if self._thread:
                self._thread.join()
            # Clear the line and show cursor again
            sys.stdout.write("\r\033[2K")  # carriage return + clear line
            sys.stdout.write("\033[?25h")
            sys.stdout.flush()

    def elapsed(self):
        if self._start is None:
            return 0.0
        return time.perf_counter() - self._start

    def _run(self):
        i = 0
        while not self._stop.is_set():
            elapsed = self.elapsed()
            # Build the status line
            msg = f"{self._frames[i % len(self._frames)]} {self.label}… {elapsed:0.1f}s"
            # Print in place
            sys.stdout.write("\r" + colored(msg, "yellow"))
            sys.stdout.flush()
            i += 1
            self._stop.wait(0.1)  # update ~10x/sec
