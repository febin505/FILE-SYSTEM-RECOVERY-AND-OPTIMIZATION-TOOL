import os

def analyze(path):
    total_files = 0
    total_size = 0

    for root, dirs, files in os.walk(path):
        for f in files:
            total_files += 1
            fp = os.path.join(root, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)

    return total_files, total_size
