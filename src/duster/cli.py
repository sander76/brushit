"""some cli"""
from itertools import chain
from pathlib import Path
import sys
from typing import Annotated, Literal
from pydantic import BaseModel, DirectoryPath, ValidationError
import tyro
from duster import duster
from duster import controller
from dataclasses import dataclass
from rich import print
from rich.table import Table


class List(BaseModel):
    root_folder: DirectoryPath = Path.cwd()
    """The repo root folder."""

    def main(self):
        controller.list_branches(self.root_folder)


class Branch(BaseModel):
    """Upperlevel"""


@dataclass
class Clean:
    """Clean your repo branches."""

    dry_run: bool = True

    root_folder: DirectoryPath = Path.cwd()
    """The repo root folder."""

    def main(self):
        if self.dry_run:
            cleaner = controller.branch_table
        controller.clean_branches(self.root_folder, cleaner=cleaner)


if __name__ == "__main__":
    try:
        out = tyro.cli(List | Clean)
        out.main()
    except ValidationError as err:
        print(err)
