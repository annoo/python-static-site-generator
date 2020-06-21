from typing import List
from pathlib import Path
import shutil

class Parser:
    def __init__(self):
        extensions: List[str] = []

    def valid_extension(self):
        return self is in self.extensions

    def parse(path, source, dest):
        self.path: Path = path
        self.souce: Path = source
        self.dest: Path = dest

        raise NotImplementedError

    def read(path):
        with path.open() as file:
            return file.read()

    def write(path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix('.ext').name
        with full_path.open() as file:
            file.write(content)

    def copy(path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))

class ResourceParser(Parser):
    def __init__(self):
        extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self):
        super().copy(path, source, dest)