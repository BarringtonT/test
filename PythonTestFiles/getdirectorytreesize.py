
import os


def dirsize(start_dirpath):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_dirpath):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size
