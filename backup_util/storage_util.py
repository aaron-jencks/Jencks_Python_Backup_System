from display_util.string_display_util import print_info
import os
from tqdm import tqdm

# Used to determine how much space is left in the output dir and if previous backups need to be deleted


def list_dir_w_exclusions(path: str, exclusions: list) -> list:
    """Walks a directory and returns a list of all of the files inside with their absolute path,
    excluding those in exclusions."""

    result = []

    def is_excluded(file: str, exclusions: list) -> bool:

        for e in exclusions:

            if os.path.isfile(e):
                if os.path.isfile(file) and file == e:
                    # file is e
                    return True
            elif os.path.isdir(e):
                if e in file:
                    # file is a child of an excluded directory
                    return True

    for r, d, f in os.walk(path, followlinks=True):
        if r not in exclusions:
            for file in f:
                target = os.path.relpath(os.path.join(r, file))
                if not is_excluded(target, exclusions):
                    print_info("Scanned {}".format(target))
                    result.append(target)

    return result


# Determine how much space all of the backups take up (size of the output folder)
def directory_size(path: str) -> float:
    """Computes how much space a directory takes up on the disk and returns its value in MB."""

    return sum(os.path.getsize(p) for p in os.listdir(path) if os.path.isfile(p)) / 1048576


# Determine if there's enough room for another backup
def directory_size_w_exclusions(path: str, exclusions: list) -> float:
    """Computes how much space a directory takes up on the disk and returns its value in MB.

    Excludes the paths/files included in the exclusions list"""

    return sum(os.path.getsize(p) for p in list_dir_w_exclusions(path, exclusions)) / 1048576


# Find the oldest backup to get rid of
def find_oldest_backup(output: str) -> str:
    file_list = [os.path.join(output, f) for f in os.listdir(output)]
    oldest = min(file_list, key=os.path.getctime)
    return oldest
