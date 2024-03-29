import sys
from os.path import exists, getsize


# badge urls for staging/production feature diff
UP_TO_DATE = "https://img.shields.io/badge/feature%20diff-up%20to%20date-33CD56.svg"
ONE_FEATURE_BEHIND = "https://img.shields.io/badge/feature%20diff-prod%20one%20feature%20behind-FFFF00.svg"
MORE_THAN_ONE_FEATURE_BEHIND = "https://img.shields.io/badge/feature%20diff-prod%20more%20than%20one%20feature%20behind-eb4034.svg"


def bump_feature_diff(path):
    with open(path, "rt") as fin:
        fin = fin.read()
        current_badge_url = fin.split("![Feature Diff](")[1].split(")")[0]
        if current_badge_url == UP_TO_DATE:
            new_badge_url = ONE_FEATURE_BEHIND
        elif current_badge_url == ONE_FEATURE_BEHIND:
            new_badge_url = MORE_THAN_ONE_FEATURE_BEHIND
        else:
            return

        with open(path, "wt") as fout:
            fout.write(fin.replace(current_badge_url, new_badge_url))
            print("Updated feature diff badge")


def reset_feature_diff(path):
    with open(path, "rt") as fin:
        fin = fin.read()
        current_badge_url = fin.split("![Feature Diff](")[1].split(")")[0]
        if current_badge_url == UP_TO_DATE:
            return

        new_badge_url = UP_TO_DATE
        with open(path, "wt") as fout:
            fout.write(fin.replace(current_badge_url, new_badge_url))
            print("Resetted feature diff badge")


def prepare(path):
    """
    Create the given file if it does not exist.
    Insert the new badge with state 'Up To Date' if not already present.
    """
    if not exists(path):
        with open(path, "x"):
            print(f"Creating file {path}")

    if getsize(path) == 0:
        with open(path, "a") as f:
            print("Creating feature diff badge in empty file")
            f.write(
                f"[![Feature Diff]({UP_TO_DATE})](https://github.com/ZeitOnline/{repo_name}/actions?query=branch%3Amain)"
            )
    else:
        with open(path, "rt") as fin:
            fin = fin.read()
            if "![Feature Diff]" not in fin:
                first_line = open(path, "r").readlines()[0].split("\n")[0]
                print("Creating feature diff badge")
                open(path, "w").write(
                    fin.replace(
                        first_line,
                        first_line
                        + f" [![Feature Diff]({UP_TO_DATE})](https://github.com/ZeitOnline/{repo_name}/actions?query=branch%3Amain)",
                    )
                )


if __name__ == "__main__":
    method = sys.argv[1]
    path = sys.argv[2]
    repo_name = sys.argv[3]

    prepare(path)

    if method == "bump":
        bump_feature_diff(path)
    elif method == "reset":
        reset_feature_diff(path)
