import os

def optimize(path):
    removed = 0

    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".tmp") or f.endswith(".log"):
                os.remove(os.path.join(root, f))
                removed += 1

    return removed
