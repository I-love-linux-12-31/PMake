import sqlite3
from . import app_files


sqlite3_connection: sqlite3.Connection = None


def init():
    global sqlite3_connection
    path = app_files.config["db_path"]
    sqlite3_connection = sqlite3.connect(path)


def get_last_hash(file_absolute_pah: str) -> str:
    cur = sqlite3_connection.cursor()
    cur.execute(f"SELECT md5 FROM files WHERE path == '{file_absolute_pah}'")
    return cur.fetchone()[0]


def set_hash(file_absolute_pah: str, md5_hash: str):
    cur = sqlite3_connection.cursor()
    cur.execute(f"UPDATE files SET md5 = '{md5_hash}' WHERE path == '{file_absolute_pah}'")
    sqlite3_connection.commit()


def add_item(file_absolute_pah: str, md5_hash: str):
    cur = sqlite3_connection.cursor()
    try:
        cur.execute(f"INSERT INTO files (path, md5) VALUES ('{file_absolute_pah}', '{md5_hash}')")
        sqlite3_connection.commit()
    except sqlite3.IntegrityError:
        print("[Err]: ADD existing file to db is bs idea !")


def on_exit():
    sqlite3_connection.close()
