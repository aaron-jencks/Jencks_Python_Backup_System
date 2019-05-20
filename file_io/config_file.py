from display_util.string_display_util import print_warning, print_notification
import os
import json


class Config:
    """A class used to store key-value pairs that can be exported to an .ini file when finished."""

    def __init__(self, path: str, data: dict = None):
        self.data = data
        self.path = path
        self.modified = True

        # Loads the file if told to
        if len(path) > 0 and data is None:
            if os.path.isfile(path):
                self.load()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value
        self.modified = True

    def load(self):
        if os.path.isfile(self.path):
            with open(self.path, 'r') as f:
                self.data = json.load(f)

            self.modified = False
            print_notification("json config file loaded")

    def save(self):
        if not os.path.isfile(self.path):
            print_warning("json config file did not exist, attempting to create.")
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            print_notification("Directory created!")

        with open(self.path, 'w+') as f:
            json.dump(self.data, f)

        self.modified = False
        print_notification("json config file saved")
