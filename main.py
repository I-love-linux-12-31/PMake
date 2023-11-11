import sys
import os

import lib.app_files, lib.db


def init():
    lib.app_files.init()
    lib.db.init()

def main():
    init()



if __name__ == "__main__":
    main()
