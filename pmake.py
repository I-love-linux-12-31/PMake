#!env python3
import sys
import os
from PMakeLib.classes import *
import PMakeLib.app_files, PMakeLib.db


def init():
    PMakeLib.app_files.init()
    PMakeLib.db.init()


def main():
    init()
    listdir = [d.upper() for d in os.listdir()]
    if "MAKEFILE" not in listdir and "MAKEFILE.PMAKE" not in listdir:
        print("\033[33mMakefile not found in current folder!\033[0m")
        exit()
    for item in os.listdir():
        if item.upper() in ("MAKEFILE", "MAKEFILE.PMAKE"):
            file = open(item, "rt", encoding="utf-8")
            break
    raw_lines = file.readlines()
    header_line = ""
    target_lines = []
    for line in raw_lines:
        if not line.strip():
            continue
        if ':' in line:
            if header_line != "":
                Target(header_line, target_lines)  # .debug_prin()
                target_lines.clear()
            header_line = line
        elif line.startswith(" ") or line.startswith("\t"):
            target_lines.append(line)
        else:
            # print(tuple(map(str.strip, line.split("="))))
            var_name, var_val = tuple(map(str.strip, line.split("=")))
            os.environ[var_name] = var_val
    if header_line != "":
        Target(header_line, target_lines)  # .debug_prin()

    argv = sys.argv
    if len(argv) > 1:
        target_name = argv[1]
        if target_name not in targets:
            print(f"\033[33mTarget '{target_name}' not found!\033[0m")
        else:
            targets[target_name]()
    else:
        if not targets.items():
            return
        tuple(targets.items())[0][1]()

    PMakeLib.db.on_exit()


if __name__ == "__main__":
    main()
