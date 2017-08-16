import json
import hashlib
import contextlib
from typing import Generator

replyIsYes = lambda: input("[y]es or [n]o? >>> ").lower().startswith("y")

@contextlib.contextmanager
def documentDB(file_path: str) -> Generator:
    with open(file_path, mode="rt") as fp:
        con = json.load(fp)
    yield con
    with open(file_path, mode="wt") as fp:
        json.dump(con, fp)
    return

def calc_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, mode="rb") as fp:
        for aBlock in iter(lambda: fp.read(128), b""):
            hasher.update(aBlock)
    return hasher.hexdigest()

