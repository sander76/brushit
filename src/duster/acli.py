from dataclasses import dataclass
from pathlib import Path
from jsonargparse import CLI


@dataclass
class Branch:
    root_folder: Path = Path.cwd()

    def list(self):
        print("list")

    def clean(self):
        print("clean")


if __name__ == "__main__":
    CLI(Branch)
