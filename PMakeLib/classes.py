import os
from .db import get_last_hash, add_item, set_hash
from .app_files import to_absolute
from hashlib import md5

targets = dict()


class Target:
    name: str = None
    dependencies: [str, ] = None
    commands: [str, ] = None

    def debug_prin(self):
        print("Target: " + self.name)
        print("Dependencies: " + ', '.join(self.dependencies) )
        print("Body:")
        for line in self.commands:
            print("\t" + line)
        print()

    def __init__(self, header: str, raw_lines: [str, ]):
        self.name, temp = header.split(":")
        self.dependencies = temp.split()
        self.commands = []
        for line in raw_lines:
            self.commands.append(line.strip())

        targets[self.name] = self
        # self.debug_prin()

    def exec(self):
        self()

    def can_skip(self):
        if self.name not in os.listdir():
            # print("[DBG] Not in listdir")
            return False
        try:
            with open(self.name, "rb") as f:
                md = md5(f.read())
                # print(md.hexdigest(), get_last_hash(to_absolute(self.name)))
                lh = get_last_hash(to_absolute(self.name))
                if lh is not None and md.hexdigest() == lh:
                    return True
        except Exception as e:
            # print("[DBG] File opening error", e)
            return False
        return False

    def __call__(self, *args, **kwargs):
        for dep in self.dependencies:
            # print(dep)
            targets[dep]()
        if self.can_skip():
            print("Skipping:", self.name)
            return
        print("Running", self.name, "...")
        for command in self.commands:
            os.system(command.replace("@echo", "echo"))

        lh = get_last_hash(to_absolute(self.name))
        if lh is None:
            try:
                with open(self.name, "rb") as f:
                    md = md5(f.read())
                    # print(md.hexdigest(), get_last_hash(to_absolute(self.name)))
                add_item(to_absolute(self.name), md.hexdigest())
            except:
                pass
        else:
            try:
                with open(self.name, "rb") as f:
                    md = md5(f.read())
                    # print(md.hexdigest(), get_last_hash(to_absolute(self.name)))
                set_hash(to_absolute(self.name), md.hexdigest())
            except:
                pass
