import os
import shutil

def recover(trash_path, recover_path):
    if not os.path.exists(trash_path):
        return 0

    recovered = 0
    os.makedirs(recover_path, exist_ok=True)

    for f in os.listdir(trash_path):
        shutil.move(
            os.path.join(trash_path, f),
            os.path.join(recover_path, f)
        )
        recovered += 1

    return recovered
