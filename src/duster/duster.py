from duster.git import BranchInfo, BranchName
import questionary


def select_local_only_branches(all_branches: dict[BranchName, BranchInfo]) -> list[int]:
    local_branches = {
        name: branch for name, branch in all_branches.items() if branch.upstream is None
    }

    print(
        "These are branches without a remote. Deleting it here will probably result "
        "in loss of data."
    )

    result = questionary.checkbox(
        "Select the branches you want to delete", choices=list(local_branches.keys())
    ).ask()
    return result
