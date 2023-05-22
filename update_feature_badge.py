import sys
from os.path import exists, getsize


# badge urls for staging/production feature diff
UP_TO_DATE = "https://img.shields.io/badge/Feature%20Diff-Up%20To%20Date-33CD56.svg"
ONE_FEATURE_BEHIND = "https://img.shields.io/badge/Feature%20Diff-Prod%20One%20Feature%20Behind-FFFF00.svg"
MORE_THAN_ONE_FEATURE_BEHIND = "https://img.shields.io/badge/Feature%20Diff-Prod%20More%20Than%20One%20Feature%20Behind-eb4034.svg"


def increase_feature_diff(path):
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


if __name__ == "__main__":
    method = sys.argv[1]
    path = sys.argv[2]
    repo_name = sys.argv[3]

    if not exists(path):
        with open(path, "x"):
            print(f"Creating file {path}")

    if getsize(path) == 0:
        with open(path, "a") as f:
            print("Creating feature diff badge")
            f.write(
                f"![Feature Diff]({UP_TO_DATE})](https://github.com/ZeitOnline/{repo_name}/actions?query=branch%3Amain)"
            )

    with open(path, "rt") as fin:
        fin = fin.read()
        if "![Feature Diff]" not in fin:
            first_line = open(path, "r").readlines()[0].split("\n")[0]
            print("Creating feature diff badge")
            open(path, "w").write(
                fin.replace(
                    first_line,
                    first_line
                    + f" ![Feature Diff]({UP_TO_DATE})](https://github.com/ZeitOnline/{repo_name}/actions?query=branch%3Amain)",
                )
            )

    if method == "increase":
        increase_feature_diff(path)
    elif method == "reset":
        reset_feature_diff(path)
