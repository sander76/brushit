from pathlib import Path
from duster import git
import pytest


def test_branch_with_existing_remote():
    branch_info = "my-branch,refs/remotes/origin/my-branch,"

    bi = git._parse(branch_info)

    assert bi == git.BranchInfo(
        "my-branch", git.Upstream("refs/remotes/origin/my-branch", exists=True)
    )


def test_branch_with_non_existing_remote():
    branch_info = "my-branch,refs/remotes/origin/my-branch, gone"

    bi = git._parse(branch_info)

    assert bi == git.BranchInfo(
        "my-branch", git.Upstream("refs/remotes/origin/my-branch", exists=False)
    )


@pytest.mark.parametrize(
    "branch_info", ["my-branch,,", "my-branch, ,", "my-branch ,,", "my-branch ,,  "]
)
def test_branch_no_remote(branch_info):
    bi = git._parse(branch_info)

    assert bi == git.BranchInfo("my-branch", None)


def test_this_repo__branch_info__success():
    git_working_folder = Path(__file__).parent.parent

    bi = git.branch_info(git_working_folder)

    for branch_info in bi.values():
        assert isinstance(branch_info, git.BranchInfo)
