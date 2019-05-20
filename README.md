# The Jencks Python Backup System
The Jencks Python Backup System is a backup service I've created to aid in backing up my files, I used to use the Windows 10 automatic backup system, but for some reason it stopped working months ago and I was never able to figure out why. Thus, I made a system of my own. It's cross platform to windows, and linux.

Contents
--------
**[Installation](#installation)**<br>
**[Usage](#usage)**<br>
**[Command-line Arguments](#command-line-arguments)**<br>
**[GUI](#gui)**<br>
**[Backup Settings](#backup-settings)**<br>
**[Backing up Your Files](#backing-up-your-files)**<br>
**[Restoring Your Files](#restoring-your-files)**<br>
**[Automation](#automating-the-process)**<br>

Installation
------------
To install the JPBS, you need to have python3, tqdm, and a few other dependencies (see below).
### 1. Python 3
   Follow the instructions on [python.org](https://www.python.org/) to get python installed on your system, if you haven't already
### 1. Pip
   You're going to want to install pip for your python installation, you can find instructions on that [here](https://pip.pypa.io/en/stable/installing/).
### 1. Packages
   You need to follow the following packages in order for the software to run correctly<br>
   At this time, you only need one dependency `tqdm` you can install it using `pip install tqdm`
   
Usage
-----
To use the system, you need to run `main.py` in either command prompt or terminal or whatever.<br>
`python main.py`
### Command-line Arguments
There are currently no command-line arguments, but verbose mode `-v` or `--verbose` is in the works.

Headless mode is also in the works `-h` or `--headless`. This will allow the system to run without any user interaction.
### GUI
The GUI is pretty straightforward, it will prompt you with menus similar to this
```
################
   Main Menu
   
Options:

1: Backup now
2: Edit Settings
3: Exit
################
Choice?
```
Simply enter in the number of the option you would like to use and press <kbd>Enter</kbd>
### Backup Settings
There are several different settings that can help you autotune your backup
* #### Output directory
  This is the output folder that you want your backup archives (.zip folders) to be located in.
* #### Included directories
  This is a list of every folder that you want included in your backup.
* #### Excluded directories
  This is a list of every folder that you want excluded from the backup, helpful if the folder exists in one of the included folders.
* #### Total Backup Size
  This is a number in Megabytes that the size of all backups is not to exceed, default is the entire disk partition, but it can be any value, if a single backup is larger than this number, an exception will be thrown.  If a backup were to put the size of all backups over this limit, then the oldest backup will be deleted to make space.
* #### Verbose mode
  In the future, this will cause the progress bars to be replaced with text indicating every file that is being transferred, and when.
### Backing up Your Files
Upon running the software for the first time you will be asked to enter a series of directories/folders.  Here you'll specify where you want the backup archive to be placed, which folders you would like to include in the backup, and which folders (if any) you would like to exclude from the backup.<br>
After completing this initial setup, you'll be shown a main menu similar to the one above, select option `1: Backup now` and the system will begin compressing and copying the selected folders into archives (.zip folders) in the output directory that you specified.
### Restoring Your Files
This functionality is still in development, for now you need to extract the contents of the archive files created upon backup and place them in the directories indicated by the restoration text file.
### Automating the process
I'm still working on this, but I've been researching the [Window's Task Scheduler](https://docs.microsoft.com/en-us/windows/desktop/taskschd/task-scheduler-start-page) and it's [alternative, Cron](https://help.ubuntu.com/community/CronHowto) for linux.
