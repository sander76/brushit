"""some cli"""
from pathlib import Path
from pydantic import BaseModel, DirectoryPath
import clipstick
from brushit import controller


class List(BaseModel):
    """List all local branches."""

    root_folder: DirectoryPath = Path.cwd()
    """The repo root folder."""

    def main(self):
        controller.list_branches(self.root_folder)


class Clean(BaseModel):
    """Clean your repo branches."""

    dry_run: bool = True

    root_folder: DirectoryPath = Path.cwd()
    """The repo root folder."""

    def main(self):
        if self.dry_run:
            cleaner = controller.dry_cleaner
        else:
            cleaner = controller.real_cleaner
        controller.clean_branches(self.root_folder, cleaner=cleaner)


class Main(BaseModel):
    """Brush your branches."""

    sub_command: List | Clean

    def main(self):
        self.sub_command.main()


if __name__ == "__main__":
    out = clipstick.parse(Main)
    out.main()
