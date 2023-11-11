import sqlite3
import yaml
import os
import sys
import pathlib

config: dict = None


def to_absolute(path: str) -> str:
    f = pathlib.Path(path.replace("~", os.environ["HOME"]))
    return f.absolute().as_posix()


DEFAULT_CONFIG_PATH = to_absolute("~/.PMake/app_config.yaml")
DEFAULT_APP_FILES_ROOT = to_absolute("~/.PMake")


def init():
    global config

    if not os.path.exists(DEFAULT_APP_FILES_ROOT):
        os.mkdir(DEFAULT_APP_FILES_ROOT)

    if config is None:
        if os.path.exists(DEFAULT_CONFIG_PATH):
            with open(DEFAULT_CONFIG_PATH, "rt", encoding="utf-8") as f:
                config = yaml.safe_load(f)
        else:
            config = dict()
            config["db_path"] = DEFAULT_APP_FILES_ROOT + "/db.sqlite3"
