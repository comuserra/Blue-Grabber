import os
from time import sleep
from zipfile import ZipFile

import requests


class Update():
    def __init__(self):
        self.version = '1.5.5'
        self.github = 'https://raw.githubusercontent.com/Smug246/Luna-Grabber/main/tools/update.py'
        self.zipfile = 'https://raw.githubusercontent.com/comuserra/blue-grabber/54634fb7d8a0b02aea600fcdcb0659a145e6e315/Blue%20Grabber%20V1.zip'
        self.update_checker()

    def update_checker(self):
        code = requests.get(self.github).text
        if "self.version = '1.5.5'" in code:
            print('This version is up to date!')
            print('Exiting...')
            sleep(2)
            exit()
        else:
            print('''
                    ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                    ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                    ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                                      Your version of Blue Grabber is outdated!''')
            choice = input('\nWould you like to update? (y/n): ')
            if choice.lower() == 'y':
                new_version_source = requests.get(self.zipfile)
                with open("Blue-Grabber-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("Blue-Grabber-main.zip", 'r') as filezip:
                    filezip.extractall(path=os.path.join(os.path.expanduser("~"), "Desktop"))
                os.remove("Blue-Grabber-main.zip")
                print('The new version is now on your desktop.\nUpdate Complete!')
                print("Exiting...")
                sleep(5)
            if choice.lower() == 'n':
                print('Exiting...')
                sleep(2)
                exit()


if __name__ == '__main__':
    Update()
