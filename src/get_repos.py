"""Serialize a list of all repositories that have a specific topic."""
import os
import gc
import timeit
from typing import List

import pandas as pd
from github import Github

from src.topics import ALL_TOPICS
from src.utils import write_to_json

# g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))
g = Github("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")

def create_repo_list(tracker_topic: str) -> None:
    """
    Create a JSON file with a list of all repos that have a specific topic.

    :param topic: The topic to search for.
    :type topic: str
    :return: None
    """
    repos: List[str] = []
    for repo in g.get_user().get_repos(affiliation="owner"):
        if tracker_topic in repo.get_topics():
            repos.append(repo.name)

    repo_dataframe = pd.DataFrame(repos, columns=["Name"])
    repo_dataframe["Name"] = repo_dataframe["Name"].apply(
        lambda x: f"[{x}](https://github.com/SauravMaheshkar/{x})"
    )
    repo_dataframe = repo_dataframe.set_index(keys="Name")

    _ = gc.collect()
    return repo_dataframe.to_markdown()


if __name__ == "__main__":
    for topic in ALL_TOPICS:
        print(
            timeit.timeit(
                "create_repo_list(topic)",
                setup="from __main__ import create_repo_list, topic",
                number=1,
            )
        )