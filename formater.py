
import sys

def clear_last_lines(n=1):
    """Utility: move cursor up and clear n lines."""
    for _ in range(n):
        sys.stdout.write("\033[F")      # move cursor up
        sys.stdout.write("\033[K")      # clear line
    sys.stdout.flush()