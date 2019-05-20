from .storage_util import directory_size, directory_size_w_exclusions, find_oldest_backup
from display_util.string_display_util import print_info, print_warning, print_notification
import archive_util.archive as archive
from archive_util.archive import zip_dir, zip_dir_delete_orig
from colorama import Fore
import os
import tempfile


class Backup:

    # Size limit in MB of all backups combined
    size_limit = -1

    def __init__(self, included: list, excluded: list, output_dir: str):
        self.included_folders = included
        self.excluded_folders = excluded
        self.output_dir = output_dir
        self.backed_up = False
        self.back_up_date = None

    def __len__(self):
        return sum(directory_size_w_exclusions(x, self.excluded_folders) for x in self.included_folders)

    def backup(self):
        """Performs a backup"""

        archive.backup_dir = self.output_dir

        if Backup.size_limit > 0:
            if len(self) > Backup.size_limit:
                raise IOError(Fore.RED + "The current backup exceeds the size limit of all backups." + Fore.RESET)
            else:
                print_info("Starting backup...")

                while len(self) + directory_size(self.output_dir) > Backup.size_limit:
                    print_warning("Erasing previous backup due to size constraints")
                    b = find_oldest_backup(self.output_dir)
                    os.remove(b)

        print_info("Zipping target folders")

        # Creates a temporary directory to store intermediate archives
        temp = tempfile.TemporaryDirectory(prefix='backup', dir=self.output_dir)
        tempdir = temp.name
        print_info("Creating intermediate archives in {}".format(tempdir))

        for d in self.included_folders:
            print_info("Archiving {}".format(d))
            zip_dir(d, tempdir, self.excluded_folders)

        print_info("Moving temp directory to output directory")
        zip_dir_delete_orig(tempdir, self.output_dir)

        temp.cleanup()

        print_notification("Backup complete!")



    # Find a way to schedule for this program to run again after the specified period of frequency occurs

