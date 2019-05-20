from backup_util.Backup import Backup
from display_util.string_display_util import print_notification, print_warning, print_list, ListTypes
from display_util.menu import console_dash_menu, yes_no_prompt, get_constrained_input, clear
from file_io.config_file import Config
from colorama import Fore
import os


config_path = "D:/backup/config.json"


def create_backup_object() -> Backup:
    """Walks the user through the first-time setup of the backup system."""

    print(Fore.CYAN + "It would appear that it's your first time! "
          "Let's get you setup!" + Fore.RESET)

    temp = input(Fore.GREEN + "Please enter an output directory: " + Fore.RESET)
    while not os.path.isdir(temp):
        print_warning("Invalid directory selected, directory does not exist!")
        if yes_no_prompt("Would you like to go ahead and create this directory?"):
            try:
                os.makedirs(temp)
                break
            except Exception as e:
                print(e)
        temp = input(Fore.GREEN + "Please enter a new output directory: " + Fore.RESET)

    output_dir = temp

    print(Fore.CYAN + "Now we need to add some files/folders to backup, feel free to enter as many as you like"
          "Just enter STOP when you're finished." + Fore.RESET)

    included = []
    temp = get_constrained_input("Please enter a file/folder you would like to include \
    (Type STOP when you are done): ", lambda x: os.path.exists(x) or x == "STOP")
    while temp != "STOP":
        included.append(temp)
        clear()
        print_list(included, type=ListTypes.UNORDERED)
        temp = get_constrained_input("Please enter a file/folder you would like to include \
            (Type STOP when you are done): ", lambda x: os.path.exists(x) or x == "STOP")

    excluded = []
    if yes_no_prompt("Are there any files you wish to exclude?"):
        temp = get_constrained_input("Please enter a file/folder you would like to exclude \
            (Type STOP when you are done): ", lambda x: os.path.exists(x) or x == "STOP")
        while temp != "STOP":
            excluded.append(temp)
            clear()
            print_list(excluded, type=ListTypes.UNORDERED)
            temp = get_constrained_input("Please enter a file/folder you would like to exclude \
                    (Type STOP when you are done): ", lambda x: os.path.exists(x) or x == "STOP")

    print(Fore.CYAN + "Well, that's just about it, hold on while we set things up." + Fore.RESET)
    return Backup(included, excluded, output_dir)


if __name__ == "__main__":
    print_notification("Welcome to the Jencks backup system!")

    # Load from a file here
    if os.path.isfile(config_path):
        c = Config(config_path)
        b = Backup(c.data['included'], c.data['excluded'], c.data['output_dir'])
    else:
        b = create_backup_object()
        c = Config(config_path,
                   {'included': b.included_folders, 'excluded': b.excluded_folders, 'output_dir': b.output_dir})
        c.save()

    while True:
        options = {"1": "Backup now", "2": "Edit Settings", '3': "Exit"}
        choice = int(console_dash_menu(options, title="Main Menu"))

        if choice == 1:
            b.backup()
        elif choice == 2:
            # Edit the settings
            options = {'1': "output directory\t{}".format(b.output_dir),
                       '2': "Included directories", '3': "Excluded directories", '4': "Go back"}

            while True:
                choice = int(console_dash_menu(options, title="Settings Menu"))

                if choice == 1:
                    temp = input(Fore.GREEN + "Please enter a new output directory: " + Fore.RESET)
                    while not os.path.isdir(temp):
                        print_warning("Invalid directory selected, directory does not exist!")
                        temp = input(Fore.GREEN + "Please enter a new output directory: " + Fore.RESET)

                    b.output_dir = temp
                    print_notification("Output directory changed to {}".format(temp))
                    continue
                elif choice == 2:
                    temp = get_constrained_input("Please enter a file/folder you would like to include \
                                (Type STOP when you are done): ", lambda x: os.path.exists(x) or x == "STOP")
                    while temp != "STOP":
                        b.included_folders.append(temp)
                        clear()
                        print_list(b.included_folders, type=ListTypes.UNORDERED)
                        temp = get_constrained_input("Please enter a file/folder you would like to include \
                                        (Type STOP when you are done): ", lambda x: os.path.exists(x) or x == "STOP")
                elif choice == 3:
                    temp = get_constrained_input("Please enter a file/folder you would like to exclude \
                                (Type STOP when you are done): ", lambda x: os.path.exists(x) or x == "STOP")
                    while temp != "STOP":
                        b.excluded_folders.append(temp)
                        clear()
                        print_list(b.excluded_folders, type=ListTypes.UNORDERED)
                        temp = get_constrained_input("Please enter a file/folder you would like to exclude \
                                        (Type STOP when you are done): ", lambda x: os.path.exists(x) or x == "STOP")
                else:
                    break

            continue
        else:
            # Exit
            print_notification("Goodbye!")
            break

    pass
